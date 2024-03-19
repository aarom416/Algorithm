import sys

input = sys.stdin.readline

first = list(input().rstrip())
end = list(input().rstrip())

#첫 문자열을 마지막 문자열로 맞추는게 아니라 마지막 문자열 중 끝 문자에 대해 조건의 반대로 적용하며 첫 문자열을 만들어가는 방식
while len(end) != len(first):
    last_string = end[-1] #마지막 문자열의 끝 문자 
    if last_string == "A": #끝 문자가 A이면 없앰
        end.pop()
    else: #끝 문자가 B 이면 없애고 단순 거꾸로 정렬
        end.pop()
        end.reverse() 
if first == end:
    print(1)
else:
    print(0)
