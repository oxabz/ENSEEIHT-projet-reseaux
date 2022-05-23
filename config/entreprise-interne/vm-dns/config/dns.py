#!/usr/bin/env python3

from subprocess import run



def start():
    run("sudo systemctl enable named".split(" "));

