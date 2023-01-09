test = int(input())

for i in range(test):
    cnt = 0
    score = []
    n = list(map(int,input().split()))
    for j in range(1,len(n)):
        score.append(n[j]) # 첫번쨰 학생수를 제외한 리스트
    avg = sum(score)/len(score)

    for i in score:
        if i > avg:
            cnt += 1
    print(f"{cnt/len(score)*100:.3f}%")
    
#다른 문제 풀이

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')

 
