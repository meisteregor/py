#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from utils.read_employees import *
from compatibility.gen import *


class TestReadEmployees(unittest.TestCase):

    def test_not_empty_file(self):
        """test employees.txt is not empty"""
        res = read_employees()
        self.assertTrue(res)

    def test_3_element_in_line(self):
        """test line has exactly 3 elements"""
        for lines in read_employees():
            res = lines.split()
            self.assertEqual(len(res), 3)

    def test_position_symbol_limit(self):
        """test position not reaches more than 7 symbols"""
        for _ in gen(len(read_employees())):
            res = read_employees()[_].split()[2]
            self.assertLessEqual(len(res), 8)

    def test_position_exists(self):
        """test position exists"""
        for _ in gen(len(read_employees())):
            res = read_employees()[_].split()[2]
            self.assertTrue(res)

    def test_name_exists(self):
        """test position exists"""
        for _ in gen(len(read_employees())):
            res = read_employees()[_].split()[0]
            self.assertTrue(res)

    def test_surname_exists(self):
        """test position exists"""
        for _ in gen(len(read_employees())):
            res = read_employees()[_].split()[1]
            self.assertTrue(res)