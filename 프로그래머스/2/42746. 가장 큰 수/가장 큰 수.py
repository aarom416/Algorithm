def solution(numbers):
    # 1. 첫째 자릿수 위주 내림차순 정렬 (완벽함)
    result = sorted(numbers, key=lambda x: str(x) * 3, reverse=True)
    
    # 2. 하나로 이어 붙이기 (완벽함)
    answer = ''.join(map(str, result))
    
    # 3. 에러 유발하는 int() 대신, 맨 앞자리가 '0'인지 확인하기
    # 가장 큰 수 순서로 정렬했는데 맨 앞이 '0'이라는 것은 뒤에도 전부 '0'이라는 뜻입니다.
    # 예: "00000" -> "0"
    return "0" if answer[0] == '0' else answer
