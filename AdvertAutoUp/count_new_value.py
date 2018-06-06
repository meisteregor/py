from prev_value import prev_value


def count_new_value(filename):
    if prev_value(filename):
        new_value = prev_value(filename) + 1
    else:
        new_value = 1
    return new_value


