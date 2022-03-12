import string


words = []
stripped_words = []
letter_quantities = {}
top_5_letters = []


with open("C:/Users/nr107/Desktop/WordleProgram/words.txt") as f:
    words = f.readlines()

for word in words:
    word = word.rstrip()
    for letter in word:
        if letter in letter_quantities:
            letter_quantities[letter] += 1
        else:
            letter_quantities[letter] = 1

sorted_answer = dict(sorted(letter_quantities.items(), key=lambda x: x[1], reverse = True))

counter = 0
for key in sorted_answer.keys():
    if counter < 5:
        top_5_letters.append(key)
        counter += 1


def letter_check(word, letter, element):
    if word[element] == letter:
        return True
    else:
        return False

def word_check(word, letter_element):
    for letter in top_5_letters:
        if letter_check(word, letter, letter_element):
            return True
    return False

def are_letters_different(word):
    counter = 4
    for num in range(5):
        for x in range(counter):
            if word[num] == word[num + (x+1)]:
                return False
        if counter == 0:
            return True
        counter -= 1


def find_optimal_words(words_to_check):
    holder = []
    for word in words_to_check:
        for element in range(0,5):
            if word_check(word, element) == False:
                break
            elif element == 4:
                holder.append(word)
    letter_quantities = []
    for word in holder:
        if are_letters_different(word):
            letter_quantities.append(word)
    return letter_quantities

def strip_words(words_to_strip):
    letter_quantities = []
    for word in words_to_strip:
        letter_quantities.append(word.rstrip())
    return letter_quantities

stripped_words = strip_words(words)

optimal_words = find_optimal_words(stripped_words)

print(optimal_words)