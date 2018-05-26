from test_cases import *


class CustomLogger(UnixCommands):
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    file_handler = logging.FileHandler(var.PATH_TO_LOGGER + 'readable_output.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)