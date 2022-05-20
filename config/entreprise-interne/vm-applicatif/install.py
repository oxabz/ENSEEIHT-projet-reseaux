#!/usr/bin/env python3

import network.addressing as network
import config.ssh as ssh
import config.appInstallation as appInstallation
import teamspeak.teamspeak as ts

appInstallation.start()
network.start()
ssh.start()
ts.start()
