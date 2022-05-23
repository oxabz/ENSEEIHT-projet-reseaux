
#!/usr/bin/env python3

from subprocess import run


def start():
    # Packages that need to be installed
    packages = [
        "bind"
    ]

    # Install epel
    run(["dnf", "install", "-y", "epel-release", "elrepo-release"] + packages)
    # Update server
    run("dnf update --refresh -y".split(" "))
    # Install packages
    run(["dnf", "install", "-y"] + packages)
