#!/bin/sh

sudo apt install -y whois sshpass git ansible
ansible-galaxy collection install community.mongodb
