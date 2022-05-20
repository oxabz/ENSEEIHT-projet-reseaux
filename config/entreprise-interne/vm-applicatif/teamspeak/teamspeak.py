from subprocess import run

def start():
    run(["podman-compose", "-f", "teamspeak.yml", "up"])

