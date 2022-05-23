from subprocess import run


def start():
    # Start the SSH service
    run("systemctl start sshd".split(" "))
