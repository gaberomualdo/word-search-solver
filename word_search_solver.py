# example word search to solve
example_to_solve = [['x', 'k', 'i', 'z', 'f', 'm', 'a', 'b', 'h', 'i', 's', 'x', 'c', 'e', 'r', 'y'], ['d', 'k', 'v', 'm', 'b', 'f', 'w', 'n', 'h', 's', 'k', 'p', 'n', 'u', 'f', 'q'], ['h', 'v', 't', 'c', 'q', 'v', 'i', 'l', 'e', 'v', 'f', 'r', 'd', 'l', 'q', 'd'], ['k', 'p', 'o', 'o', 'g', 'r', 'c', 'f', 'a', 'd', 'd', 't', 'k', 's', 'e', 'h'], ['k', 'o', 's', 'x', 'h', 'b', 'n', 'o', 's', 'r', 'e', 'f', 'f', 'e', 'j', 'h'], ['d', 'k', 'w', 'o', 'f', 'e', 's', 'd', 'n', 'k', 'o', 'i', 'p', 'k', 'l', 'x'], ['q', 'g', 'a', 'o', 's', 't', 'm', 'q', 'i', 'l', 't', 'l', 'g', 'u', 'p', 'q'], ['b', 'x', 's', 'w', 'd', 'u', 'y', 'v', 'e', 'a', 'o', 'u', 's', 'p', 'u', 'b'], ['n', 'c', 'h', 'k', 'd', 'x', 'b', 'a', 's', 's', 'r', 'c', 'e', 'q', 'm', 'j'], ['r', 'r', 'i', 'p', 'c', 'r', 'b', 'u', 's', 'h', 'p', 'l', 'n', 'g', 'n', 'l'], ['a', 'q', 'n', 'f', 'e', 'm', 'h', 'r', 'g', 't', 'p', 'm', 'u', 'i', 'q', 'c'], ['l', 'h', 'g', 'e', 'z', 'p', 'l', 'o', 'j', 'v', 'p', 'x', 'e', 't', 'l', 's'], ['b', 'i', 't', 's', 'h', 'z', 'd', 'h', 'q', 'w', 'u', 'z', 'k', 'z', 'q', 't'], ['p', 'y', 'o', 'j', 'm', 'e', 'k', 'j', 'm', 'l', 'm', 'w', 'p', 'a', 'd', 'j'], ['u', 'a', 'n', 't', 'r', 't', 'l', 'i', 'c', 'l', 'i', 'n', 't', 'o', 'n', 'y'], ['d', 'q', 'g', 'd', 'e', 'o', 's', 'w', 'z', 'r', 'f', 'b', 'p', 'p', 'q', 'a']]

# solve word search function
def solve_word_search(word_search, words):
	# convert word search from 2D array of letters to array of strings with letters joined together as a row
	for row_index in range(len(word_search)):
		word_search[row_index] = "".join(word_search[row_index])

	# list of words found
	words_found = [False]*(len(words))

	# loop through each word and find
	for wordlist_index in range(len(words)):
		word = words[wordlist_index]
		# find horizontal occurences
		for row_index in range(len(word_search)):
			# word index will be an int of the index in the string where the word is (if found)
			word_index = False

			# try to get index of string
			try:
				word_index = word_search[row_index].index(word)
			except:
				pass

			try:
				# try reverse as well
				word_index = word_search[row_index].index(word[::-1])
			except:
				pass

			# if word was found in row
			if(word_index != False):
				words_found[wordlist_index] = True
				word_search[row_index] = (" "*word_index) + word_search[row_index][word_index:word_index + len(word)] + (" "*(len(word_search[row_index]) - len(word) - word_index))

	# return solved word search
	return word_search

# test solve word search function
print solve_word_search(example_to_solve, ["jefferson", "washington", "clinton", "bush", "lincoln"])