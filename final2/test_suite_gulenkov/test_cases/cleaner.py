import subprocess
import test_cases.variables as var
import test_cases.constants as cons


class Cleaner(object):
    """Removing dirs and its content after TCs' run"""

    @staticmethod
    def clear_share_dir():
        command = subprocess.Popen(["ssh -T " + var.SERVER_NAME + '@' + var.SERVER_IP + ' ' + cons.REMOVE_ON_SERVER],
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            print >> command.stderr, "ERROR: %s" % error
        else:
            print(result)

    @staticmethod
    def remove_test_dir():
        subprocess.call([cons.REMOVE_TEST_DIR], shell=True)