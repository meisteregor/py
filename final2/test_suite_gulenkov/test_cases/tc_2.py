from test_cases import *


class TC2(UnixCommands):
    """From client side rename a file from a share directory. Condition rw"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC2.logger.info(cons.INFO_RENAME + cons.INFO_CONDITION_RW)
        step_1 = UnixCommands.ssh_to_server(var.SERVER_NAME, var.SERVER_IP,
                                            cons.REMOTE_TOUCH + var.HOST_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Inspection.check_ssh_to_server(step_1, TC2, 1)
        step_2 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_2, TC2, 2)
        Inspection.check_work_dir(TC2)
        step_3 = UnixCommands.rename_file(cons.TEST_FILE_NAME, cons.TEST_FILE_2_NAME)
        Inspection.check_rename(step_3, TC2, 3)
        Inspection.check_list_of_files(TC2)
