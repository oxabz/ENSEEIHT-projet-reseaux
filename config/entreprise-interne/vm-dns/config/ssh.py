from subprocess import run


def start():
    run("systemctl start sshd")
