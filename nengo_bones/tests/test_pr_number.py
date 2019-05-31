# pylint: disable=missing-docstring

from functools import partial
import os

from click.testing import CliRunner
import pytest

from nengo_bones.scripts import pr_number
from nengo_bones.tests.utils import assert_exit, make_has_line, write_file


def mocked_requests_get(url, repo=None, number=None):
    """Used to mock out github requests so that we don't get timed out."""
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    assert url == (
        "https://api.github.com/repos/%s/issues?state=all&sort=created" % repo)

    return MockResponse([{"number": number}])


@pytest.mark.parametrize("mode", ("repo", "conf-default", "conf-arg"))
def test_pr_number(monkeypatch, tmpdir, mode):
    repo = "a-repo/%s" % mode

    monkeypatch.setattr(
        pr_number.requests, "get",
        partial(mocked_requests_get, repo=repo, number=len(mode)))

    if mode != "repo":
        write_file(tmpdir, ".nengobones.yml", """
            project_name: Nengo Bones
            pkg_name: nengo-bones
            repo_name: %s
            version:
              major: 3
              minor: 2
              patch: 1
              release: False
        """ % repo)

    if mode == "repo":
        result = CliRunner().invoke(
            pr_number.main,
            [repo])
    elif mode == "conf-arg":
        result = CliRunner().invoke(
            pr_number.main,
            ['--conf-file',
             str(tmpdir.join('.nengobones.yml'))])
    else:
        original_dir = os.getcwd()
        os.chdir(str(tmpdir))
        try:
            result = CliRunner().invoke(pr_number.main)
        finally:
            os.chdir(original_dir)

    assert_exit(result, 0)

    lines = result.output.split('\n')
    has_line = make_has_line(lines, regex=True)
    assert has_line(r"about %s\.\.\." % repo)
    assert has_line(r"assigned #%s" % (len(mode) + 1))
