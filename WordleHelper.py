
words = []
answer = {}



with open("C:/Users/nr107/Desktop/WordleProgram/words.txt.txt") as f:
    words = f.readlines()

for word in words:
    for letter in word:
        if letter in answer:
            answer[letter] += 1
        else:
            answer[letter] = 1


print(answer)
