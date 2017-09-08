#! /usr/bin/env python3

#### Continue statement ####
# while True:
# 	print('Who are you?')
# 	name = input()
# 	if name != 'Joe':
# 		continue
# 	print('Hello, Joe. What is the password? (it is a fish)')
# 	password = input()
# 	if password == 'swordfish':
# 		break
# print('Access granted')


# #### false datatype
# name = ''
# while not name:
# 	print('Enter your name:')
# 	name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
# 	print('Be sure to have enough room for all')
# print('DOne')


# # for in range
# print('My name is')
# for i in range(5):
# 	print('Jimmy five times (' + str(i) + ')')


# # Flexible for in range
# for i in range(5, -1, -1):
# 	print(i)


# Module Importing
# # import random 
# from random import * # doesnt require the random prefix
# for i in range(5):
# 	print(randint(1, 103))


# Exiting
# import sys

# while True:
# 	print('Type exit to exit')
# 	response = input()
# 	if response == 'exit':
# 		sys.exit()
# 	print('You typed ' + response + '.')


# # practice
# print('Spam?')
# spam = int(input())
# if spam == 1:
# 	print('Hello')
# elif spam == 2:
# 	print('Howdy')
# else:
# 	print('Greetings!')


#practice 2
# for i in range(1, 11):
# 	print(i)

# i = 1
# while i <= 10:
# 	print(i)
# 	i = i + 1


# functions
# def hello():
# 	print('Howdy')
# 	print('Howdy!!!')
# 	print('Hello there')

# hello()


# passing params
# def hello(name):
# 	print('Hello ' + name)

# hello('Alice')
# hello('Bob')


# # return keyword
# import random
# def getAnswer(answerNumber):
# 	if answerNumber == 1:
# 		return 'It is certain'
# 	elif answerNumber == 2:
# 		return 'It is decidedly so'
# 	elif answerNumber == 3:
# 		return 'Yes'
# 	elif answerNumber == 4:
# 		return 'Reply hazy try again'
# 	elif answerNumber == 5:
# 		return 'Ask later'
# 	elif answerNumber == 6:
# 		return 'Concentrate and ask again'
# 	elif answerNumber == 7:
# 		return 'My reply is no'
# 	elif answerNumber == 8:
# 		return 'Outlook not so good'
# 	elif answerNumber == 9:
# 		return 'Very doubtful'

# # r = random.randint(1, 9)
# # fortune = getAnswer(r)
# # print(fortune)

# print(getAnswer(random.randint(1, 9)))

# spam = print('Hello!')
# print(None == spam)

# # print nonewline
# print('40', end='.00 ')
# print('World')

# foo = 'bar'
# print('cats', 'dogs', 'mice', sep=foo)


# # Global & local variables
# def spam():
# 	eggs = 31337
# spam()
# print(eggs)

# def spam():
# 	eggs = 99
# 	bacon()
# 	print(bacon())

# def bacon():
# 	ham = 101
# 	eggs = 2
# 	return eggs

# spam()

# def spam():
# 	print(eggs)
# eggs = 42
# spam()
# print(eggs)

# def spam():
# 	eggs = 'spam local'
# 	print(eggs)

# def bacon():
# 	eggs = 'bacon local'
# 	print(eggs)
# 	spam()
# 	print(eggs)

# eggs = 'global'
# bacon()
# print(eggs)

# def spam():
# 	global eggs
# 	eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)

# def spam():
# 	global eggs
# 	eggs = 'spam'
# def ham():
# 	print(eggs)

# eggs = 42
# spam()
# print(eggs)

# def spam():
# 	print(eggs)
# 	eggs = 'spam local'

# eggs = 'global'
# spam()


# Exception handling
# def spam(divideBy):
# 	return 42 / divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# def spam(divideBy):
# 	try:
# 		return 42 / divideBy
# 	except ZeroDivisionError:
# 		print('Error: Invalid argument.')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# def spam(divideBy):
# 	return 42 / divideBy

# try:
# 	print(spam(2))
# 	print(spam(12))
# 	print(spam(0))
# 	print(spam(1))
# except ZeroDivisionError:
# 	print('Error: Invalid argument.')

# # Guessing Game
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

# for guessesTaken in range(1, 7):
# 	print('Take a guess.')
# 	guess = int(input())

