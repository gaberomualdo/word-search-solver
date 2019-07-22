# example word search to solve
example_to_solve = [['x', 'k', 'i', 'z', 'f', 'm', 'a', 'b', 'h', 'i', 's', 'x', 'c', 'e', 'r', 'y'], ['d', 'k', 'v', 'm', 'b', 'f', 'w', 'n', 'h', 's', 'k', 'p', 'n', 'u', 'f', 'q'], ['h', 'v', 't', 'c', 'q', 'v', 'i', 'l', 'e', 'v', 'f', 'r', 'd', 'l', 'q', 'd'], ['k', 'p', 'o', 'o', 'g', 'r', 'c', 'f', 'a', 'd', 'd', 't', 'k', 's', 'e', 'h'], ['k', 'o', 's', 'x', 'h', 'b', 'n', 'o', 's', 'r', 'e', 'f', 'f', 'e', 'j', 'h'], ['d', 'k', 'w', 'o', 'f', 'e', 's', 'd', 'n', 'k', 'o', 'i', 'p', 'k', 'l', 'x'], ['q', 'g', 'a', 'o', 's', 't', 'm', 'q', 'i', 'l', 't', 'l', 'g', 'u', 'p', 'q'], ['b', 'x', 's', 'w', 'd', 'u', 'y', 'v', 'e', 'a', 'o', 'u', 's', 'p', 'u', 'b'], ['n', 'c', 'h', 'k', 'd', 'x', 'b', 'a', 's', 's', 'r', 'c', 'e', 'q', 'm', 'j'], ['r', 'r', 'i', 'p', 'c', 'r', 'b', 'u', 's', 'h', 'p', 'l', 'n', 'g', 'n', 'l'], ['a', 'q', 'n', 'f', 'e', 'm', 'h', 'r', 'g', 't', 'p', 'm', 'u', 'i', 'q', 'c'], ['l', 'h', 'g', 'e', 'z', 'p', 'l', 'o', 'j', 'v', 'p', 'x', 'e', 't', 'l', 's'], ['b', 'i', 't', 's', 'h', 'z', 'd', 'h', 'q', 'w', 'u', 'z', 'k', 'z', 'q', 't'], ['p', 'y', 'o', 'j', 'm', 'e', 'k', 'j', 'm', 'l', 'm', 'w', 'p', 'a', 'd', 'j'], ['u', 'a', 'n', 't', 'r', 't', 'l', 'i', 'c', 'l', 'i', 'n', 't', 'o', 'n', 'y'], ['d', 'q', 'g', 'd', 'e', 'o', 's', 'w', 'z', 'r', 'f', 'b', 'p', 'p', 'q', 'a']]

# solve word search function
def solve_word_search(word_search, words):
	# convert word search from 2D array of letters to array of strings with letters joined together as a row (function)
	def convertToStringArray(local_word_search, joinString = ""):
		# loop through word search and join each letter in each row with an empty string (unless otherwise specified in function argument) to create string row
		for row_index in range(len(local_word_search)):
			local_word_search[row_index] = joinString.join(local_word_search[row_index])
		
		# return resulting 1D array of strings
		return local_word_search
	
	# convert array of strings to 2D array (function)
	def convertTo2DArray(local_word_search):
		# map each string in the array to an array of letters
		return map(list, local_word_search)

	# find words horizontally within word search (function)
	def findWordHorizontally(local_word_search, word):
		# variable for whether word was found
		word_found = False

		# loop through rows and search for word within string, and replace word with all caps version
		for row_index in range(len(local_word_search)):
			# replace word with all caps word (if found)
			local_word_search[row_index] = local_word_search[row_index].replace(word, word.upper())

			# try reverse as well
			local_word_search[row_index] = local_word_search[row_index].replace(word[::-1], word[::-1].upper())

			# if word was found and replaced, break for loop
			try:
				local_word_search[row_index].index(word)
				word_found = True
				break
			except:
				pass
			
			try:
				local_word_search[row_index].index(word[::-1])
				word_found = True
				break
			except:
				pass
		
		# return word search with word in all caps
		if(word_found == True):
			return local_word_search
		else:
			return False

	# rotate array 90 degrees (function)
	def rotateArray(local_array):
		# this neat one liner rotates any 2D array clockwise
		return list(map(list, zip(*local_array[::-1])))

	# rotate array counterclockwise 90 degrees (function)
	def rotateArrayCounterClockwise(local_array):
		# rotate array clockwise 3 times to simulate counterclockwise turn
		for i in range(3):
			local_array = rotateArray(local_array)

		# return rotated array
		return local_array

	# list of words found
	words_found = [False]*(len(words))

	# loop through each word and find
	for wordlist_index in range(len(words)):
		# variable for word
		word = words[wordlist_index]
		
		# find horizontal occurences

		# first, convert to string array
		word_search = convertToStringArray(word_search)

		# replace word with all caps version in word search

		# variable for word search with word found
		local_word_search_found_word = findWordHorizontally(word_search, word)

		# if word was found, replace word search with word search with word highlighted
		if(local_word_search_found_word != False):
			word_search = local_word_search_found_word
			continue
		
		# delete useless variable
		del local_word_search_found_word
		
		# revert back to 2d array
		word_search = convertTo2DArray(word_search)

		# find vertical occurences

		# first, rotate word search
		word_search = rotateArray(word_search)

		# convert to string array
		word_search = convertToStringArray(word_search)

		# replace word with all caps version in word search
		
		# variable for word search with word found
		local_word_search_found_word = findWordHorizontally(word_search, word)

		# if word was found, replace word search with word search with word highlighted
		if(local_word_search_found_word != False):
			word_search = local_word_search_found_word
			continue
		
		# delete useless variable
		del local_word_search_found_word

		# revert back to 2D array
		word_search = convertTo2DArray(word_search)
		
		# rotate word search back to original by rotating clockwise 3 times (same thing as rotating counter clockwise)
		word_search = rotateArrayCounterClockwise(word_search)

		# find diagonal occurences (this one is much more complex than the casual horizontal string replace)


	# return solved word search
	return convertToStringArray(word_search, " ")

# test solve word search function
for row in solve_word_search(example_to_solve, ["jefferson", "washington", "clinton", "bush", "lincoln"]):
	print row