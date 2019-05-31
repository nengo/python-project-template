"""Scripts for auto-generating nengo-bones files."""

from collections import OrderedDict
import os
import stat

import click
import jinja2

import nengo_bones


def render_template(ctx, cfg_key, output_file, template_file=None, **kwargs):
    """
    Render a template to file.

    Parameters
    ----------
    ctx : `click.Context`
        CLI context, containing information specified upstream.
    cfg_key : str
        The heading for the section in the config file containing config
        options specific to the template being rendered.
    output_file : str
        Filename for the rendered output file.
    template_file
        Filename for the input template file (default is
        ``output_file + ".template"``)
    kwargs : dict
        Will be passed on to the ``render`` function.
    """
    if template_file is None:
        template_file = output_file + ".template"

    template = ctx.obj["env"].get_template(template_file)

    output_file = os.path.join(ctx.obj["output_dir"], output_file)
    with open(output_file, "w") as f:
        f.write(template.render(
            bones_version=nengo_bones.__version__,
            **kwargs,
            # pass in the top-level config options as well
            # TODO: separate "top-level" config into its own section?
            **ctx.obj["config"],
            **ctx.obj["config"][cfg_key],
        ))


@click.group(invoke_without_command=True)
@click.option("--conf-file", default=None, help="Filepath for config file")
@click.option("--output-dir", default=".", help="Output directory for scripts")
@click.pass_context
def main(ctx, conf_file, output_dir):
    """Loads config file and sets up template environment.

    By default, this updates all templated files that are
    to be committed to the repository.

    We look in the current directory for a ``.templates`` folder. If it
    exists, any templates defined in that folder will be loaded first.
    Otherwise, built-in templates will be loaded from the
    ``nengo_bones/templates`` directory.

    If you are overriding a template in the ``.templates`` folder, the
    original built-in version of that template can be accessed with
    the ``templates/`` prefix. This is useful in ``include`` and
    ``extends`` tags. For example, to add text to the default
    ``LICENSE.rst`` template, put the following in
    ``.templates/LICENSE.rst.template``:

    .. code-block:: rst

       {% include "templates/LICENSE.rst.template %}

       Additional license info
       =======================
       ...

    """

    ctx.ensure_object(dict)

    config = nengo_bones.load_config(conf_file)

    bones_toplevel = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    # Load overridden templates first.
    # Builtins are referenced with templates/*.template
    override_dirs = []
    override_dirs.append(".templates")
    override_dirs.append(bones_toplevel)
    override_loader = jinja2.FileSystemLoader(override_dirs)
    # If those fail, use the builtins
    builtin_loader = jinja2.FileSystemLoader(
        os.path.join(bones_toplevel, "templates")
    )

    env = jinja2.Environment(
        loader=jinja2.ChoiceLoader([override_loader, builtin_loader]),
        trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    env.filters["rstrip"] = lambda s, chars: s.rstrip(chars)

    if not os.path.exists(output_dir):
        os.makedirs(os.path.normpath(output_dir))

    ctx.obj["env"] = env
    ctx.obj["config"] = config
    ctx.obj["output_dir"] = output_dir

    def check_cfg(name):
        name = name.replace("-", "_")
        if name not in config:
            print("No config entry detected for %s, skipping" % name)
            return False
        return True

    if ctx.invoked_subcommand is None:
        for cfg_name in nengo_bones.all_templated_files.values():
            if check_cfg(cfg_name):
                ctx.invoke(globals()[cfg_name])
    elif not check_cfg(ctx.invoked_subcommand):
        exit()


@main.command()
@click.pass_context
def ci_scripts(ctx):
    """Generate TravisCI shell scripts."""

    config = ctx.obj["config"]
    for params in config["ci_scripts"]:
        script_name = params.pop("template")
        template = ctx.obj["env"].get_template(script_name + ".sh.template")
        output_name = params.pop("output_name", script_name)
        path = os.path.join(ctx.obj["output_dir"], output_name + ".sh")

        with open(path, "w") as f:
            f.write(template.render(
                pkg_name=config["pkg_name"], repo_name=config["repo_name"],
                bones_version=nengo_bones.__version__, **params))

        # Mark CI script as executable
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)


@main.command()
@click.pass_context
def travis_yml(ctx):
    """Generate TravisCI config file."""

    config = ctx.obj["config"]

    jobs = config["travis_yml"]["jobs"]
    for job in jobs:
        # shortcuts for setting environment variables
        if "env" not in job:
            job["env"] = OrderedDict()
        for var in ("script", "test_args"):
            if var in job:
                job["env"][var] = job.pop(var)

    template = ctx.obj["env"].get_template(".travis.yml.template")
    with open(os.path.join(ctx.obj["output_dir"], ".travis.yml"), "w") as f:
        f.write(template.render(bones_version=nengo_bones.__version__,
                                **config["travis_yml"]))


@main.command()
@click.pass_context
def codecov_yml(ctx):
    """Generate codecov config file."""

    render_template(ctx, "codecov_yml", ".codecov.yml")


@main.command()
@click.pass_context
def license_rst(ctx):
    """Generate LICENSE.rst file."""

    render_template(ctx, "license_rst", "LICENSE.rst")


@main.command()
@click.pass_context
def contributing_rst(ctx):
    """Generate CONTRIBUTING.rst file."""

    render_template(ctx, "contributing_rst", "CONTRIBUTING.rst")


@main.command()
@click.pass_context
def contributors_rst(ctx):
    """Generate CONTRIBUTORS.rst file."""

    render_template(ctx, "contributors_rst", "CONTRIBUTORS.rst")


@main.command()
@click.pass_context
def manifest_in(ctx):
    """Generate MANIFEST.in file."""

    render_template(ctx, "manifest_in", "MANIFEST.in",
                    custom=ctx.obj["config"]["manifest_in"])


@main.command()
@click.pass_context
def setup_py(ctx):
    """Generate setup.py file."""

    config = ctx.obj["config"]

    setup_config = config["setup_py"]

    extras = OrderedDict()
    extra_types = {
        "classifiers": "list",
        "entry_points": "dict",
        "package_data": "dict",
    }
    # we iterate over setup_config (rather than extra_types) so that the
    # order in setup_config is preserved
    for key in list(setup_config.keys()):
        if key in extra_types:
            extras[key] = (extra_types[key], setup_config.pop(key))

    render_template(ctx, "setup_py", "setup.py",
                    extras=extras)


@main.command()
@click.pass_context
def setup_cfg(ctx):
    """Generate setup.cfg file."""

    render_template(ctx, "setup_cfg", "setup.cfg")


@main.command()
@click.pass_context
def docs_conf_py(ctx):
    """Generate docs/conf.py file."""

    output_dir = os.path.join(ctx.obj["output_dir"], "docs")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    render_template(ctx, "docs_conf_py", "docs/conf.py",
                    template_file="docs_conf.py.template")


@main.command()
@click.pass_context
def gitignore(ctx):
    """Generate setup.cfg file."""

    render_template(ctx, "gitignore", ".gitignore")


@main.command()
@click.pass_context
def version_py(ctx):
    """Generate {{ pkg_name }}/version.py file."""

    pkg_name = ctx.obj["config"]["pkg_name"]
    output_dir = os.path.join(ctx.obj["output_dir"], pkg_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    render_template(ctx, "version_py", "%s/version.py" % (pkg_name,),
                    template_file="version.py.template")


if __name__ == "__main__":
    main(obj={})  # pragma: no cover pylint: disable=no-value-for-parameter
