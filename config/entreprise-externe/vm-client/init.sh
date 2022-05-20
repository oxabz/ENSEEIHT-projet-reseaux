#!/bin/bash

ip a a 192.168.1.1 dev enp0s8
ip r a default via 192.168.1.254 
