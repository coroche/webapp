import csv
import random

def reduce_list(remaining_words, greens, oranges, oranges_excl, elim):
	#Takes a list of remaining possible solutions and checks each one against current constraints to reduce the list

	#Checks that each word satisfies the green letters already found
	for i in range(5):
		remaining_words = [word for word in remaining_words if (greens[i]==word[i] or greens[i]=='_')]
	
	#Checks that each word contains orange letters already found but not in eliminated positions
	for i in range(len(oranges)):
		remaining_words = [word for word in remaining_words if oranges[i] in word and word.index(oranges[i]) not in oranges_excl[i]]
	
	#Checks that each word does not contain letters that have been eliminated
	for letter in elim:
		remaining_words = [word for word in remaining_words if letter not in word]
	
	return remaining_words

def validate_input(text, length, error_msg, validate_word, all_possible_words):
	#Runs validations on user input for guesses an results. Recursion is used for invalid inputs
	user_input = input(text).lower()
	if len(user_input) != length:
		print(error_msg)
		print()
		validate_input(text, length, error_msg, validate_word, all_possible_words)
	elif validate_word:
		if user_input not in all_possible_words:
			print('Enter a valid word')
			print()
			validate_input(text, length, error_msg, validate_word, all_possible_words)
	return list(user_input)

def returnWordList(guesses, results):
	#Reads csv file of all possible words as writes them to a list
	with open('./app/library/allowed_words.csv', 'r') as read_obj:
		csv_reader = csv.reader(read_obj)
		all_possible_words = list(csv_reader)[0]

	#The remaining_words list will be reduced. all_possible_words will be unchanged and used to validate guesses
	remaining_words = all_possible_words

	#Stores known letters in the corret position (green letters). '_' signifies that the letter is unknows for that position
	greens = ['_']*5

	#Stores a list of letters that are known to be in the solution but with an unknown position (orange letters)
	oranges = []
	#Stores positions that we know each orange letter doesn't go
	oranges_excl = []

	#Stores letters that are known not to be in the solution
	elim = []

	#When the solution is unknown
	for ind, guess in enumerate(guesses):
		result = results[ind]
		
		#Update lists with this result
		#Loop over the letters in guess
		for i in range(5):

			#if the result is green write it to the greens list in the correct position
			if result[i] == 'g':
				greens[i] = guess[i]

			#If the result is orange write the letter to the oranges list and its position to the exclusion list as we know the position is incorrect
			elif result[i] == 'o':
				if guess[i] not in oranges:
					oranges.append(guess[i])
					oranges_excl.append([i])
				else:
					j = oranges.index(guess[i])
					oranges_excl[j].append(i)
			
			#The letter is not in the solution. Write it to the elim list
			else:
				if guess[i] not in greens and guess[i] not in oranges:
					elim.append(guess[i])

		#Reduce the list of remaining possible solutions
		remaining_words = reduce_list(remaining_words, greens, oranges, oranges_excl, elim)

	return remaining_words