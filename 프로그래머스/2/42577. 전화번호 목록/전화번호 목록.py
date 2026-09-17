from collections import Counter

def solution(phone_book):
    
    dic = Counter(phone_book)
    
    for phone_number in phone_book:
        temp = ''
        for p in phone_number:
            temp += p
            if temp in dic and temp != phone_number:
                return False

    return True