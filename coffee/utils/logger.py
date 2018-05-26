#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger()
logfile = "log.log"
formatter = logging.Formatter('%(asctime)s - %(name)s : - %(levelname)s - %(message)s')

screen_handler = logging.StreamHandler()
screen_handler.setLevel(logging.WARNING)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
