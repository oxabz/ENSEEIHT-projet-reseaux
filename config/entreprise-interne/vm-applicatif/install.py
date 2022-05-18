from subprocess import run

#run(["dnf","up","--refresh"])
run("dnf up --refresh".split(" "))

