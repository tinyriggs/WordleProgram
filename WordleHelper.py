
words = []
answer = {}
acab = []
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
    fuck = letter_check(word,"s",0)



print(acab)
