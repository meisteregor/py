from test_cases import *


class TC7(UnixCommands):
    """From a test directory on client side move a file into a share directory. Condition: ro"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC7.logger.info(cons.INFO_MOVE + cons.INFO_CONDITION_RO)
        step_1 = UnixCommands.make_dir(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Inspection.check_make_dir(step_1, TC7, 1)
        step_2 = UnixCommands.change_directory(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Inspection.check_change_dir(step_2, TC7, 2)
        Inspection.check_work_dir(TC7)
        step_3 = UnixCommands.touch_file(cons.TEST_FILE_NAME)
        Inspection.check_touch_file(step_3, TC7, 3)
        step_4 = UnixCommands.move_file(cons.TEST_FILE_NAME, var.LOCAL_PATH_TO_SHARE)
        Inspection.check_move(step_4, TC7, 4)
        Inspection.check_list_of_files(TC7)
        step_5 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_5, TC7, 5)
        Inspection.check_work_dir(TC7)
        Inspection.check_list_of_files(TC7)


