#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.logger import *
from utils.shop import Managers
from utils.shop import Salesmen
from compatibility.gen import *
from utils.read_employees import *


def setup_employees():
    """"
    Reading from employees.txt to invoke an instances of Salesmen & Managers class.
    File has its own exact structure, so its called and elements assigned by its positions
    """
    setup_list = read_employees()

    for _ in gen(len(setup_list)):
        if setup_list[_].split()[2] == 'manager':
            _ = Managers(setup_list[_].split()[0], setup_list[_].split()[1], setup_list[_].split()[2])
            logging.info('An instance of Managers called {} created'.format(_.fullname))
        elif setup_list[_].split()[2] == 'salesman':
            _ = Salesmen(setup_list[_].split()[0], setup_list[_].split()[1], setup_list[_].split()[2])
            logging.info('An instance of Salesmen called {} created'.format(_.fullname))
        else:
            raise AssertionError("Incorrect file format, look README.txt for details")
