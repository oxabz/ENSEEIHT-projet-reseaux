from subprocess import run

run(["podman-compose", "-f", "teamspeak.yml", "up"])

