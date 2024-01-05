import sys
input = sys.stdin.readline

n = int(input())
book_list = [input().strip() for _ in range(n)]

dic = {}
count_max = -1
book_max = []

#각각의 책이 몇 개 있는지 dic으로 확인하는 로직
for book in book_list: 
    if book in dic:
        dic[book]+=1
    else:
        dic[book]=1

#dic에서 최대 개수의 책을 찾는 로직
for key, count in dic.items():
    count_max = max(count_max, count)

#최대 개수의 책을 찾아 리스트로 저장
for key, count in dic.items():
    if count_max == count:
        book_max.append(key)
        
book_max.sort(reverse=True) # 사전순으로 찾기 위해 거꾸로 정렬 (리스트는 뒷부분에 접근이 더 빠르기 떄문에)
print(book_max[-1])