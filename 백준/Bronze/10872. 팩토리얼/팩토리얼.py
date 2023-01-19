def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1) #재귀함수 사용
n = int(input())
print(factorial(n))