# ensconce-red

Setup one or more Linux machines, harden the security, configure GitHub CI/CD deployment, and set up an account on the target machine specifically for the application being deployed.

It is recommended to only use this with private repositories, because forks of your repository can potentially run dangerous code on your self-hosted runner machine by creating a pull request that executes the code in a workflow (reference GitHub [self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#about-self-hosted-runners)).

## Preparation

You will choose three accounts names required for; annsible automated provioning, github deployment and for application run. 

The setup_base.yml will configure unattended-upgrades on the target machines with an automatic reboot time 02:45. You may wish a differnt time. 

## Setup Ansible Controller

```
sudo apt update
sudo apt upgrade
sudo apt install whois sshpass git ansible
```

SSH onto the machine, so the fingerprint is added to the known machines list. Maybe you have to setup SSH first...

```
sudo apt install openssh-server
```

## Prepare Target IPs

The 'hosts' file needs to be given the IP address of the target machine(s). 

Test connectivity and ensure the IPs is reachable. 
```
ansible -i hosts -u <USERID> -m raw -a 'lsb_release -a' test --ask-pass
```

## Create Provisioner Account on Targets Machines

The username 'neil' given at the command line is a remote user which has sudoer privilieges. 
```
ansible-playbook -i hosts main.yml -u neil --ask-pass -kK
```
A secret password will be displayed at the end of the run. You will need it for the next steps.

The following instructions assume the specified provisioner account user name will be 'provisioner'.

Test SSH login with password which should fail.
```
ssh provisioner@192.168.122.184
```

Add SSH private key to the ssh-agent (for ansible to be able to access the private key), then test login with SSH key. 
```
ssh-add ssh/provisioner-rsa
ssh -i ssh/provisioner-rsa provisioner@192.168.122.184 
exit
```

## GitHub Runner Notes

Information on the latest command line arguements are provided by the tool itself:
```
./config.sh --help
```