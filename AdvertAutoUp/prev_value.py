from add_first_counter import add_first_counter
from create_db import create_db


def prev_value(filename):
    try:
        with open(filename, "r") as f:
            extract_prev_value = f.readlines()
        return int(extract_prev_value[0])
    except IOError:
        create_db(filename)
        add_first_counter(filename)
    except IndexError:
        create_db(filename)
        add_first_counter(filename)

