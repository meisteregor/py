#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Here is an error only, screenshots of installs attached, do not count this module
#  I just left it in archive to solve it later after resolving hard disk space problems.
import os

try:
    import pysqlite
except ImportError:
    os.system("pip install pysqlite")

try:
    import mysql.connector
except ImportError:
    os.system("pip install mysql")