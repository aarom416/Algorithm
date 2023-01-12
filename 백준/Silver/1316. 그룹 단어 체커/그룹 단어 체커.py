n = int(input())
word = [input() for _ in range(n)]

cnt = n

for i in range(n):
    word_list = list(word[i])
    for j in range(len(word_list)-1):
        if word_list[j]==word_list[j+1]:
            pass
        elif word_list[j] in word_list[j+1:]:
            cnt -= 1
            break
print(cnt)
