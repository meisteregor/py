from test_cases import variables as var

# Constants for temporary essences
TEST_FILE_NAME = 'file_for_test'
TEST_FILE_2_NAME = 'file_for_test_2'
TEST_DIR_NAME = 'dir_for_test'
SCRIPT_DATA = 'echo "vampires pretending to be humans pretending to be vampires"'

# Constants for preconditions
RED_HAT_FAMILY = 'CentOS Linux'
PATH_TO_TEST_DIR = var.PATH_TO_LOGGER
MAKEDIR = 'mkdir -p'
REMOTE_TOUCH = 'touch '
OUTER_SOURCE = 'tut.by'
PING_OUTER_SOURCE = 'ping -c 2 ' + OUTER_SOURCE
CHANGE_PRECONDITION_TO_RW = var.HOST_PATH_TO_SHARE + '       *(rw,sync,no_root_squash,no_all_squash)'
CHANGE_PRECONDITION_TO_RO = var.HOST_PATH_TO_SHARE + '       *(ro,sync,no_root_squash,no_all_squash)'
REMOTE_RERUN_NFS = 'exportfs -arv'
DIR_FOR_CONDITION = '/etc'
FILE_FOR_CONDITION = '/exports'
REMOVE_ON_SERVER = 'rm -f ' + var.HOST_PATH_TO_SHARE + '*'
REMOVE_TEST_DIR = 'rm -rf ' + PATH_TO_TEST_DIR + '/dir_for_test'
REMOTE_CHECK_DIR = MAKEDIR + ' ' + var.HOST_PATH_TO_SHARE

# Constants for logger
INFO_CHECKING_LOCAL_WEB_AVAILABILITY = 'checking local internet connection...'
INFO_CHECKING_REMOTE_WEB_AVAILABILITY = 'checking remote internet connection...'
INFO_CHECKING_HOST_AVAILABILITY = 'checking host availability...'
DEBUG_CONNECTION_STAGE = '=============== CONNECTION STAGE ==============='
DEBUG_SETTING_NFS_STAGE = '=============== NFS SETUP STAGE ==============='
DEBUG_START_TEST_STAGE = '================== TEST STAGE =================='
DEBUG_GENERATING_KEYS = 'Keys for SSH generated!'
DEBUG_DROP_KEYS = 'Keys for SSH added to the machines!'
INFO_PASSWORLESS_SSH_DONE = 'Setting passwordless SSH: *DONE'
DEBUG_PARAMIKO_IMPORTED = 'paramiko module has been imported successfully\n'
WARN_PARAMIKO_NOT_FOUND = 'paramiko module not found. Trying to install...'
INFO_PARAMIKO_INSTALLED = 'paramiko module has been installed successfully\n'
INFO_CONDITION_RO = 'Read-only config has been set *(ro, sync)'
INFO_CONDITION_RW = 'Read-write config has been set *(rw, sync)'
INFO_CREATE = 'Create a file in a share directory. '
INFO_RENAME = 'Rename a file from a share directory. '
INFO_REMOVE = 'Remove a file from a share directory. '
INFO_COPY = 'Copy a file to a share directory. '
INFO_MOVE = 'Move a file into a share directory. '
INFO_EXECUTE = 'Execute a file from a share directory. '
INFO_WRITE_DATA = 'Write data into a file from a share directory. '
