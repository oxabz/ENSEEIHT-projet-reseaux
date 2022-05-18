cat << EOF
sh /etc/dhcpcd.enter-hooks/iptables-reset-rules.sh
EOF >  /etc/dhcpcd.enter-hook

mkdir /etc/dhcpcd.enter-hooks/
cp iptables-setup.sh /etc/dhcpcd.enter-hooks/iptables-reset-rules.sh

chmod a+xrs /etc/dhcpcd.enter-hooks/iptables-reset-rules.sh