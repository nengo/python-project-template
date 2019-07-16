"""Applies validation to auto-generated files."""

import difflib
import os
import sys

import click

from nengo_bones import __version__
from nengo_bones.config import load_config, sections
from nengo_bones.templates import BonesTemplate, load_env


@click.command()
@click.option("--root-dir", default=".",
              help="Directory containing files to be checked")
@click.option("--conf-file", default=None, help="Filepath for config file")
@click.option(
    "--verbose",
    is_flag=True,
    help="Show more information about failed checks.",
)
def main(root_dir, conf_file, verbose):
    """
    Validates auto-generated project files.

    Note: This does not check the ci scripts, because those are generated
    on-the-fly in TravisCI (so any ci files we do find are likely local
    artifacts).
    """

    config = load_config(conf_file)
    env = load_env()

    click.echo("*" * 50)
    click.echo("Checking content of nengo-bones generated files:")
    click.echo("root dir: %s\n" % root_dir)

    passed = True

    for filename in sections.values():
        click.echo(filename + ":")

        # TODO: Ensure that the file is there <=> it is in the config
        if not os.path.exists(os.path.join(root_dir, filename)):
            click.echo("  File not found")
            continue

        with open(os.path.join(root_dir, filename)) as f:
            current_lines = f.readlines()

        for line in current_lines[:50]:
            if "Automatically generated by nengo-bones" in line:
                break
        else:
            click.echo("  This file was not generated with nengo-bones")
            continue

        template = BonesTemplate(filename, env)
        new_lines = template.render(
            version=__version__,
            **template.get_render_data(config),
        ).splitlines(keepends=True)

        diff = list(difflib.unified_diff(
            current_lines,
            new_lines,
            fromfile="current %s" % (filename,),
            tofile="new %s" % (filename,),
        ))

        if len(diff) > 0:
            click.secho(
                "  Content does not match nengo-bones (version %s);\n"
                "  please update by running `bones-generate` from\n"
                "  the root directory." % (__version__,),
                fg="red")
            if verbose:
                click.echo("\n  Full diff")
                click.echo("  =========")
                for line in diff:
                    click.echo("  %s" % (line.strip("\n"),))
            passed = False
        else:
            click.secho("  Up to date", fg="green")

    click.echo("*" * 50)

    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()  # pragma: no cover pylint: disable=no-value-for-parameter
