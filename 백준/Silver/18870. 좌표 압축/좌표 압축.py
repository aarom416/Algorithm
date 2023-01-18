import sys
n = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))
num_setlist = list(set(num_list))
num_setlist.sort()
num_dict={} #시간복잡도 O(1)인 딕셔너리 사용
for i in range(len(num_setlist)): 
    num_dict[num_setlist[i]]=i #작은 숫자부터 인덱스 값 저장 (인덱스값=현재 숫자보다 작은 숫자의 개수)
for i in num_list:
    print(num_dict[i],end=" ") #처음 받은 num_list에서 각각의 키(숫자)에 따른 값(숫자보다 작은 값 개수) 출력