#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
	# Create the quiz and answer key files

	# Creates the quiz file, adds incremented number to the end, write privelges
	quizFile = io.open('quizFiles/capitalsQuiz%s.txt' % (quizNum + 1), 'w')

	# Creates the quiz answers file, add incremented number to end of file name, write privledges
	answerKeyFile = io.open('quizFiles/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

	# Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')

	# Writes the name of the quiz 20 spaces indented adds incrememnted number
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	# Shuffle the order of the states.

	# Creates list of States from capitals keys
	states = list(capitals.keys())

	# Shuffles the list of capital keys (state)
	random.shuffle(states)

	# Loop through all 50 states, making a question for each.
	for questionNum in range(50):
		# Get right and wrong answers.

		# Assigns Correct Answer to correct position in dict
		correctAnswer = capitals[states[questionNum]]

		# Create list of wrong answers from all values
		wrongAnswers = list(capitals.values())

		# Deletes the correct answer from the collective list of all vals
		del wrongAnswers[wrongAnswers.index(correctAnswer)]

		# Assigns wrong answer choices per question to 3 random values from the wrongAnswer list
		wrongAnswers = random.sample(wrongAnswers, 3)

		# Concats the wrong answer options with the correct answer to create the options for the question 
		answerOptions = wrongAnswers + [correctAnswer]

		# Shuffle the options
		random.shuffle(answerOptions)

		# Write the question and the answer options to the quiz file.
		quizFile.write('%s. What is the capital of %s\n' % (questionNum + 1, states[questionNum]))

		# Loops through all question options
		for i in range(4):
			# Writes the options to the file
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		# Write the answer key to a file.
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()
