This file is mainly to ensure directory correction.

Add SSH private key to the ssh-agent (for ansible to be able to access the private key), then test login with SSH key. 
```
ssh-add ssh/provisioner-rsa
ssh -i ssh/provisioner-rsa provisioner@192.168.122.184 
```

To remove the private key password.
```
ssh-add -d ssh/provisioner-rsa
```
