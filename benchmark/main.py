import os
from pyinfra import local, host
from pyinfra.operations import apt, files, server
from pyinfra.facts.server import Home, User

current_user=host.get_fact(User)
working_dir=host.get_fact(Home) + "/Downloads"

apt.packages(
    name="Ensure prerequisites are installed.",
    packages=[
        "build-essential",
        "curl",
        "git",
        "screenfetch",
        "iperf3",
        "stress-ng",
        "s-tui",
        "btop",
    ],
    _sudo=True,
)

files.directory(
    name="Ensure working directory is present",
    path=working_dir,
    present=True,
    user=current_user,
    group=current_user,
    _sudo=True,
)

local.include("tasks/basics.py")
# local.include("tasks/tinymembench.py")
# local.include("tasks/geekbench.py")
# local.include("tasks/disk-benchmark.py")
local.include("tasks/top500.py")
local.include("tasks/ollama-benchmark.py")
local.include("tasks/sbc-general-benchmark.py")
