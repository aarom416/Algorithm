test = int(input())

for i in range(test):
    cnt = 0
    score = []
    n = list(map(int,input().split()))
    for j in range(1,len(n)):
        score.append(n[j])
    avg = sum(score)/len(score)

    for i in score:
        if i > avg:
            cnt += 1
    print(f"{cnt/len(score)*100:.3f}%")

