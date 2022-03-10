
words = []
answer = {}
first_letters = []
second_letters = []
third_letters = []
fourth_letters = []
fifth_letters = []
letters = []


with open("C:/Users/nr107/Desktop/WordleProgram/words.txt") as f:
    words = f.readlines()

for word in words:
    word = word.rstrip()
    for letter in word:
        if letter in answer:
            answer[letter] += 1
        else:
            answer[letter] = 1

sorted_answer = dict(sorted(answer.items(), key=lambda x: x[1], reverse = True))

counter = 0
for key in sorted_answer.keys():
    if counter < 5:
        letters.append(key)
        counter += 1


def letter_check(word, letter, element):
    if word[element] == letter:
        return True
    else:
        return False


for word in words:
    word = word.rstrip()
    for letter in letters:
        if letter_check(word, letter, 0):
            first_letters.append(word)

for word in first_letters:
    for letter in letters:
        if letter_check(word, letter, 1):
            second_letters.append(word)

for word in second_letters:
    for letter in letters:
        if letter_check(word, letter, 2):
            third_letters.append(word)

for word in third_letters:
    for letter in letters:
        if letter_check(word, letter, 3):
            fourth_letters.append(word)

for word in fourth_letters:
    for letter in letters:
        if letter_check(word, letter, 4):
            fifth_letters.append(word)


def are_letters_matching(word):
    counter = 4
    for num in range(5):
        for x in range(counter):
            if word[num] == word[num + (x+1)]:
                return False
        if counter == 0:
            return True
        counter -= 1

for word in fifth_letters:
    if are_letters_matching(word):
        print(word)
