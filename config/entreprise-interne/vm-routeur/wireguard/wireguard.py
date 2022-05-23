#!/usr/bin/env python3

from subprocess import run


def start():
    # Create the wireguard configuration files directory
    run("mkdir -p /etc/wireguard/".split(" "))

    # Copy wireguard keys to wireguard configuration directory
    run("cp ./wireguard/publickey /etc/wireguard/".split(" "))
    run("cp ./wireguard/privatekey /etc/wireguard/".split(" "))

    # Copy wireguard configuration file to wireguard configuration directory
    run("cp ./wireguard/wg0.conf /etc/wireguard/".split(" "))

    # Start and enable wireguard service
    run("systemctl stop wg-quick@wg0.service".split(" "))
    run("systemctl enable wg-quick@wg0.service".split(" "))
    run("systemctl start wg-quick@wg0.service".split(" "))
