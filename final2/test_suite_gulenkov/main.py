import test_cases
from test_cases import *
import test_cases.variables as var
import test_cases.constants as cons
import logging

logger = logging.getLogger(test_cases.__name__)
logger.addHandler(CustomLogger.console)
logger.setLevel(logging.DEBUG)
logger.addHandler(CustomLogger.file_handler)


if __name__ == '__main__':
    # checking connections: network, hosts availability, ssh. if not passwordless ssh exists - setting it up also
    Network.check_local_internet()
    Network.check_host_availability()
    # setting Passwordless ssh connection if its not exists yet
    try:
        PasswordlessSSH.check(var.SERVER_IP, var.SERVER_NAME)
    except EnvironmentError:
        PasswordlessSSH.set(var.SERVER_IP, var.SERVER_NAME, var.SERVER_PASS)
    Network.check_remote_internet()
    # setting NFS
    NFS.set_nfs()
    # running positive tests and cleaning up
    TC1.run_tc()
    Cleaner.clear_share_dir()
    TC2.run_tc()
    Cleaner.clear_share_dir()
    TC3.run_tc()
    Cleaner.clear_share_dir()
    TC4.run_tc()
    Cleaner.clear_share_dir()
    Cleaner.remove_test_dir()
    TC5.run_tc()
    Cleaner.clear_share_dir()
    Cleaner.remove_test_dir()
    TC6.run_tc()
    Cleaner.clear_share_dir()
    # changing NFS permissions to read-only
    Precondition.put_file(var.SERVER_IP, var.SERVER_NAME, cons.DIR_FOR_CONDITION, cons.FILE_FOR_CONDITION,
                          cons.CHANGE_PRECONDITION_TO_RO)
    Precondition.ssh_to_server(var.SERVER_NAME, var.SERVER_IP, cons.REMOTE_RERUN_NFS)
    # running negative tests and cleaning up
    TC7.run_tc()
    Cleaner.clear_share_dir()
    Cleaner.remove_test_dir()
    TC8.run_tc()
    Cleaner.clear_share_dir()
    # returning NFS permissions back.
    Precondition.put_file(var.SERVER_IP, var.SERVER_NAME, cons.DIR_FOR_CONDITION, cons.FILE_FOR_CONDITION,
                          cons.CHANGE_PRECONDITION_TO_RW)
    Precondition.ssh_to_server(var.SERVER_NAME, var.SERVER_IP, cons.REMOTE_RERUN_NFS)
