from subprocess import run


def start():
    # Enabling SSH service
    run("systemctl start sshd".split(" "))
