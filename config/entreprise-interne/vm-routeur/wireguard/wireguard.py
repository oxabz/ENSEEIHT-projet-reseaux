#!/usr/bin/env python3

from subprocess import run


def start():
    int_ip = "10.10.10.1/24"
    listen_port = "51820"

    # create the wireguard configuration files directory
    run("mkdir -p /etc/wireguard".split(" "))

    # generate private and public key pair
    run("wg genkey | sudo tee privatekey | wg pubkey | sudo tee /etc/wireguard/publickey".split(" "))

    privatekey = run("cat privatekey".split(" "))

    # wireguard config file
    wg_config = """
    [Interface]
    PrivateKey = {pkey}
    Address = {ip}
    ListenPort = {port}
    SaveConfig = true
    """.format(pkey=privatekey, ip=int_ip, port=listen_port)

    run(["echo", wg_config])

    # run("echo '{}' > /etc/wireguard/wg0.conf".format(wg_config))

    # run("".split(" "))
