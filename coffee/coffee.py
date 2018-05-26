#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.terminal import *
from utils.setup_empoyees import *


def main():
    try:
        setup_employees()
        logging.debug('trying to connect with: {} {} {}'.format(args.name, args.surname, args.position))
    except AssertionError:
        logging.critical(
            '{} {} {} DO NOT MATCHES WITH PRE SETTINGS in employees.txt'.format(args.name, args.surname, args.position))
    try:
        terminal()
    except UserWarning:
        logging.warning('access denied to {} {} {}'.format(args.name, args.surname, args.position))


if __name__ == '__main__':
    main()
