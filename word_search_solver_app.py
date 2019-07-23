# import word_search_solver.py (function)
execfile("word_search_solver.py")

# variable for word search to solve
word_search_to_solve = []

# variable for while loop running
loop_status = True

# current row number variable (used as iteration count in while loop)
current_row_number = 1

# get words
words = raw_input("Enter words to find (separated by a comma): ")

# turn words into list of lowercase strings
words = "".join(words.lower().split(" ")).split(",")

# keep prompting user to enter new lines of word search until exit
print "\nEnter word search. Type each letter of each row separated by a space. When you're done, type \"exit\" and hit enter."

while(loop_status):
    # prompt user for new row of word search
    current_row = raw_input(str(current_row_number) + ": ")

    # if "done" was typed, then exit; else, add string to word_search variable
    if(current_row.lower() == "exit"):
        loop_status = False
    else:
        word_search_to_solve.append(list("".join(current_row.lower().split(" "))))
    
    current_row_number += 1

# variable for solved word search
solved_word_search = solveWordSearch(word_search_to_solve, words)

# remove letters which aren't parts of words

# loop through each row
for row_index in range(len(solved_word_search)):
    # loop through each letter in each row
    for item_index in range(len(solved_word_search[row_index])):
        # if letter is lowercase, replace with "*" as it is not a solution
        if(solved_word_search[row_index][item_index].lower() == solved_word_search[row_index][item_index]):
            # replace letter with "*"
            solved_word_search[row_index][item_index] = "*"

# convert array into list of strings (function)
def convertToArrayOfStrings(array):
    # this neat line maps the array to a list of strings (each letter joined by a space)
    return map(" ".join, array)

# use function to turn word search(es) into array of rows
word_search_to_solve = convertToArrayOfStrings(word_search_to_solve)
solved_word_search = convertToArrayOfStrings(solved_word_search)

# print the original and solved versions side by side, and labels above

# labels
print (" " * ((len(word_search_to_solve[0]) - 8) / 2)) + "ORIGINAL" + (" " * ((len(word_search_to_solve[0]) - 8) / 2)) + "\t\t" + (" " * ((len(word_search_to_solve[0]) - 7) / 2)) + "SOLVED"

# print each row of both versions side by side
for row_index in range(len(word_search_to_solve)):
    print word_search_to_solve[row_index] + "\t\t" + solved_word_search[row_index]
