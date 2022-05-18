ip link set up enp0s8
ip link set up enp0s9
ip a add 192.168.1/24 dev enp0s9
dhclient enp0s8& 