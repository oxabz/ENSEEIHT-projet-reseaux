#!/usr/bin/env python3

from subprocess import run


def start():
    # Packages that need to be installed
    packages = []

    # wget on url ts client
    run("wget -O /usr/bin/TeamSpeak3-Client-linux_amd64-3.5.6.run https://files.teamspeak-services.com/releases/client/3.5.6/TeamSpeak3-Client-linux_amd64-3.5.6.run".split(" "))
    run("cp assets/teamspeak /usr/bin/".split(" "))
    run("cp assets/teamspeak.Desktop /usr/share/applications".split(" "))
    run("chmod a+x /usr/bin/TeamSpeak3-Client-linux_amd64-3.5.6.run".split(" "))
    run("chmod a+x /usr/bin/teamspeak".split(" "))



