import subprocess
import platform
import os
import sys
from test_cases import *
from os.path import expanduser

# The absence of paramiko in the python's library
try:
    import paramiko
except ImportError:
    if platform.linux_distribution()[0] == 'debian' or platform.linux_distribution()[0] == 'Ubuntu':
        if sys.version_info.major == 2:
            os.system("apt install python-pip -y")
            os.system("pip install paramiko")
        else:
            os.system("apt install python3-pip -y")
            os.system("pip3 install paramiko")
    elif platform.linux_distribution()[0] == 'CentOS Linux':
        if sys.version_info.major == 2:
            os.system("yum install epel-release -y")
            os.system("yum install python-pip -y")
            os.system("pip install paramiko")
        else:
            os.system("pip3 install paramiko")
    else:
        raise OSError
finally:
    import paramiko


from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


class PasswordlessSSH(object):
    """Purpose: make the run more flexible, as it would not neccessary to input password all the time
    as run needs to install another package to prepare environment."""
    logger = logging.getLogger(__name__)

    @staticmethod
    def set(server_ip, server_name, password):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        # generate keys inside the python's env.
        PasswordlessSSH.logger.debug(cons.DEBUG_GENERATING_KEYS)
        key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, key_size=2048)
        public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH)
        pem = key.private_bytes(encoding=serialization.Encoding.PEM,
                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                encryption_algorithm=serialization.NoEncryption())
        private_key_str = pem.decode('utf-8')
        public_key_str = public_key.decode('utf-8')
        # local keys drop
        PasswordlessSSH.logger.debug(cons.DEBUG_DROP_KEYS)
        if not os.path.exists(expanduser("~") + '/.ssh'):
            os.makedirs(expanduser("~") + '/.ssh')
        os.chdir(expanduser("~") + '/.ssh')
        with open("id_rsa.pub", 'w') as f:
            f.write(public_key_str)
        with open("id_rsa", "w") as f:
            f.write(private_key_str)
        # for CentOS its necessary to change permissions as OS would not trust such a self-made crypto. So we want
        # to avoid additional system questions.
        os.system("chmod 400 ~/.ssh/id_rsa")
        # remote key fragment drop
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server_ip, port=22, username=server_name, password=password)
        sftp = ssh.open_sftp()
        try:
            sftp.mkdir(expanduser("~") + '/.ssh')
        except IOError:
            pass
        os.chdir(expanduser("~") + '/.ssh')
        sftp.put(expanduser("~") + '/.ssh/id_rsa.pub', '/' + var.SERVER_NAME + '/.ssh/authorized_keys')
        sftp.close()
        ssh.close()
        PasswordlessSSH.logger.info(cons.INFO_PASSWORLESS_SSH_DONE)

    @staticmethod
    def check(server_ip, server_name):
        """To ensure there is no passwordless SSH already exists between the machines"""
        assert isinstance(server_name, str) and isinstance(server_ip, str)
        try:
            subprocess.check_output(['ssh' + server_name + '@' + server_ip], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError:
            raise EnvironmentError


class Precondition(object):
    """Purpose: change server's config file and remote restart NFS to switch rw/ro permissions"""

    @staticmethod
    def put_file(machine_name, user_name, dir_name, filename, data):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(machine_name, username=user_name)
        sftp = ssh.open_sftp()
        try:
            sftp.mkdir(dir_name)
        except IOError:
            pass
        f = sftp.open(dir_name + '/' + filename, 'w')
        f.write(data)
        f.close()
        ssh.close()

    @staticmethod
    def ssh_to_server(server_name, server_ip, remote_command):
        command = subprocess.Popen(["ssh -T " + server_name + '@' + server_ip + ' ' + remote_command], shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            print >> command.stderr, "ERROR: %s" % error
        else:
            print(result)
