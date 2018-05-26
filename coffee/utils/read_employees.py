#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_employees():
    with open("employees.txt", "r") as f:
        setup_list = list(f)
    return setup_list
