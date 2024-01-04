#처음 풀이 - while 문을 사용하여 폭발문자열이 있는지 확인하고 있으면 split으로 구분하여 join 으로 없애줌(replace도 생각)
# 하지만 이렇게 하면 while 과 in 으로 인해 시간 복잡도가 최악의 경우 O(N^2)으로 시간 초과 발생
import sys

input = sys.stdin.readline

string = input().strip()
bomb_string = input().strip()

while True:    
    if len(string)==0:
        print('FRULA')
        exit()
    if bomb_string in string:
        string=string.split(bomb_string)
        string=''.join(string)
    else:
        break
print(string)

#개선된 코드 - 시간복잡도를 O(N)으로 맞추기 위해 stack을 사용하여 문자열을 순환하면서 슬라이싱으로 폭발 문자열이 있는지 확인
#이때 폭발 문자열이 있는지 확인할 때 list를 join을 사용해 문자열 변환해 확인
import sys
input = sys.stdin.readline

string = input().strip()
bomb_string = input().strip()

bomb_length = len(bomb_string) 

stack = [] #문자열을 순환하여 stack으로 폭발문자열이 있는지 확인
for s in string:
    stack.append(s)
    if ''.join(stack[-bomb_length:]) == bomb_string: #슬라이싱을 사용하여 폭발 문자열 개수만큼 폭발 문자열 있는지 확인
        for _ in range(bomb_length): #개수만큼 pop()
            stack.pop()
if len(stack)==0:
    print("FRULA")
else:
    print(''.join(stack))
