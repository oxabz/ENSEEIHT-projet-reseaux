from subprocess import run


def start():
    # Start teampseak service
    run(["podman-compose", "-f", "./teamspeak/teamspeak.yml", "up"])

