#!/usr/bin/env python3

import config.addressing as addressing
import config.ssh as ssh
import teamspeak_installation as ts

addressing.start()
ssh.start()
ts.start()