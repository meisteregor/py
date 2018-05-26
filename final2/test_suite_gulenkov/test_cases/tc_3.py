from test_cases import *


class TC3(UnixCommands):
    """From client side remove a file in a share directory. Condition: rw"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC3.logger.info(cons.INFO_REMOVE + cons.INFO_CONDITION_RW)
        step_1 = UnixCommands.ssh_to_server(var.SERVER_NAME, var.SERVER_IP,
                                            cons.REMOTE_TOUCH + var.HOST_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Inspection.check_ssh_to_server(step_1, TC3, 1)
        step_2 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_2, TC3, 2)
        Inspection.check_work_dir(TC3)
        step_3 = UnixCommands.remove_file(cons.TEST_FILE_NAME)
        Inspection.check_remove(step_3, TC3, 3)
        Inspection.check_list_of_files(TC3)
