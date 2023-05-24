import sys
input=sys.stdin.readline
n=int(input())
str_dic={}
num_dic={}
number=[0,1,2,3,4,5,6,7,8,9]
str_list=[]
sum=0
for _ in range(n): #앞번호 부터 큰 숫자를 부여하기 위해 거꾸로 정렬 ex)GCF, ACDEB 경우 str_list = FCG, BEDCA
    a=list(input().rstrip())
    a.reverse()
    str_list.append(a)
str_list.sort(key=len,reverse=True) #길이가 큰 (값이 높은) 문자부터 높은 숫자를 부여하기 위해 key를 이용해 정렬
for str in str_list: #각 문자에 대해 자릿수 부여 ( ABB BB BB BB BB BB BB BB BB 처럼 나오면 B가 9여야함)->따라서 나오는 횟수에 따른 자릿수의 합으로 우선순위 설정
    for i in range(len(str)):
        if str[i] not in str_dic: 
            str_dic[str[i]]=10**i
        else:
            str_dic[str[i]]+=10**i
sorted_list=sorted(str_dic.items(),key=lambda x:x[1],reverse=True) #자릿수의 합으로 내림차순 정렬
for str in sorted_list: #숫자 부여
    num_dic[str[0]]=number.pop()
for str in str_list: #각 숫자의 합 구함
    for i in range(len(str)):
        sum+=num_dic[str[i]]*10**i
print(sum)