# ensconce-red

## Step 1. Setup Ansible Controller

```
sudo apt update
sudo apt upgrade
sudo apt install whois sshpass git ansible
```

SSH onto the machine, so the fingerprint is added to the known machines list. Maybe you have to setup SSH first...

```
sudo apt install openssh-server
```

Test connectivity to server. Ensure IP in both 'hosts' amd 'hosts_warm' files is correct, then run 
```
ansible -i hosts -u <USERID> -m raw -a 'lsb_release -a' test --ask-pass
```

## Step 2. Setup Target


```
ansible-playbook -i hosts setup_provisioner.yml -u neil --ask-pass -kK
```

Login with password should fail
```
ssh provisioner@192.168.122.184
```

Login with SSH key
```
ssh -i ssh/provisioner-rsa provisioner@192.168.122.184 
```

Basis VM configuration; updates, firewall, fail2ban, unattended-upgrades.
```
ansible-playbook -i hosts_warm setup_base.yml -u provisioner
```
Note: FAIL2BAN install will follow with an error 

ERROR! The requested handler 'restart fail2ban' was not found in either the main handlers list nor in the listening handlers list

Just re-run ansible!!!

Fail2Ban activation
```
sudo systemctl start fail2ban
sudo systemctl status fail2ban
```

## Step 3. Configure RED

```
ansible-playbook -i hosts_warm setup_red.yml -u provision
```














#    - name: Print return information from the previous task
#      ansible.builtin.debug:
#        var: sshkey