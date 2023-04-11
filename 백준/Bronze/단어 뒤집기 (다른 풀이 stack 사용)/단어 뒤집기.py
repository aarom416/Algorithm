import sys
n = int(sys.stdin.readline())
reverse_list=[]
for _ in range(n):
    word_list = sys.stdin.readline().split() #리스트로 사용
    for i in word_list:
        a=''
        word = list(i) #각 문자를 리스트화
        word.reverse() #거꾸로
        for j in word: #각 문자열 다시 합침
            a+=j
        print(a,end=" ")
    print()

# 다른 풀이 (stack 사용)
n = int(input())
for i in range(n):
    string=input() #문자열로 사용
    string+=" "
    stack=[]
    for j in string:
        if j!=" ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(),end="")
            print(' ',end="")

