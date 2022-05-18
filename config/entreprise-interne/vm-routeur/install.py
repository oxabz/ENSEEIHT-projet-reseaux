#!/usr/bin/env python3

import config.iptables as iptables
import config.appInstallation as appInstallation
import config.addressing as addressing

iptables.start()
appInstallation.start()
addressing.start()
