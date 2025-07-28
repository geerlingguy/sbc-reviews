from pyinfra import host
from pyinfra.operations import apt, dnf, files
from pyinfra.facts.server import Home, User, LinuxName

current_user=host.get_fact(User)
working_dir=host.get_fact(Home) + "/Downloads"
linux_name=host.get_fact(LinuxName)

if linux_name in ["Debian", "Ubuntu"]:
    apt.packages(
        name="Ensure prerequisites are installed (Debian).",
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

if linux_name in ["CentOS", "RedHat", "Fedora"]:
    dnf.packages(
        name="Ensure prerequisites are installed (RedHat).",
        packages=[
            "@development-tools",
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
