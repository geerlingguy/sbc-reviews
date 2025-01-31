from pyinfra import host, logger
from pyinfra.operations import apt, files, git, pip, python, server
from pyinfra.facts.server import Home

working_dir=host.get_fact(Home) + "/Downloads"

git.repo(
    name="Clone top500 with git.",
    src="https://github.com/geerlingguy/top500-benchmark.git",
    dest="{}/top500-benchmark".format(working_dir),
)

apt.packages(
    name="Install Ansible dependencies",
    packages=["python3-pip"],
    update=True,
    _sudo=True,
)

# TODO: Dynamically set Python version here. (3.11/3.12...)
for python_version in ["3.11", "3.12"]:
    files.file(
        name="Remove Python {} EXTERNALLY-MANAGED file".format(python_version),
        path="/usr/lib/python{}/EXTERNALLY-MANAGED".format(python_version),
        present=False,
        _sudo=True,
    )

pip.packages(
    name="Install Ansible",
    packages=["ansible"],
)

server.shell(
    name="Copy config files into place",
    commands=[
        "cp {}/top500-benchmark/example.config.yml {}/top500-benchmark/config.yml".format(working_dir, working_dir),
        "cp {}/top500-benchmark/example.hosts.ini {}/top500-benchmark/hosts.ini".format(working_dir, working_dir),
    ],
)

# TODO: Modify config.yml, hpl_dat_opts for Ps and Qs...

# TODO: It'd be nice to get live output from this command...
top500_result = server.shell(
    name="Run top500 playbook",
    commands="cd {}/top500-benchmark && ~/.local/bin/ansible-playbook main.yml --tags 'setup,benchmark'".format(working_dir),
)

def callback():
    logger.info(f"\n```\n{top500_result.stdout}\n```")

python.call(
    name="Print top500 playbook result",
    function=callback,
)
