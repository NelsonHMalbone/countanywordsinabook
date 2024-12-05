# take the book file in beable to enter a word and see how many times that word is used.
def countWordsInFile(filepath, target_word):
    # initialize a counter
    count = 0

    # open the file
    with open(filepath, 'r', encoding='utf-8') as file:
        # reading the content
        content = file.read()

        # split content into words
        words = content.split()

        # count occurance of the target word
        count = words.count(target_word)

    return count

# running the function

filepath = 'book.txt' # use your filepath
# instead of hard coding the word to look up we will have a user input
user_input = input('Enter the word to count: ')

target_word = user_input   # replace with your word
word_count = countWordsInFile(filepath, target_word)
print(f"The word '{target_word}' appears {word_count} times in the file.")
