import sys
import bisect
read = sys.stdin.readline

sequence_N = int(read().strip())
sequence_list = list(map(int, read().strip().split()))

# record: 모든 수의 최장 수열의 길이를 저장하는 배열, dp: 해당 dp에 임시로 저장하는 배열(최대 길이를 알기 위해)
record = [0] * (sequence_N)
dp = [sequence_list[0]]
record[0] = 1

# 기존 최대값보다 큰 값이 들어오면, dp에 추가하고 최장길이를 record에 기록한다.
# 기존 최대값보다 작은 값이 들어오면, 그 값이 들어갈 중간 위치를 찾아서 동일한 dp를 가지는 값과 바꿔준다.
for i in range(1, sequence_N):
    if dp[-1] < sequence_list[i]:
        dp.append(sequence_list[i])
        record[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, sequence_list[i])
        dp[idx] = sequence_list[i]
        record[i] = idx + 1

# LIS를 담을 배열 ans
ans = []
find_dp = len(dp)
# 최대 dp를 가지는 수부터 역으로 하나씩 담는다. 그 이후 reverse하여 출력
# 더 작은 dp(LIS 길이)를 가지고, 더 작은 인덱스를 가지는 것들을 연결하여 담으면, 무조건 LIS가 완성된다.
for i in range(len(record) - 1, -1, -1):
    if record[i] == find_dp:
        ans.append(sequence_list[i])
        find_dp -= 1

    if find_dp < 1:
        break

print(len(ans))
print(*ans[::-1])