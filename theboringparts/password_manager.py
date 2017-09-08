#! /usr/bin/env python3
#password_manager.py - An insecure password locker program.

PASSWORDS = {'email': 'sfsodjf0w3jrefowi',
			 'blog': 'owijesf092uwj039ei',
			 'luggage': '32423'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python password_manager.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)

