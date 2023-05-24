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

# 다른 풀이 -> 실패 (ABB BB BB BB BB BB BB BB BB BB BB BB 이 경우 A:9 B:8 가 아니라 B:9 A:8 이여야 함)
# 하지만 아래 풀이 경우 자릿수의 합이 아닌 자릿수의 위치를 기준으로 우선순위를 선정했기 때문에 무조건 A:9 B:8 임
import sys
input=sys.stdin.readline
n=int(input())
dic={}
string=[[] for _ in range(100)]
number=[0,1,2,3,4,5,6,7,8,9]
str_list=[]
sum=0
for _ in range(n): #앞번호 부터 큰 숫자를 부여하기 위해 거꾸로 정렬 ex)GCF, ACDEB 경우 str_list = FCG, BEDCA
    a=list(input().rstrip())
    a.reverse()
    str_list.append(a)
for str in str_list: #각 문자열대로 우선순위 저장 ex) string = [F,B],[C,E],[G,D],[C],[A]
    for idx,s in enumerate(str):
        string[idx].append(s)
for i in range(len(string)-1,-1,-1): #뒤부터 딕셔너리 적용해 큰숫자 부여 A=9,C=8,G=7,D=6,C=5,E=4,F=3,B=2
    if string[i]:
        for s in string[i]:
            if s not in dic:
                dic[s]=number.pop()
for i in range(len(str_list)): #딕셔너리를 토대로 각 숫자의 합 구함
    x=len(str_list[i])
    for s in range(len(str_list[i])-1,-1,-1):
        sum+=dic[str_list[i][s]]*(10**(x-1))
        x-=1
print(sum)
