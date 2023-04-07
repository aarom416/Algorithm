def solution(numbers):
    numbers=list(map(str,numbers)) #문자열로 바꿔야 각 자리수를 비교하여 정렬할 수 있음 ex) 234 < 24,
    #ex) 30,3 은 330이 되야 하지만 그냥 정렬하면 문자길이가 더 긴 30이 큰 수 이므로 303 이 됨
    #원소가 0이상 1000이하 이므로 문자열을 3번 반복한 것을 기준으로 정렬(셋째 자리 수까지 맞춰 비교하기 위해)
    #ex) 30,3 -> 303030,333 이므로 30<3 이됨
    #ex) 330,3 -> 330330330,333 -> 330<3
    numbers.sort(key=lambda x: x*3,reverse=True) 
    answer=''.join(numbers) #for 문 말고 join 함수 사용
    return str(int(answer)) #모든 원소가 0 인경우는 000... 이렇게 출력될 수 있으므로 정수 변환 후 다시 문자열로 변환하여 리턴
    
