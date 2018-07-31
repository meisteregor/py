#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
from time import gmtime, strftime
from utils.shop import *
from utils.manager_functinon import *
from compatibility.enter import *
from utils.setup_empoyees import *
from utils.parse import *


def terminal():
    """
    Function that invokes terminal connection if login to system was successful. In real time it triggers
    creating DB files(sale_details.txt, sale_details_sum.txt, files of external_place dir) when <push> and <exit>
    buttons pressed. It also creates an instances of MenuItems when buttons of goods pressed to use recalculate methods
    to make correct records in DB files
    """
    if args.position == 'manager' and args.name + args.surname in Managers.list_of_managers:
        logging.info('{}: {} {} connected successfully'.format(args.position, args.name, args.surname))
        print("Hello, {} {}! Have a nice day".format(args.name, args.surname))
        print('Use <details> for monitoring salesmen or enter exit if your workday is over')
        while True:
            response = enter('> ')
            if response == 'details':

                manager_function()
                logging.debug('{} {} {} took an info via details command'.format(args.position, args.name, args.surname))

            elif response == 'exit':
                logging.info('{} {} {} closed terminal session'.format(args.position, args.name, args.surname))
                break
    elif args.position == 'salesman' and args.name + args.surname in Salesmen.list_of_salesmen:

        logging.info('{}: {} {} connected successfully!'.format(args.position, args.name, args.surname))
        print("Hello, {} {}! Have a nice day".format(args.name, args.surname))
        print('To see goods available use <menu> command')
        print('Enter goods in check one by be then enter <push> to sell them. Enter <exit> if your workday is over')

        response_list_to_filter = []  # Container of responses. Would be filtered if terminal takes smth not from Menu
        deal_list = []  # Container of MenuItems
        salesman_box = []  # Container of Checks
        while True:
            response = enter('> ')

            response_list_to_filter.append(response)
            if response == 'push':

                for _ in response_list_to_filter:
                    if _ == 'sugar':
                        deal_list.append(Sugar(args.name + args.surname))
                        print('A portion of sugar was added for {}'.format(SUGAR_COST_USD))
                    elif _ == 'cream':
                        deal_list.append(Cream(args.name + args.surname))
                        print('A portion of cream was added for {}'.format(CREAM_COST_USD))
                    elif _ == 'cinnamon':
                        deal_list.append(Cinnamon(args.name + args.surname))
                        print('A portion of cinnamon was added for {}'.format(CINNAMON_COST_USD))
                    elif _ == 'tea':
                        deal_list.append(Tea(args.name + args.surname))
                        print('A couple of tea was added for {}'.format(TEA_COST_USD))
                    elif _ == 'cappuccino':
                        deal_list.append(Cappuccino(args.name + args.surname))
                        print('A couple of cappuccino was added for {}'.format(CAPPUCCINO_COST_USD))
                    elif _ == 'latte':
                        deal_list.append(Latte(args.name + args.surname))
                        print('A couple of latte was added for {}'.format(LATTE_COST_USD))

                deal_tuple = tuple(
                    deal_list)  # Making tuple from list to give it as an argument to class Check constructor
                check = Check(args.name + args.surname, deal_tuple)  # Creating exemplar of class Check
                salesman_box.append(check)

                print('Check created for sum of {}'.format(check.check_price))  # Interactive info for Salesmen
                logging.info("Salesman {} made a deal on sum: {}".format(args.name + args.surname, check.check_price))

                # The 6th requirement of "The script should" doing dump on flight to make data reusable for next runs
                with open("sale_details.txt", "a") as f:
                    f.write(args.name + args.surname + ' ' + str(check.check_price) + '\n')

                # The 7th requirement of "The script should" and doing dumps on flight also
                # Create dir, change dir, drop <salesman>.txt files, return path, OS compatibility.
                if platform.system() == 'Windows':
                    if not os.path.exists(os.getcwd() + '\\external_place'):
                        os.makedirs(os.getcwd() + '\\external_place')
                    working_dir = os.getcwd()  # Need to return here after dumping
                    os.chdir(os.getcwd() + '\\external_place')
                    with open(args.name + args.surname + ".txt", "a") as f:
                        f.write(strftime("(%Y-%m-%d-%H:%M:%S)", gmtime()) + ' ' + str(check.check_price) + ' ' + str(
                            deal_tuple) + '\n')
                    os.chdir(working_dir)
                elif platform.system() == 'Linux':
                    if not os.path.exists(os.getcwd() + '/external_place'):
                        os.makedirs(os.getcwd() + '/external_place')
                    working_dir = os.getcwd()  # We need to remember current dir to return it later
                    os.chdir(os.getcwd() + '/external_place')
                    with open(args.name + args.surname + ".txt", "a") as f:
                        f.write(strftime("(%Y-%m-%d-%H:%M:%S)", gmtime()) + ' ' + str(check.check_price) + ' ' + str(
                            deal_tuple) + '\n')
                    os.chdir(working_dir)  # Return to a starting path
                else:
                    raise OSError('Your OS is not supported')
                response_list_to_filter = []  # Clearing not filtered list of responses to invoke it for new requests
                deal_list = []  # Also clearing filtered list

            elif response == 'exit':
                print('Goodbye, {}!'.format(args.name))
                logging.info('{} {} {} closed terminal session'.format(args.position, args.name, args.surname))
                box = CheckBox(salesman_box)  # Calling an instance of CheckBox to wrap Checks

                with open("sale_details_sum.txt", "a") as f:
                    f.write(args.name + args.surname + ' ' + str(box.check_box_length) + ' ' + str(box.check_box_price) + '\n')
                logging.info(
                    'Box belongs to {} with {} created and added to db'.format(args.name + args.surname, salesman_box))
                break

            elif response == 'menu':
                print('Today on sale: <cappuccino>, <latte>, <tea>, <sugar>, <cream>, <cinnamon>')
    else:
        raise UserWarning('NO ACCESS!')
