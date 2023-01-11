s = input()
string_cnt = []

string = list(s.upper())
for i in set(string):  # set을 사용해 중복제거 후 루프
    string_cnt.append(string.count(i))  # 각 문자 개수 구함

if string_cnt.count(max(string_cnt)) > 1:  # 최대값이 2개 이상인 경우
    print("?")
else:
    max_idx = string_cnt.index(max(string_cnt))  # 최대값 인덱스 저장
    strings = list(set(string))  # 인덱스 string_cnt와 string 맞추기 위해 string을 set으로 중복 제거
    print(strings[max_idx])
