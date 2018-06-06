from up_add import up_add
from update_db import update_db
from constants import *

if __name__ == '__main__':
    update_db(FILE_NAME_IDLE)
    up_add()
