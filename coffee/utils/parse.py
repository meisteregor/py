#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description="Greetings from CoffeeForMe company!")
parser.add_argument("name", help="first name")
parser.add_argument("surname", help="second name")
parser.add_argument("position", help="manager or salesman")
args = parser.parse_args()