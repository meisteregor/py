#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
import sys
import logging

logger = logging.getLogger(__name__)
logfile = "script_log.log"
span_time = 2
run_tracker = []

formatter = logging.Formatter('%(asctime)s - %(name)s : %(threadName)s - %(levelname)s - %(message)s')
screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.DEBUG)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

start_time = time.time()


# MODIFY-START if needed

# MODIFY-END if needed

def threaded_execution(func_to_thread):
    # MODIFY-START
    # TODO: here be your code that runs a decorated function in a separate thread

    def wrapped(*args_, **kwargs_):
        # # raise NotImplementedError("Change me")
        t = threading.Thread(target=func_to_thread, args=args_, kwargs=kwargs_)
        t.start()

    return wrapped
    # MODIFY-END


@threaded_execution
def long_long_function(filename):
    logger.info("Filename to work with: {}".format(filename))
    run_tracker.append(filename)
    time.sleep(span_time)
    # TODO: here be your code that works on file content:
    # MODIFY-START
    with open(filename, "r") as f:
        list_of_strings = list(f)

    with open("truncated_" + filename, 'w') as f:
        for _ in list_of_strings[-10::]:
            f.write(_)
    # MODIFY-END


if __name__ == "__main__":
    logger.info("Starting a chain of long functions")
    long_long_function("input_file1.txt")
    long_long_function("input_file2.txt")

    logger.info("Starting long main logic")
    time.sleep(span_time)

    ########################
    # --- Summary part --- #
    ########################
    total_time = time.time() - start_time
    logger.info("The run took '{:.3}' seconds".format(total_time))
    assert len(run_tracker)  # Do NOT remove or change, we need to ensure long_long_function ever ran
    assert total_time < (span_time + 1)  # +1 second is granted for all the threads to get allocated

    # MODIFY-START if needed
    # MODIFY-END if needed
