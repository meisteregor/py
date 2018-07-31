#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from utils.constants import *


class CheckBox(object):
    """A bit abstracted class. Just perceive it as a casket for checks"""

    def __init__(self, box):
        self.box = box

    @property
    def check_box_price(self):
        return sum(_.check_price for _ in self.box)

    @property
    def check_box_length(self):
        return len(self.box)


class Check(object):
    """Checks that forms under each pressing on push button"""

    def __init__(self, whose, pack=None, *items):
        assert isinstance(whose, str)
        self.whose = whose
        if pack is None:
            pack = []
        self.pack = pack
        for each in items:
            assert issubclass(each, MenuItems)
            self.pack.append(each)

    @property
    def check_price(self):
        return sum(_.cost for _ in self.pack)


class Employees(object):
    """Formal empty class to inherit workers of CoffeeForMe"""
    pass


class Managers(Employees):
    """
    Managers, instantiate at the start of the main script after successful login parsing employees.txt
    Attribute .fullname is made for the agreement that there would not be full namesakes in a relatively
    small coffee shop. So, this bonding used as the unique identifier.
    """

    list_of_managers = []

    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.fullname = args[0] + args[1]  # super(Managers, self).__init__()
        Managers.list_of_managers.append(self.fullname)
        self.list_of_managers = Managers.list_of_managers.append(self.fullname)
        super(Managers, self).__init__()


class Salesmen(Employees):
    """Salesmen, instantiate at the start of the main script after successful login parsing employees.txt
    Attribute .fullname is made for the agreement that there would not be full namesakes in a relatively
    small coffee shop. So, this bonding used as the unique identifier."""
    list_of_salesmen = []

    def __init__(self, *salesman):
        self.salesman = salesman
        self.name = salesman[0]
        self.surname = salesman[1]
        self.fullname = salesman[0] + salesman[1]
        self.list_of_salesmen = Salesmen.list_of_salesmen.append(self.fullname)
        super(Salesmen, self).__init__()


class MenuItems(object):
    """Everything that we can sell in CoffeeForMe company"""

    def __init__(self, pack=None):
        if pack is None:
            pack = []
        self.pack = pack

    def add_items(self, *items):
        for item in items:
            self.pack.append(item)

    def remove_item(self, item):
        if item in self.pack:
            self.pack.remove(item)
            logging.info('item {} was successfully removed'.format(item))
        else:
            AttributeError("There is no such an item in pack")


class Goods(MenuItems):
    def __init__(self):
        super(Goods, self).__init__()

    def add_items(self, *items):
        for _ in items:
            if isinstance(_, Drinks) or isinstance(_, Additions):
                super(Goods, self).add_items(_)
                logging.warning('An item(s): {} was successfully added'.format(_))
            else:
                raise TypeError("Incorrect product assignment!")


class Drinks(Goods):
    pass


class Additions(Goods):
    pass


class Coffee(Drinks):
    pass


class Tea(Drinks):

    def __init__(self, posted_by, name='tea', cost=TEA_COST_USD):
        self.cost = cost
        self.name = name
        self.posted_by = posted_by
        super(Tea, self).__init__()


class Latte(Coffee):

    def __init__(self, posted_by, name='latte', cost=LATTE_COST_USD):
        self.cost = cost
        self.name = name
        self.posted_by = posted_by
        super(Latte, self).__init__()


class Cappuccino(Coffee):
    def __init__(self, posted_by, name='cappuccino', cost=CAPPUCCINO_COST_USD):
        self.cost = cost
        self.name = name
        self.posted_by = posted_by
        super(Cappuccino, self).__init__()


class Sugar(Additions):
    def __init__(self, posted_by, name='sugar', cost=SUGAR_COST_USD):
        self.cost = cost
        self.name = name
        self.posted_by = posted_by
        super(Sugar, self).__init__()


class Cream(Additions):
    def __init__(self, posted_by, name='cream', cost=CREAM_COST_USD):
        self.cost = cost
        self.name = name
        self.posted_by = posted_by
        super(Cream, self).__init__()


class Cinnamon(Additions):
    def __init__(self, posted_by, name='cinnamon', cost=CINNAMON_COST_USD):
        self.cost = cost
        self.name = name
        self.posted_by = posted_by
        super(Cinnamon, self).__init__()
