#!/usr/bin/env python3

from subprocess import run


def start():

    # Server properties
    hostname = "dns1"

    # Internal interface properties
    int_name = "enp0s8"
    int_ip = "10.0.0.20/24"

    # Gateway properties
    gateway_ip = "10.0.0.1"

    # === General configuration

    # Set hostname
    print("Setting hostname: {}".format(hostname))

    # === Interface configuration

    # Add nmcli connection
    run("nmcli con add type ethernet con-name {int1} ifname {int2}".format(int1=int_name, int2=int_name).split(" "))

    # Set ipv4 address
    run("nmcli connection modify {int} ipv4.addresses {ip}".format(int=int_name, ip=int_ip).split(" "))

    # Set gateway
    run("nmcli connection modify {int} ipv4.gateway {ip}".format(int=int_name, ip=gateway_ip).split(" "))

    # Set adressing method to manual
    run("nmcli connection modify {int} ipv4.method manual".format(int=int_name).split(" "))

    # Disble ipv6
    run("nmcli connection modify {int} ipv6.method disabled".format(int=int_name).split(" "))

    # Restart the interface to reload settings
    run("nmcli connection down {int}".format(int=int_name).split(" "))
    run("nmcli connection up {int}".format(int=int_name).split(" "))
