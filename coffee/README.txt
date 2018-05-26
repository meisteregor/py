UTILITY PURPOSE:

I tried to implemented something like terminals in KFC. All you need at your workplace is to press colorful
buttons and check out your clients' menu orders. Unfortunately, instead of buttons we will simply use key words which are
instances of MenuItems. After adding it one by one (imagine your finger clicking) you have to check out visitors
by pressing keyword "push".


USAGE OF THE UTILITY:

1. First of all you need to employ workers for "CoffeeForMe" company.
Do initialization of employees to your coffee shop in form "name surname position" for each worker from a new line in
employees.txt. This file already contains some examples for test run of the application.

2. Run coffee.py in console with arguments name surname position of the workers you have just set.
use -h --help for help. After authorization complete successfully, you can start using it as a terminal session.

3. If you are manager you have the only option "details": look for your salesmen statistics.
If you are salesman you have the option: sale goods by inputting menu titles, that would trigger instances of foods,
refreshment of DB's files on flight


PACKAGE INFO:

- coffee.py: main module to run the utility
- shop.py: Objects of the coffee shop
- manager_function.py: data parser for output info
- constants.py: Set prices for goods
- logger.py: Logger setups
- log.log: Details of project runs
- sale_details.txt: After run script created database registering each check out
- sale_details_sum.txt: After run script created database registering each salesman deals summary
- tests dir: Tests of the most important functions
- compatibility dir: Folder with OS & python versions compatibility snippets.
- external_place dir: After run script created folder to dump detailed info about every action of each salesman
- README.txt: Tutorial


SALESMAN BUTTONS:
latte
tea
sugar
cream
cappuccino
cinnamon
-----
push
-----
exit

MANAGER BUTTONS:
details
exit


TIPS:
- Try to avoid running script from outer dirs.
- Use this in its logical sequence: first hire workers, login, produce some work selling goods, turn to details.


GOOD LUCK! HAVE A NICE EXPERIENCE!