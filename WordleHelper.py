
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

sorted_answer = sorted(answer.items(), key=lambda x: x[1], reverse = True)


for i in sorted_answer:
    print(i[0], i[1])
