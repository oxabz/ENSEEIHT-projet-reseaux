#!/usr/bin/env python3

from subprocess import run


def start():
    run("twistd -n web --path ./web/website/ --listen tcp:8000 &")
