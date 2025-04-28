from pyinfra import host, logger
from pyinfra.operations import apt, files, git, pip, python, server
from pyinfra.facts.server import Home

working_dir=host.get_fact(Home) + "/Downloads"

# TODO: Make this dynamic based on CPU core count?
hpl_ps=1
hpl_qs=4

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

for python_version in ["3.11", "3.12", "3.13"]:
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

# Mind your Ps and Qs.
files.line(
    name="Mind your Ps",
    path="{}/top500-benchmark/config.yml".format(working_dir),
    line=r"  Ps: .",
    replace="  Ps: {}".format(hpl_ps),
)
files.line(
    name="Mind your Qs",
    path="{}/top500-benchmark/config.yml".format(working_dir),
    line=r"  Qs: .",
    replace="  Qs: {}".format(hpl_qs),
)

# TODO: It'd be nice to get live output from this command...
top500_result = server.shell(
    name="Run top500 playbook",
    commands="cd {}/top500-benchmark && ~/.local/bin/ansible-playbook main.yml --tags 'setup,benchmark'".format(working_dir),
)

def top500_result_callback():
    logger.info(f"\n```\n{top500_result.stdout}\n```")

python.call(
    name="Print top500 playbook result",
    function=top500_result_callback,
)
