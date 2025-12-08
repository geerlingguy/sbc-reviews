from pyinfra import host
from pyinfra.operations import apt, brew, dnf, files
from pyinfra.facts.server import Command, Home, LinuxName, Os, User

current_user=host.get_fact(User)
current_group=host.get_fact(Command, 'id -gn')
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

if host.get_fact(Os) == 'Darwin':
    brew.packages(
        name="Ensure prerequisites are installed (macOS).",
        packages=[
            "curl",
            "iperf3",
            "screenfetch",
            "stress-ng",
            "btop",
        ],
    )

files.directory(
    name="Ensure working directory is present",
    path=working_dir,
    present=True,
    user=current_user,
    group=current_group,
    _sudo=True,
)
