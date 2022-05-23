#!/usr/bin/env python3

from subprocess import run


def start():

    external_int_name = "enp0s8"
    external_int_ip = "120.0.24.14"

    dns_server_ip = "10.0.0.20"
    dns_server_ext_ssh_port = "221"
    app_server_ip = "10.0.0.30"
    app_server_ext_ssh_port = "222"
    cli_server_ip = "10.0.0.40"
    cli_server_ext_ssh_port = "223"

    # Clear all iptables entries
    run("iptables -F".split(" "))
    run("iptables -t nat -F".split(" "))
    run("iptables -t mangle -F".split(" "))

    # Add Source NAT rule to enable internal clients to communicate with the outside
    run("iptables -t nat -A POSTROUTING -o {int} -j SNAT --to-source {ip}".format(int=external_int_name, ip=external_int_ip).split(" "))

    # Add Destination NAT rule to enable external clients to connect with internal clients via SSH
    # This needs to be disabled after the configuration for security reasons
    # NAT rule for the DNS server
    run("iptables -t nat -A PREROUTING -p tcp -d {dip} --dport {dport} -j DNAT --to-destination {rip}:22"
        .format(dip=external_int_ip, dport=dns_server_ext_ssh_port, rip=dns_server_ip)
        .split(" "))

    # NAT rule for the application server
    run("iptables -t nat -A PREROUTING -p tcp -d {dip} --dport {dport} -j DNAT --to-destination {rip}:22"
        .format(dip=external_int_ip, dport=app_server_ext_ssh_port, rip=app_server_ip)
        .split(" "))

    # NAT rule for the client computer
    run("iptables -t nat -A PREROUTING -p tcp -d {dip} --dport {dport} -j DNAT --to-destination {rip}:22"
        .format(dip=external_int_ip, dport=cli_server_ext_ssh_port, rip=cli_server_ip)
        .split(" "))
