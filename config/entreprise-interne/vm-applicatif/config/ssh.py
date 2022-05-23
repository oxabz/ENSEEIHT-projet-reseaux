from subprocess import run


def start():
    # Start SSH service
    run("systemctl start sshd".split(" "))
