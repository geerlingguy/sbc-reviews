from pyinfra import host
from pyinfra.operations import apt, files
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
