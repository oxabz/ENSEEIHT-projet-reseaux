#!/bin/bash

ip a a 120.0.38.2/24 dev enp0s8
ip a a 192.168.1.254/24 dev enp0s9
ip r a default via 120.0.38.1


echo 1 > /proc/sys/net/ipv4/ip_forward

sudo systemctl start wg-quick@wg0

