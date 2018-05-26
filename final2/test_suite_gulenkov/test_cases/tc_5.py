from test_cases import *


class TC5(UnixCommands):
    """From a test directory on client side move a file into a share directory. Condition: rw"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC5.logger.info(cons.INFO_MOVE + cons.INFO_CONDITION_RW)
        step_1 = UnixCommands.make_dir(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Inspection.check_make_dir(step_1, TC5, 1)
        step_2 = UnixCommands.change_directory(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Inspection.check_change_dir(step_2, TC5, 2)
        Inspection.check_work_dir(TC5)
        step_3 = UnixCommands.touch_file(cons.TEST_FILE_NAME)
        Inspection.check_touch_file(step_3, TC5, 3)
        step_4 = UnixCommands.move_file(cons.TEST_FILE_NAME, var.LOCAL_PATH_TO_SHARE)
        Inspection.check_move(step_4, TC5, 4)
        Inspection.check_list_of_files(TC5)
        step_5 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_5, TC5, 5)
        Inspection.check_work_dir(TC5)
        Inspection.check_list_of_files(TC5)
