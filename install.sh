#!system/bin/sh
apt update -y
apt upgrade -y
pkg install python
pkg install python2
pip2 install mechanize 
pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg update && pkg upgrade -y
pkg install git python -y
termux-setup-storage -y
git clone https://github.com/EsanAhmedAbir/test
cd test
pip install --upgrade pip
pip install -r requirements.txt
clear

