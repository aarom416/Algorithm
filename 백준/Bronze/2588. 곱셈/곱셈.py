import sys

sum = [0,0,0]
total = 0

first_num = int(sys.stdin.readline().strip())
second_num = list(map(int, sys.stdin.readline().strip()))

for i in reversed(range(3)) : 
    print(first_num*second_num[i])
    sum[2-i] = (first_num*second_num[i])

for i in range(3) :
    total = total + sum[i]*(10**i) 
print(total)
    

#### 다른 사람 풀이

a = int(input())
b = int(input())

print(a*(b%10))
print(a*(b%100//10))
print(a*(b//100))
print(a*b)
