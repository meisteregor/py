#!/usr/bin/env python
# -*- coding: utf-8 -*-
# also not implemented part as it touches install_db.py
# pass it through...

import pysqlite
import mysql.connector

config = {
  'user': 'user',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'sale_details',
  'raise_on_warnings': True,
  'use_pure': False,
}

cnx = mysql.connector.connect(**config)

cnx.close()
