from pyinfra import host, logger
from pyinfra.operations import git, python, server
from pyinfra.facts.server import Home

working_dir=host.get_fact(Home) + "/Downloads"

git.repo(
    name="Clone tinymembench with git.",
    src="https://github.com/rojaster/tinymembench.git",
    dest="{}/tinymembench".format(working_dir),
)

server.shell(
    name="Build tinymembench",
    commands="cd {}/tinymembench && make".format(working_dir),
)

tinymembench_result = server.shell(
    name="Run tinymembench",
    commands="{}/tinymembench/tinymembench".format(working_dir),
)

def tinymembench_result_callback():
    logger.info(f"\n```\n{tinymembench_result.stdout}\n```")

python.call(
    name="Print tinymembench results",
    function=tinymembench_result_callback,
)
