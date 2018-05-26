UTILITY PURPOSE:
Setting up & Testing of NFSv4 with 2 linux-based machines.

REQUIREMENTS:
Both of the machines need:
1. Network:
- succesfull ping each other and outer sources
2. openSSH service installed
*Debian Family Lunix it may not have "PermitRootLogin yes" in /etc/ssh/sshd_config. Uncomment it. ([>> /etc/init.d/ssh restart] or reboot after)

USAGE OF THE UTILITY:
1. Turn on 2 lunux-based machines.
2. Login as root on client.
3. Move test_suit_gulenkov package to client.
4. Input existing variables in ../test_suite_gulenkov/test_cases/variables.py: host, ip address, path for logger.
5. Run main.py with python2 or python3
6. See readable_output.log to get full info about testing application run

