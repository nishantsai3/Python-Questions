s = input().split(" ")

answer = s[0]
for word in s:
    if(word.lower() < answer.lower() and word.isalpha()):
        answer = word

print(answer)