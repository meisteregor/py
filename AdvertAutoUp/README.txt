UTILITY PURPOSE:
- Automation of everyday rising of the adverts into customers rooms on sites

UTILITY USAGE:
- instanciate ../dist/aau.exe via PowerShell: >pyinstaller -w -F -i "path_to_shotcut" aau.py
- Place your login and site data into AdvertAutoUp/constants.py
- Crate aau.exe shortcut from AdvertAutoUp/dist/ and place it into C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
to make it run on each start of the system
- Also add aau.exe into the Windows Scheduler and choose a preferable time for the execution

REQUIREMENTS:
- Win10
- Python2\3
- Google Chrome Browser
- Selenium Chrome Driver nearby aau.exe(included by default)

NOTES:
- As an addition utility also starts 2 DB files to track some stats:
    1) times_i_did_it.txt: for tracking successful ups
    2) times_master_called_me.txt: each run of the utility
- This utility can be distributed in the form where all the execution runs in the shadow mode to aviod interrupiton of your working processes.
