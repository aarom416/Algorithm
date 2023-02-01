string = input()
string_list=[]
for i in range(len(string)):
    string_list.append(string[i:(len(string))])
string_list.sort()
print('\n'.join(string_list))