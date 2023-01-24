import sys
n = int(sys.stdin.readline())
reverse_list=[]
for _ in range(n):
    word_list = sys.stdin.readline().split()
    for i in word_list:
        a=''
        word = list(i) #각 문자를 리스트화
        word.reverse() #거꾸로
        for j in word: #각 문자열 다시 합침
            a+=j
        print(a,end=" ")
    print()
