#!/usr/bin/env python3

from subprocess import run


def start():
    # Packages that need to be installed
    packages = [
        "podman",
        "podman-compose",
        "python3-twisted"
    ]

    # Install epel
    run(["dnf", "install", "-y", "epel-release", "elrepo-release"] + packages)
    # Update server
    run("dnf update --refresh -y".split(" "))
    # Install packages
    run(["dnf", "install", "-y"] + packages)
