#!/usr/bin/env python3

from struct import pack
from subprocess import *


def start():
    packages = [
        "iptables-services",
        "iptables-utils",
    ]

    # install packages
    run(["dnf", "install", "-y"] + packages)