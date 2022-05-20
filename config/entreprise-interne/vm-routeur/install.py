#!/usr/bin/env python3

import config.iptables as iptables
import config.appInstallation as appInstallation
import config.addressing as addressing
import wireguard.wireguard as wireguard

iptables.start()
appInstallation.start()
addressing.start()
# disable automatic wireguard install for now
# wireguard.start()
