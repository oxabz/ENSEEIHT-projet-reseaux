#!/usr/bin/env python3

from subprocess import run
import network.addressing as network
import config.ssh as ssh
import config.appInstallation as appInstallation
import teamspeak.teamspeak as ts
import web.web as web

# Enable interface to allow access to the internet
run("ip link set dev enp0s3 up".split(" "))

appInstallation.start()
network.start()
ssh.start()
ts.start()
web.start()

# Disable the previsouly enabled interface
run("ip link set dev enp0s3 up".split(" "))
