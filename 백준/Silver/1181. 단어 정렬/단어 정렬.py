import sys
n = int(sys.stdin.readline())
word_list = [sys.stdin.readline().rstrip() for _ in range(n)]
sorted_word = list(set(word_list)) #set으로 중복 제거
sorted_word.sort() #미리 사전식 정렬
sorted_word.sort(key=len) #마지막 단어 크기로 정렬
for i in sorted_word:
    print(i)