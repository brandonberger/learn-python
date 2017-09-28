 #! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: python3 mcb.pyw save <keyword> - Saves Clipboard to keyword.
#		 python3 mcb.pyw <keyword> - Loads keyword to clipboard.
#		 python3 mcb.pyw list - loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save Clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	if sys.argv[2] == 'all':
		for i in mcbShelf:
			del mcbShelf[i]
	else:
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# List Keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()