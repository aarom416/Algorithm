import sys

def merge_sort(a):
    if len(a)==1:
        return a
    mid = (len(a)+1)//2
    l = merge_sort(a[:mid]) #전반부 정렬
    r = merge_sort(a[mid:]) #후반부 저열ㄹ
    a2=[]
    i,j=0,0
    while i<len(l) and j <len(r): #병합
        if l[i]>r[j]:
            result.append(r[j])
            a2.append(r[j])
            j+=1
        else:
            result.append(l[i])
            a2.append(l[i])
            i+=1
    while i<len(l): #왼쪽 배열 부분 남는 경우
        result.append(l[i])
        a2.append(l[i])
        i+=1
    while j<len(r): #오른쪽 배열 부분 남는 경우
        result.append(r[j])
        a2.append(r[j])
        j+=1
    return a2    
n,k = map(int, sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
result=[]
merge_sort(num_list)
if len(result)>=k:
    print(result[k-1])
else:
    print(-1)