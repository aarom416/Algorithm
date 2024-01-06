import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    case = input().strip()
    result = True
    while len(case)>0:
        if case.startswith('100'): #맨앞이 100인 경우
            case = case[3:] #맨앞 100 제거
            while len(case)>0 and case.startswith('0'): #100+인 부분에서 0이 연속된 경우 0 제거
                case = case[1:]
            
            if len(case) == 0: #이때 마지막은 무조건 1로 끝나야되는데 100 처럼 끝난 경우 False 기록
                result = False
                break
            
            case = case[1:] #위에서 100+까지 제거했으므로 100+1인 부분에서 맨앞 1 제거
            
            while len(case)>0 and case.startswith('1'): 
                #100+1+ 부분에서 1001100100 처럼 다시 100이 시작되는 부분을 고려하여 break로 다시 위에서 처리
                if len(case)>=3 and case[1] == '0' and case[2] == '0': 
                    break
                else:
                    case = case[1:] #10011111 처럼 1 연속되는 부분 1 제거
                    
        elif case.startswith('01'): #맨앞이 01인 경우
            case = case[2:] #맨앞 01 제거 그 후 0110001 같이 100이 시작되는 부분은 위에서 알아서 처리됨
            
        else:
            result = False #그 외에 1100, 1010000 같이 맨앞에 다르 경우는 False 기록
            break
        
    if result:
        print("YES")
    else:
        print("NO")

#다른 풀이 - 정규식 이용 (re 모듈)
import sys
import re #정규식 엔진에 대한 인터페이스 제공
input = sys.stdin.readline

n = int(input())

pattern = re.compile('(100+1+|01)+') #정규식 패턴 입력
for _ in range(n):
    case = input().strip()
    if pattern.fullmatch(case): #입력된 패턴과 문자열이 남는 부분 없이 완벽하게 일치하는 지 검사. 일치하지 않으면 None
        print("YES")
    else:
        print("NO")
        
