#!/usr/bin/env bash

apt update
apt dist-upgrade
apt install nmap
apt install sqlmap
apt install gobuster
apt install dirb

echo "Terminou :)"
