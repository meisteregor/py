from test_cases import *


class TC1(UnixCommands):
    """From client side create a file in a share directory. Condition: rw"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC1.logger.debug(cons.DEBUG_START_TEST_STAGE)
        TC1.logger.info(cons.INFO_CREATE + cons.INFO_CONDITION_RW)
        step_1 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_1, TC1, 1)
        Inspection.check_work_dir(TC1)
        step_2 = UnixCommands.touch_file(cons.TEST_FILE_NAME)
        Inspection.check_touch_file(step_2, TC1, 2)
        step_3 = UnixCommands.cat_file(cons.TEST_FILE_NAME)
        Inspection.check_cat_file(step_3, TC1, 3)
        Inspection.check_list_of_files(TC1)

