import subprocess
import os
import sys
from test_cases.distribution_checker import DistributionChecker


class UnixCommands(object):
    """Main test app runner. Both local and remote UNIX commands necessary for the run implemented here."""

    @staticmethod
    def write_into_file(file_name, data):
        """compatibility of python's exceptions"""
        assert isinstance(data, str)
        if sys.version_info.major == 2:
            try:
                with open(file_name, 'w') as _:
                    subprocess.call(['echo', data], stdout=_)
                return 0
            except StandardError as Error:
                return str(Error)
        else:
            try:
                with open(file_name, 'w') as _:
                    subprocess.call(['echo', data], stdout=_)
                return 0
            except Exception as Error:
                return str(Error)

    @staticmethod
    def remote_restart_rpcbind(server_name, server_ip):
        try:
            subprocess.check_output(["ssh -T " + server_name + '@' + server_ip + ' ' + 'service rpcbind restart'],
                                    shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def remote_restart_nfs(server_name, server_ip):
        distribution = DistributionChecker.remote_check_distribution(server_name, server_ip)
        if distribution == 'CentOS Linux':
            restart_command = 'service nfs restart'
        else:
            restart_command = '/etc/init.d/nfs-kernel-server restart'
        try:
            subprocess.check_output(["ssh -T " + server_name + '@' + server_ip + ' ' + restart_command], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def remote_disable_firewall(server_name, server_ip):
        distribution = DistributionChecker.remote_check_distribution(server_name, server_ip)
        if str(distribution) == 'CentOS Linux':
            try:
                subprocess.check_output(
                    ["ssh -T " + server_name + '@' + server_ip + ' ' + 'systemctl disable firewalld'], shell=True,
                    stderr=subprocess.STDOUT)
                return 0
            except subprocess.CalledProcessError as Error:
                return Error.output
        else:
            pass

    @staticmethod
    def remote_stop_firewall(server_name, server_ip):
        distribution = DistributionChecker.remote_check_distribution(server_name, server_ip)
        if str(distribution) == 'CentOS Linux':
            try:
                subprocess.check_output(["ssh -T " + server_name + '@' + server_ip + ' ' + 'systemctl stop firewalld'],
                                        shell=True, stderr=subprocess.STDOUT)
                return 0
            except subprocess.CalledProcessError as Error:
                return Error.output
        else:
            pass

    @staticmethod
    def remote_install_nfs_packages(server_name, server_ip):
        distribution = DistributionChecker.remote_check_distribution(server_name, server_ip)
        if distribution == "CentOS Linux":
            os_install_command = 'yum install nfs* -y'
        else:
            os_install_command = 'apt install nfs* -y'
        try:
            subprocess.Popen(["ssh -T " + server_name + '@' + server_ip + ' ' + os_install_command], shell=True,
                             stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def local_install_nfs_packages():
        distribution = DistributionChecker.local_check_distribution()
        if distribution == 'CentOS Linux':
            install_command = "yum install nfs* -y"
        else:
            install_command = "apt install nfs* -y"
        try:
            subprocess.check_output([install_command], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def remote_ping_web(server_name, server_ip, remote_command):
        command = subprocess.Popen(["ssh -T " + server_name + '@' + server_ip + ' ' + remote_command], shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            return error
        else:
            return result

    @staticmethod
    def ping(address):
        try:
            subprocess.check_output(['ping -c 2 ' + address], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def mount(ip, server_dir, local_dir):
        try:
            subprocess.check_output(['mount ' + ip + ':' + server_dir + ' ' + local_dir], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def check_remote_dir(server_name, server_ip, remote_command, arg):
        command = subprocess.Popen(["ssh -T " + server_name + '@' + server_ip + ' ' + remote_command + ' ' + arg],
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            return error
        else:
            return result

    @staticmethod
    def check_local_dir(path):
        assert isinstance(path, str)
        if not os.path.exists(path):
            os.system('mkdir -p ' + path)

    @staticmethod
    def change_directory(path):
        assert isinstance(path, str)
        try:
            os.chdir(path)
            return 0
        except StandardError as Error:
            return str(Error)

    @staticmethod
    def pwd():
        command = subprocess.check_output(["pwd"], shell=True)
        return "Your work directory is {} ".format(command)

    @staticmethod
    def ls():
        command = subprocess.check_output(["ls"], shell=True)
        return "A list of files in current directory: \n {} ".format(command)

    @staticmethod
    def make_dir(dir_name):
        assert isinstance(dir_name, str)
        try:
            subprocess.check_output(["mkdir " + dir_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def remove_dir(dir_name):
        assert isinstance(dir_name, str)
        try:
            subprocess.check_output(["rmdir ./" + dir_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def touch_file(file_name):
        assert isinstance(file_name, str)
        try:
            subprocess.check_output(["touch ./" + file_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def ssh_to_server(server_name, server_ip, remote_command):
        assert isinstance(server_ip, str) and isinstance(server_name, str) and isinstance(remote_command, str)
        command = subprocess.Popen(["ssh -T " + server_name + '@' + server_ip + ' ' + remote_command], shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            print >> command.stderr, "ERROR: %s" % error
        else:
            print(result)

    @staticmethod
    def read_from_file(file_name):
        list_data = []
        with open(file_name, 'r') as f:
            for line in f:
                list_data.append(line)
        return list_data

    @staticmethod
    def cat_file(file_name):
        assert isinstance(file_name, str)
        try:
            subprocess.check_output(["cat " + file_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def copy_file(file_name, path_for_copy):
        assert isinstance(file_name, str) and isinstance(path_for_copy, str)
        try:
            subprocess.check_output(["cp " + file_name + " " + path_for_copy], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def move_file(file_name, path_for_move):
        assert isinstance(file_name, str) and isinstance(path_for_move, str)
        try:
            subprocess.check_output(["mv " + file_name + " " + path_for_move], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def rename_file(file_name, new_file_name):
        return UnixCommands.move_file(file_name, new_file_name)

    @staticmethod
    def remove_file(file_name):
        assert isinstance(file_name, str)
        str_without_asterisk = (file_name.replace('*', ''))
        try:
            subprocess.check_output(["rm -f ./" + str_without_asterisk], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def run_script(name_scr):
        assert isinstance(name_scr, str)
        try:
            subprocess.check_output(["sh " + name_scr], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output
