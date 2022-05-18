systemctl disable NetworkManager.service
systemctl stop NetworkManager.service

systemctl enable systemd-networkd.service
systemctl start systemd-networkd.service

cp 20-wired.network /etc/systemd/network/20-wired.network

systemctl restart systemd-networkd.service