# -*- coding: utf-8 -*-
import paramiko
import logging

logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-2s [%(asctime)s]  %(message)s')

hostname = '192.168.56.102'  # Here is to swap for testing passwordless connection to a specific machine
port = 22
username = "egorgulenkov"
# password = "gggg"


class Response(object):
    def __init__(self, out_, err_, exit_):
        self._out = out_
        self._err = err_
        self._exit = exit_

    @property
    def out(self):
        if hasattr(self._out, "readlines"):
            # self._out = self.readlines()
            pass
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


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, port=port, username=username)


def run_remote_cmd(cmd):
    assert isinstance(cmd, str)
    _, stdout, stderr = client.exec_command(cmd)
    ret_code = stdout.channel.recv_exit_status()
    out = stdout.readlines()
    return out, ret_code, stderr


print(run_remote_cmd('whoami'))
client.close()
