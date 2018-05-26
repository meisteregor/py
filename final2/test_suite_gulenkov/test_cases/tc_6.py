from test_cases import *


class TC6(UnixCommands):
    """From client side execute a file in a share directory. Condition: rw, sync"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def run_tc():
        TC6.logger.info(cons.INFO_EXECUTE + cons.INFO_CONDITION_RW)
        step_1 = UnixCommands.change_directory(var.LOCAL_PATH_TO_SHARE)
        Inspection.check_change_dir(step_1, TC6, 1)
        Inspection.check_work_dir(TC6)
        step_2 = UnixCommands.touch_file(cons.TEST_FILE_NAME)
        Inspection.check_touch_file(step_2, TC6, 2)
        Inspection.check_list_of_files(TC6)
        step_3 = UnixCommands.write_into_file(cons.TEST_FILE_NAME, cons.SCRIPT_DATA)
        Inspection.check_write_into_file(step_3, TC6, 3)
        Inspection.check_read_from_file(TC6, cons.TEST_FILE_NAME)
        step_4 = UnixCommands.run_script(cons.TEST_FILE_NAME)
        Inspection.check_run_script(step_4, TC6, 4)


