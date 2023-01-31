s = input()
a=[]
string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in string:
    a.append(s.count(i))
print(*a)