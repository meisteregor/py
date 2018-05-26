import subprocess
import platform
import re
import sys


class DistributionChecker(object):
    """Command redirection for Unix-like system compatibility"""
    @staticmethod
    def remote_check_distribution(server_name, server_ip):
        assert isinstance(server_name, str) and isinstance(server_ip, str)
        command = subprocess.Popen(
            ["ssh -T " + server_name + '@' + server_ip + ' ' + 'cat /etc/*-release | grep NAME='], shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        # Zero-index double-used for retrieval 1st str element inside 1st list element inside container type
        # from the command output. Regexp extracts info inside double quotes of this element.
        if sys.version_info.major == 2:
            distribution = re.findall(r'NAME="([^"]*)"', result[0])
        else:
            distribution = re.findall(r'NAME="([^"]*)"', result[0].decode('utf-8'))
        return distribution[0]

    @staticmethod
    def local_check_distribution():
        distribution = platform.linux_distribution()[0]
        return distribution
