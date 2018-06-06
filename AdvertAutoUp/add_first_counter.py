
def add_first_counter(name_of_file):
    with open(name_of_file, "a") as f:
        f.write("0")
