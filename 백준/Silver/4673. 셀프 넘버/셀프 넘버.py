num = set(range(1,10001)) #순서와 중복을 고려하지 않은 set 함수 사용
generated_num = set()

for i in range(1,10001):
    for j in str(i): #ex) i = 770, j = 7,7,0
        i += int(j) #ex) i = 770+7+7+0
    generated_num.add(i) #set 함수는 add로 추가

self_num = sorted(num-generated_num) 
#직접 수정이 아닌 self_num으로 값을 넘겨야하기 때문에 sort() 말고 sorted() 사용
#sort()는 리스트.sort() 형식, sorted()는 sorted(리스트) 형식
for i in self_num:
    print(i)