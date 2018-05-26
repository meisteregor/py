# -*- coding: utf-8 -*-
import os
import sys
import logging
if sys.version_info[0] > 2:
    os.system('apt install python3-venv python3-pip')
    print('installingpython 3 pip')
else:
    os.system('apt install python-pip')
    print('installingpython 2 pip')
try:
    import paramiko
except ImportError:
    os.system('pip install paramiko')
    print('installing package')
try:
    # Module for generating keys into to the code's space
    from cryptography.hazmat.primitives import serialization

except ImportError as f:
    os.system('pip install cryptography')
    print('installing package cryptography')
finally:
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.backends import default_backend
logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-2s [%(asctime)s]  %(message)s',
                    filename='ssh_log.log')

port = 22  # Port is an only constant as it usually 22 for SSH connection


class Response(object):
    def __init__(self, out_, err_, exit_):
        self._out = out_
        self._err = err_
        self._exit = exit_

    @property
    def out(self):
        if hasattr(self._out, "readlines"):
            self._out = self.readlines()
        return self._out

    @property
    def error(self):
        return self._err

    @property
    def exit(self):
        return self._exit

    @property
    def is_success(self):
        return not self._err and self._exit == 0


def run_remote_cmd(cmd):
    assert isinstance(cmd, str)
    # Splitting output into basic sections
    _, stdout, stderr = ssh.exec_command(cmd)
    ret_code = stdout.channel.recv_exit_status()
    out = stdout.readlines()
    return out, ret_code, stderr


# Getting machines info for the first password connection from nearby machines.txt file
with open("machines.txt", "r") as f:
    list_of_machines = list(f)

# Generate private/public key pair
key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
                               key_size=2048)
# Get public key in OpenSSH format
public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
                                           serialization.PublicFormat.OpenSSH)
# Get private key in PEM container format
pem = key.private_bytes(encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption())
# Decode to printable strings
private_key_str = pem.decode('utf-8')
public_key_str = public_key.decode('utf-8')

# In-between result of generation. Full key pair to client, public part to remote machines.
# For our case windows machine will invoke remote connection with virtual linux machines
print('Private key = ')
print(private_key_str)
print('Public key = ')
print(public_key_str)

# Creating & changing windows dir and dropping the full key pair here
if not os.path.exists(os.environ.get("UserProfile") + '/.ssh'):
    os.makedirs(os.environ.get("UserProfile") + '/.ssh')
os.chdir(os.environ.get("UserProfile") + '/.ssh')
with open("id_rsa.pub", 'w') as f:
    f.write(public_key_str)
with open("id_rsa", "w") as f:
    f.write(private_key_str)

# Running func to provide all the machines from machines.txt with public part of generated key
for _ in xrange(len(list_of_machines)):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=list_of_machines[_].split()[0], port=port, username=list_of_machines[_].split()[1],
                password=list_of_machines[_].split()[2])

    run_remote_cmd('mkdir .ssh')

    sftp = ssh.open_sftp()
    sftp.put(os.environ.get("UserProfile") + "/.ssh/id_rsa.pub",
             '/home/' + list_of_machines[_].split()[1] + '/.ssh/authorized_keys')
    logging.info("Public key was successfully added to remote machine!")
    sftp.close()
    ssh.close()