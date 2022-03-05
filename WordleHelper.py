
words = []
answer = {}
first_letters = []
second_letters = []
third_letters = []
fourth_letters = []
fifth_letters = []
letters = ["s", "e", "a", "o", "r"]


with open("C:/Users/nr107/Desktop/WordleProgram/words.txt.txt") as f:
    words = f.readlines()

for word in words:
    word = word.rstrip()
    for letter in word:
        if letter in answer:
            answer[letter] += 1
        else:
            answer[letter] = 1

sorted_answer = sorted(answer.items(), key=lambda x: x[1], reverse = True)


# for i in sorted_answer:
#     print(i[0], i[1])

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

#for word in fifth_letters:
    #print(word)


counter = 0

for word in fifth_letters:
    while counter < 5:
        if word[counter] == word[counter + 1]:
            break
        elif word[counter] == word[counter + 2]:
        counter += 1
    counter = 0
