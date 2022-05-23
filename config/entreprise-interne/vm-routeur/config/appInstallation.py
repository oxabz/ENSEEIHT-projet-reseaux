#!/usr/bin/env python3

from subprocess import run


def start():
    # Packages that need to be installed
    packages = [
        "iptables-services",
        "iptables-utils",
        "wireguard-tools",
        "kmod-wireguard"
    ]

    # Install necessary package repositories
    run(["dnf", "install", "-y", "epel-release"])
    run("dnf install elrepo-release -y".split(" "))

    # Install necessary packages
    run(["dnf","install", "-y"] + packages)

    # Update server
    run("dnf update --refresh -y".split(" "))

    # Try to install necessary packages again just in case
    run(["dnf", "install", "-y"] + packages)
