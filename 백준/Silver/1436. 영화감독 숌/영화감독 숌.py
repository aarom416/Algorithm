n = int(input())
num=666
cnt=0
while True:
    if '666' in str(num): 
        cnt+=1
    if cnt==n: #n번째 영화제목은 cnt 값과 같음
        print(num)
        break
    num+=1