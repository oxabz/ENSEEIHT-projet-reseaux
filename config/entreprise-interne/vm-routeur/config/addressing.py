#!/usr/bin/env python3

from subprocess import run


def start():

    # Server properties
    hostname = "router"

    # Internal interface properties
    internal_int_name = "enp0s9"
    internal_int_ip = "10.0.0.1/24"

    # External interface properties
    external_int_name = "enp0s8"
    external_int_ip = "120.0.24.14/30"

    # Gateway properties
    gateway_ip = "120.0.24.14"

    # === General configuration

    # Set hostname
    print("Setting hostname: {}".format(hostname))
    run("hostnamectl set-hostname {}".format(hostname).split(" "))

    # Disable firewalld
    run("systemctl stop firewalld".split(" "))
    run("systemctl disable firewalld".split(" "))
    run("systemctl mask firewalld".split(" "))
    
    # Enable ip forwarding
    run("echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.conf".split(" "))

    # === Gateway interface configuration

    # Add nmcli connection
    run("nmcli con add type ethernet con-name {int1} ifname {int2}".format(int1=external_int_name, int2=external_int_name).split(" "))

    # Set ipv4 address
    run("nmcli connection modify {int} ipv4.addresses {ip}".format(int=external_int_name, ip=external_int_ip).split(" "))

    # Set gateway
    run("nmcli connection modify {int} ipv4.gateway {ip}".format(int=external_int_name, ip=gateway_ip).split(" "))

    # Set adressing method to manual
    run("nmcli connection modify {int} ipv4.method manual".format(int=external_int_name).split(" "))

    # Disble ipv6
    run("nmcli connection modify {int} ipv6.method disabled".format(int=external_int_name).split(" "))

    # Restart the interface to reload settings
    run("nmcli connection down {int}".format(int=external_int_name).split(" "))
    run("nmcli connection up {int}".format(int=external_int_name).split(" "))

    # === Internal inteface configuration

    # Add nmcli connection
    run("nmcli con add type ethernet con-name {int1} ifname {int2}".format(int1=internal_int_name, int2=internal_int_name).split(" "))

    # Set ipv4 address
    run("nmcli connection modify {int} ipv4.addresses {ip}".format(int=internal_int_name, ip=internal_int_ip).split(" "))

    # Set adressing method to manual
    run("nmcli connection modify {int} ipv4.method manual".format(int=internal_int_name).split(" "))

    # Disble ipv6
    run("nmcli connection modify {int} ipv6.method disabled".format(int=internal_int_name).split(" "))

    # Restart the interface to reload settings
    run("nmcli connection down {int}".format(int=internal_int_name).split(" "))
    run("nmcli connection up {int}".format(int=internal_int_name).split(" "))
 