#!/usr/bin/env python
# -*- coding: utf-8 -*-
from compatibility.gen import *


def manager_function():
    """
    This function parses two dynamically creating txt files which are something like database for our program.

    """
    list_to_total = []
    list_to_total_float = []

    with open("sale_details_sum.txt", "r") as f:
        sale_details_sum = f.readlines()

    with open("sale_details.txt", "r") as f:
        sale_details = list(f)

    # Gather each 2nd element of file which is cost of 1 check of 1 sale operation. Its len - ammount of deals,
    #  its sum - sales total
    for _ in gen(len(sale_details)):
        list_to_total.append(sale_details[_].split()[1])

    # Making it floats to count sum
    for _ in list_to_total:
        list_to_total_float.append(float(_))

    print('Seller name | Number of sales | Total Value ($)')

    for _ in gen(len(sale_details_sum)):
        print('{} | {} | {}'.format(sale_details_sum[_].split()[0], sale_details_sum[_].split()[1],
                                    sale_details_sum[_].split()[2]))

    print("TOTAL: | {} | {} ".format(len(sale_details), sum(list_to_total_float)))
