#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


# testing func from ssh task
def take_connection_info():
    with open("machines.txt", "r") as f:
        list_of_machines = list(f)
    return list_of_machines


class MyListTest(unittest.TestCase):
    # test machines.txt is not empty
    def test_not_empty_file(self):
        res = take_connection_info()
        self.assertTrue(res)

    # test each line is a string
    def test_lines_are_str(self):
        for _ in take_connection_info():
            res = _
            self.assertIsInstance(res, str)

    # test each line has exactly 3 elements
    def test_3_element_in_line(self):
        for lines in take_connection_info():
            res = lines.split()
            self.assertEqual(len(res), 3)

    # test ip address symbol limit
    def test_ip_symbol_limit(self):
        for _ in xrange(len(take_connection_info())):
            res = take_connection_info()[_].split()[0]
            self.assertLessEqual(len(res), 15)

    # test login symbol limit
    def test_login_symbol_limit(self):
        for _ in xrange(len(take_connection_info())):
            res = take_connection_info()[_].split()[1]
            self.assertLessEqual(len(res), 256)

    def test_password_symbol_limit(self):
        for _ in xrange(len(take_connection_info())):
            res = take_connection_info()[_].split()[2]
            self.assertLessEqual(len(res), 256)

    # using regexp for test ip address matches ip form
    def test_ip_format_match(self):
        for _ in xrange(len(take_connection_info())):
            res = take_connection_info()[_].split()[0]
            self.assertRegexpMatches(res, r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


if __name__ == '__main__':
    unittest.main()
