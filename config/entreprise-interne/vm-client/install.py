#!/usr/bin/env python3

from subprocess import run
import config.addressing as addressing
import config.ssh as ssh
import teamspeak_installation as ts

# Enable interface to allow access to the internet
run("ip link set dev enp0s3 up".split(" "))

addressing.start()
ssh.start()
ts.start()

# Disable the previsouly enabled interface
run("ip link set dev enp0s3 up".split(" "))
