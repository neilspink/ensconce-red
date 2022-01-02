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

Test connectivity to server. Ensure the IP is updated in the 'hosts' file before testing 
```
ansible -i hosts -u <USERID> -m raw -a 'lsb_release -a' test --ask-pass
```

## Step 2. Setup Target

The username 'neil' given at the command line is a remote user which has sudoer privilieges. 
```
ansible-playbook -i hosts setup_provisioner.yml -u neil --ask-pass -kK
```

The following instructions assume the specified provisioner account user name will be 'provisioner'.

Test SSH login with password which should fail.
```
ssh provisioner@192.168.122.184
```

Add SSH private key to the ssh-agent (for ansible to be able to access the private key), then test login with SSH key. 
```
ssh-add ssh/provisioner-rsa
ssh -i ssh/provisioner-rsa provisioner@192.168.122.184 
```

Basis VM configuration; updates, firewall, fail2ban, unattended-upgrades.
```
ansible-playbook -i hosts setup_base.yml --user=provisioner --private-key=ssh/provisioner-rsa -kK
```

If FAIL2BAN install fails with an error:

ERROR! The requested handler 'restart fail2ban' was not found in either the main handlers list nor in the listening handlers list

Just re-run the ansible playbook.

Fail2Ban activation
```
sudo systemctl start fail2ban
sudo systemctl status fail2ban
```

## Step 3. Configure RED

```
ansible-playbook -i hosts setup_red.yml --user=provisioner --private-key=ssh/provisioner-rsa -kK
```
