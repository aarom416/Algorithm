def solution(lines):
    count = [0] * 201
    
    for start, end in lines:
        for i in range(start, end):
            count[i] += 1
            
    return sum(1 for x in count if x >= 2)



### 초기 풀이 -> 실패

### 배경 
### 각 선분을 3번만 비교하면 되므로 각각으로 비교로 접근했고 각 좌표의 크기로만 비교 하려함 
def solution(lines):
    [[x1,x2], [y1,y2], [z1,z2]] = lines
    
    result1 = [max(x1, y1), min(x2, y2)]
    result2 = [max(x1, z1), min(x2, z2)]
    result3 = [max(y1, z1), min(y2, z2)]
    
    a, b  = min(result1[0], result2[0], result3[0]), max(result1[1], result2[1], result3[1])
    
    
    return abs(b - a)

### 피드백
### 해당 내용은 여러 좌표를 합쳐서 겹치는 부분을 새로운 좌표에 표시하는 형식으로 보는 게 중요
### 특히 좌표로 표시할때 start 는 그 선분이 덮는 칸의 시작 좌표임을 명심해야함 따라서 end+1 가 아닌 end 로 사용해야 함(주의)


### 다른 사람 풀이
def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

### 피드백
### &(교집합), |(합칩합) 을 이용하기 위해 set 을 사용해 접근하는 방식. 교집합을 이용해 두 선분이 덮고 있는 선분을 구하고 합칩합을 이용해 총 겹치는 set을 구하고 len 으로 세서 마무리
