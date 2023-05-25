import sys
input=sys.stdin.readline
n=int(input())
max_list=[]
rope_list=[int(input().rstrip()) for _ in range(n)]
rope_list.sort(reverse=True) #ex) 1 3 5 경우
#로프 하나 쓸 경우 최대 5*1
#로프 두개 쓸 경우 최대 3*2 (3 5 사용 못함-> 3 줄 끊어짐)
#로프 세개 쓸 경우 최대 1*3 
for i in range(len(rope_list)):
    max_list.append(rope_list[i]*(i+1))
print(max(max_list))
    
    