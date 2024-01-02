import sys
input = sys.stdin.readline
n = input().strip()

dic = {}
odd_count = 0
mid = ''
front = ''
back = ''

#dic 을 사용하여 단어에 따른 개수 구하는 로직
for i in n:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

#단어 홀수 인거 찾아 가운데 값으로 처리해주기 위한 로직
for s,count in dic.items():
    if count%2==1: #홀수이면
        odd_count +=1
        mid += s
        dic[s]-=1 # mid 로 사용했으므로 하나 제거
        if odd_count>=2: #팰린드롬은 홀수인 단어가 2개 이상이면 못만듬
            print("I'm Sorry Hansoo")
            exit()

#나머지를 사전순으로 팰린드롬을 만들어주는 로직
for s, count in sorted(dic.items()):
    front = front + s*(count//2) # fornt, back 으로 나눠 몫은 fonnt, 나머지는 back으로 처리 (10개인 경우, 5,5 로 나눔)
    back = back + s*(count - count//2)

print(front+mid+back[::-1]) #back은 거꾸로 나열하여 완성