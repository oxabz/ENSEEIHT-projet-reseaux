#!/usr/bin/env python3

from subprocess import run

def start():
    external_int_name = "enp0s9"
    external_int_ip = "120.0.24.14"

    run("iptables -t nat -A POSTROUTING -o {int} -j SNAT --to-source {ip}".format(int=external_int_name, ip=external_int_ip).split(" "))