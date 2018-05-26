from test_cases import *


class TC4(UnixCommands):
    """Copy a file from server side into a test directory on client side. Condition: rw"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC4.logger.info(cons.INFO_COPY + cons.INFO_CONDITION_RW)
        step_1 = UnixCommands.ssh_to_server(var.SERVER_NAME, var.SERVER_IP, cons.REMOTE_TOUCH +
                                            var.HOST_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Inspection.check_ssh_to_server(step_1, TC4, 1)
        step_2 = UnixCommands.make_dir(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Inspection.check_make_dir(step_2, TC4, 2)
        step_3 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_3, TC4, 3)
        Inspection.check_work_dir(TC4)
        step_4 = UnixCommands.copy_file(cons.TEST_FILE_NAME, cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Inspection.check_copy(step_4, TC4, 4)
        # verification of a file in test directory
        step_5 = UnixCommands.cat_file(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME + '/' + cons.TEST_FILE_NAME)
        Inspection.check_cat_file(step_5, TC4, 5)
        Inspection.check_list_of_files(TC4)