# 	if guess < secretNumber:
# 		print('Your guess is too low.')
# 	elif guess > secretNumber:
# 		print('Your guess is too high')
# 	else:
# 		break

# if guess == secretNumber:
# 	print('Good job! You guessed my number in ' + str(guessesTaken))


# ## LISTS
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam[0] = 'dog'
# spam = spam + ['ye', 'nay', 'hay'] * 3
# del spam[1]
# del spam[-1]
# print(spam[0:])
# print(len(spam))


# catNames = []
# while True:
# 	print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
# 	name = input()
# 	if name == '':
# 		break
# 	catNames = catNames + [name] # list concatenation
# print('The cat names are:')
# for name in catNames:
# 	print(' ' + name)


# for i in range(4):
# 	print(i)

# for i in [0, 1, 2, 3]:
# 	print(i)

# supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for i in range(len(supplies)):
# 	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# spam = ['hello', 'hi', 'howdy', 'heyas']
# if 'h3' not in spam:
# 	print('yes')
# else:
# 	print('no')


# myPets = ['Jinxey', 'Jack', 'Dolly']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
# 	print('I do not have a pet named ' + name)
# else:
# 	print(name + ' is my pet.')


# cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# cat = ['fat', 'orange', 'loud']
# size, color, disposition = cat
# print(size)
# print(color)
# print(disposition)

# a, b = 'Alice', 'Bob'
# a, b = b, a
# print(a)
# print(b)

# spam = ['hello', 'hi', 'howdy', 'heyas']
# spam.append('Moose')
# spam.insert(2, 'chicken')
# spam.append('Zebra')
# spam.append('zebra')
# spam.append('apple')
# spam.remove('hi')
# # spam.sort()
# #spam.sort(reverse=True)
# spam.sort(key=str.lower)
# print(spam)
#print(spam.index('hello')) #index method


# import random

# messages = ['It is certain',
# 			'It is decidedly so',
# 			'Yes definitely',
# 			'My reply is no',
# 			'Outlook not so good',
# 			'Very doubtful']

# # print('How do you feel about the future of the planet?')
# while True:
# 	yourAnswer = input('Do you think the worlds going to end soon? ')
# 	if yourAnswer in messages:
# 		print('Probably right.')
# 		break
# 	else:
# 		print('Yeah, ' + messages[random.randint(0, len(messages) - 1)] + '.')
# 		messages.append(yourAnswer)
# #print(messages[random.randint(0, len(messages) - 1)])

# name = 'Brandon'
# for i in name:
# 	print(i, sep="", end=".")

# for i in range(1, 5):
# 	print(i, end="")

# for i in name:
# 	print('* * *' + i + '* * *')
# print(name[0])
# print(name[-2])
# print(name[0:4])
# print('Zo' in name)
# print('p' not in name)


# name = 'Zophie a cat'
# newName = name[0:7] + 'the' + name[8:12]
# print(name)
# print(newName)


# var = type(('hello',))
# print(var)

# var = tuple(['cat', 'dog', 5])
# print(var)

# var = list(('cat', 'dog', 5))
# print(var)

# var = list('hello')
# print(var)

# spam = 42
# cheese = spam
# spam = 100
# print(spam)
# print(cheese)


# import copy
# spam = ['A', 'B', 'C', ['D', 'No']]
# cheese = copy.deepcopy(spam)
# cheese[1] = 42
# print(spam)
# print(cheese)

# def listContents(list):
# 	listSize = len(list)
# 	printedList = ''
# 	for i in list:
# 		if i == list[listSize - 1]:
# 			printedList = printedList + 'and ' + i
# 		else:
# 			printedList = printedList + i + ', '
# 	return printedList

# spam = ['apples', 'bananas', 'tofu', 'cats']
# listed = listContents(spam)
# print(listed)

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]


# for i in range(0, 6):
# 	for j in range(0,9):
# 		print(grid[j][i], end="")
# 	print('')


# myCat = {'size': 'fat', 'color':'gray', 'disposition': 'loud'}
# print(myCat['size'])
# print('My cat has ' + myCat['color'] + ' fur')


# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# print(spam == bacon)

# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(eggs == ham)

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
# 	print('Enter a name: (blank to quit)')
# 	name = input()
# 	if name == '':
# 		break

