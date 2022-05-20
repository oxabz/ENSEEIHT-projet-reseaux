#!/bin/bash

IP_INT=$( ip -f inet addr show enp0s8 | grep -Po 'inet \K[\d.]+')

# Désactiver le pare-feu
iptablesoff() {

  # Supprime tous les filtres
  iptables -F
  iptables -t filter -F
  iptables -t nat -F
  iptables -t mangle -F

  # Attribut une politiques "ACCEPT" aux tables
  iptables -P INPUT ACCEPT
  iptables -P FORWARD ACCEPT
  iptables -P OUTPUT ACCEPT

  iptables -t filter -P INPUT ACCEPT
  iptables -t filter -P FORWARD ACCEPT
  iptables -t filter -P OUTPUT ACCEPT

  iptables -t nat -P PREROUTING ACCEPT
  iptables -t nat -P POSTROUTING ACCEPT
  iptables -t nat -P OUTPUT ACCEPT

  iptables -t mangle -P PREROUTING ACCEPT
  iptables -t mangle -P INPUT ACCEPT
  iptables -t mangle -P FORWARD ACCEPT
  iptables -t mangle -P OUTPUT ACCEPT
  iptables -t mangle -P POSTROUTING ACCEPT

  echo "[Firewall stopped]"
}

# Activer le pare-feu
iptableson() {
  echo "[Démarrage du pare-feu]"

  ### EFFACE TOUT LES PARAMETRES
  iptables -F
  iptables -t filter -F
  iptables -t nat -F
  iptables -t mangle -F

  ### REGLES DE FILTRAGE
  # Autoriser le Loopback
  iptables -A INPUT -i lo -j ACCEPT
  iptables -A OUTPUT -o lo -j ACCEPT

  ### Ne pas casser les connexions déjà établies
  iptables -t filter -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
  iptables -t filter -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
  iptables -t filter -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

  ### PING (ICMP)
  iptables -t filter -A INPUT -p icmp -j ACCEPT
  iptables -t filter -A OUTPUT -p icmp -j ACCEPT
  iptables -t filter -A FORWARD -p icmp -j ACCEPT

  ### Règles de NAT
  # Clients -> Internet
  iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j SNAT --to-source ${IP_INT}

  ### Clients to Router
  # SSH
  iptables -t filter -A INPUT -i enp0s9 -p tcp --dport ssh -j ACCEPT 

  ### Client to Outside
  iptables -t filter -A FORWARD -i enp0s9 -j ACCEPT

  echo "[Firewall started]"
}

echo $IP_INT

if [ !$IP_INT ];then
#  iptablesoff
  iptableson
  ip route add default dev enp0s8
fi