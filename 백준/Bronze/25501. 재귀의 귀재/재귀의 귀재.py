import sys

def recursion(word,l,r,call):
    if(l>=r):
        print(1,call)
    elif word[l]!=word[r]:
        print(0,call) 
    else:
        call+=1
        return recursion(word,l+1,r-1,call)

def isPalindrome(w):
    recursion(w,0,len(w)-1,1)

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    word = sys.stdin.readline().rstrip()
    isPalindrome(word)    