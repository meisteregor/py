from test_cases import *
from test_cases.distribution_checker import DistributionChecker


class NFS(UnixCommands):
    """Setting up NFSv4 stage. Some steps will be skipped if server do not belong to Red Hat Family"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def set_nfs():
        """All the responses with its numeric count may be perceived as an NFS installation guide including cross
        platform Debian&RedHat Families of UNIX."""
        NFS.logger.debug(cons.DEBUG_SETTING_NFS_STAGE)
        response_1 = UnixCommands.check_local_dir(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_local_dir(response_1, NFS)
        response_2 = UnixCommands.check_remote_dir(var.SERVER_NAME, var.SERVER_IP, cons.MAKEDIR, var.HOST_PATH_TO_SHARE)
        Inspection.check_remote_dir(response_2, NFS)
        response_3 = UnixCommands.remote_install_nfs_packages(var.SERVER_NAME, var.SERVER_IP)
        Inspection.check_if_nfs_packages_installed(response_3, NFS)
        response_4 = UnixCommands.local_install_nfs_packages()
        Inspection.check_if_nfs_packages_installed(response_4, NFS)
        response_5 = Precondition.put_file(var.SERVER_IP, var.SERVER_NAME, cons.DIR_FOR_CONDITION,
                                           cons.FILE_FOR_CONDITION, cons.CHANGE_PRECONDITION_TO_RW)
        Inspection.check_config_rewritten_successfully(response_5, NFS)
        # if DistributionChecker.remote_check_distribution(var.SERVER_NAME, var.SERVER_IP) == cons.RED_HAT_FAMILY:
        response_6 = UnixCommands.remote_restart_rpcbind(var.SERVER_NAME, var.SERVER_IP)
        Inspection.is_rpcbind_restarted(response_6, NFS)
        response_7 = UnixCommands.remote_restart_nfs(var.SERVER_NAME, var.SERVER_IP)
        Inspection.is_nfs_restarted(response_7, NFS)
        if DistributionChecker.remote_check_distribution(var.SERVER_NAME, var.SERVER_IP) == cons.RED_HAT_FAMILY:
            response_8 = UnixCommands.remote_disable_firewall(var.SERVER_NAME, var.SERVER_IP)
            Inspection.is_fw_disabled(response_8, NFS)
            response_9 = UnixCommands.remote_stop_firewall(var.SERVER_NAME, var.SERVER_IP)
            Inspection.is_fw_stopped(response_9, NFS)
        response_10 = UnixCommands.mount(var.SERVER_IP, var.HOST_PATH_TO_SHARE, var.LOCAL_PATH_TO_SHARE)
        Inspection.is_mounted(response_10, NFS)
