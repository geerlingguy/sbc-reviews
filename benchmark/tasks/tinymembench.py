from pyinfra import logger
from pyinfra.operations import git, python, server

git.repo(
    name="Clone tinymembench with git.",
    src="https://github.com/rojaster/tinymembench.git",
    dest="{working_dir}/tinymembench",
)

server.shell(
    name="Build tinymembench",
    commands="cd {working_dir}/tinymembench && make",
)

tinymembench_result = server.shell(
    name="Run tinymembench",
    commands="{working_dir}/tinymembench/tinymembench",
)

def callback():
    logger.info(f"\n```\n{tinymembench_result.stdout}\n```")

python.call(
    name="Print tinymembench results",
    function=callback,
)
