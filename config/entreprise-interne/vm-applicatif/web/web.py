#!/usr/bin/env python3
import sys
from subprocess import Popen


def start():
    Popen("twistd -n web --path ./web/website/ --listen tcp:8080".split(" ") + sys.argv[1:] )
