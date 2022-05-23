
#!/usr/bin/env python3

from subprocess import run


def start():
    packages = [
        "bind"
    ]

    # install epel
    run(["dnf", "install", "-y", "epel-release", "elrepo-release"] + packages)
    # update server
    run("dnf update --refresh -y".split(" "))
    # install packages
    run(["dnf", "install", "-y"] + packages)
