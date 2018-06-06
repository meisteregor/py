from count_new_value import count_new_value


def update_db(db_file):
    dump = str(count_new_value(db_file))
    with open(db_file, "w") as f:
        f.write(dump)