# 	if name in birthdays:
# 		print(birthdays[name] + ' is the birthday of ' + name)
# 	else:
# 		print('I do not have birthday information for ' + name)
# 		print('What is their birthday?')
# 		bday = input()
# 		birthdays[name] = bday
# 		print('Birthday database updated.')


# spam = {'color': 'red', 'age': 42}
# # for v in spam.values():
# # 	print(v)
# # for k in spam.keys():
# # 	print(k)
# # for i in spam.items():
# # 	print(i)
# # print(spam.keys())
# # print(list(spam.keys()))
# for k, v in spam.items():
# 	print('Key: ' + k + ' Value: ' + str(v))


# spam = {'name': 'Zophie', 'age': 7}
# # print('name' in spam.keys())
# # print('Zophie' in spam.values())
# # print('color' in spam.keys())
# # print('color' not in spam.keys())
# # print('color' in spam)
# # print('Zophie' in spam)


# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 'no')) + ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs', 'no')) + ' eggs')


# spam = {'name': 'Pooka', 'age': 5}
# sd = spam.setdefault('color', 'black')
# print(sd)
# print(spam)
# sd = spam.setdefault('color', 'white')
# print(sd)

# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
# 	count.setdefault(character, 0)
# 	count[character] = count[character] + 1
# print(count.values())


# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# count = {}
# for character in message:
# 	count.setdefault(character, 0)
# 	count[character] = count[character] + 1
	
# #pprint.pprint(count)
# print(pprint.pformat(count))


# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X'
# for i in range(9):
# 	printBoard(theBoard)
# 	print('Turn for ' + turn + '. Move on which space?')
# 	move = input()
# 	theBoard[move] = turn
# 	if turn == 'X':
# 		turn = 'O'
# 	else:
# 		turn = 'X'
# printBoard(theBoard)


# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
# 			 'Bob': {'ham sandwiches': 3, 'apples': 2},
# 			 'Carol': {'cups': 3, 'apple pies': 1}}

# def totalBrought(guests, item):
# 	numBrought = 0
# 	for k, v in guests.items():
# 		numBrought = numBrought + v.get(item, 9)
# 	return numBrought

# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))


"""inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
	total = 0
	for i, n in inventory.items():
		total = total + n
		amount = str(n)
		thing = i
		print(amount + ' ' + thing)
	return total

print('Total number of items: ' + str(displayInventory(inventory)))
"""

# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
# 	print('I feel great too.')
# else:
# 	print('I hope the rest of your day is good.')


# while True:
# 	print('Enter your age:')
# 	age = input()
# 	if age.isdecimal():
# 		break
# 	print('Please enter a number for your age.')

# while True:
# 	print('Select a new password (letters and numbers only):')
# 	password = input()
# 	if password.isalnum():
# 		break
# 	print('Passwords can only have letters and numbers.')


# # splicer = ', '
# splicer = ' $ '
# wordList = ['Kava', 'Kratom', 'Coffee', 'Soda']
# text = splicer.join(wordList)
# print(text)

# text = text.split(' $ ')
# # print(text)

# def printPicnic(itemsDict, leftWidth, rightWidth):
# 	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
# 	for k, v in itemsDict.items():
# 		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)


# def makeTable(title, items):
# 	centerLength = len(title) * 2
# 	# if length is an odd number add 1
# 	if centerLength % 2 != 0:
# 		centerLength = centerLength + 1

# 	finalTable = title.center(centerLength, '-')
# 	finalTable = finalTable + '\n'
# 	for i, v in items.items():
# 		finalTable = finalTable + i.ljust(centerLength, '.') + str(v).rjust(centerLength, ' ') + '\n'
# 	return finalTable
	
# title = 'Bula'
# items = {'Kava': 4, 'Kratom': 12, 'Coffee': 2}
# table = makeTable(title, items)
# print(table)


# spam = '	Hello World 	'
# # spam = spam.strip()
# # spam = spam.lstrip()
# spam.rstrip()
# print(spam)

# spam = 'SpamSpamBaconSpamEggsSpamSpam'
# spam = spam.strip('SpamSpamBaconSpam')
# print(spam)

import pyperclip
# pyperclip.copy('Hello world!')
pasted = pyperclip.paste()
print(pasted)
