#!/usr/bin/env python3

from subprocess import run
import config.iptables as iptables
import config.appInstallation as appInstallation
import config.addressing as addressing
import wireguard.wireguard as wireguard
import config.ssh as ssh

# Enable interface to allow access to the internet
run("ip link set dev enp0s3 up".split(" "))

iptables.start()
appInstallation.start()
addressing.start()
ssh.start()
wireguard.start()

# Disable the previsouly enabled interface
run("ip link set dev enp0s3 down".split(" "))
