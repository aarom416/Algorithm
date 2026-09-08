def solution(babbling):
    can_sounds = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for word in babbling:
        temp = word
        for can_sound in can_sounds:
            temp = temp.replace(can_sound, ' ')
        if temp.strip() == '':
            count+=1
    return count