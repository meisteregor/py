from test_cases import *


class TC8(UnixCommands):
    """From client side remove a file from a share directory. Condition: ro"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC8.logger.info(cons.INFO_REMOVE + cons.INFO_CONDITION_RO)
        step_1 = UnixCommands.ssh_to_server(var.SERVER_NAME, var.SERVER_IP,
                                            cons.REMOTE_TOUCH + var.HOST_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Inspection.check_ssh_to_server(step_1, TC8, 1)
        step_2 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_2, TC8, 2)
        Inspection.check_work_dir(TC8)
        step_3 = UnixCommands.remove_file(cons.TEST_FILE_NAME)
        Inspection.check_remove(step_3, TC8, 3)
        Inspection.check_list_of_files(TC8)
