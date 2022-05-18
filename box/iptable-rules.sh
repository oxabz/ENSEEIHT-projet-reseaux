iptables --table nat --append POSTROUTING --out-interface enp0s8 -j MASQUERADE
iptables --append FORWARD --in-interface enp0s9 -j ACCEPT
echo 1 > /proc/sys/net/ipv4/ip_forward
service iptables restart


