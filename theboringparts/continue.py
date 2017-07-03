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

def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))