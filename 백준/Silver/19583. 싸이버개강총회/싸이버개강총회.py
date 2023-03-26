import sys
input=sys.stdin.readline
dic={}
string=input().replace(':',' ')
start_hour,start_minute,end_hour,end_minute,streaming_hour,streaming_minute=map(int,string.split())
while True:
    try:
        strings=input().rstrip()
        s=strings.replace(':',' ').split()
        std_hour=int(s[0])
        std_minute=int(s[1])
        std_name=s[2]
        if std_name not in dic:
            if (std_hour==start_hour and std_minute<=start_minute):
                dic[std_name]=1
            elif std_hour<start_hour:
                dic[std_name]=1
            else:
                dic[std_name]=0
        else:
            if dic[std_name]==1:
                if end_hour==std_hour==streaming_hour and end_minute<=std_minute<=streaming_minute:
                    dic[std_name]+=1
                elif end_hour<std_hour<streaming_hour:
                    dic[std_name]+=1
                elif end_hour<std_hour==streaming_hour and std_minute<=streaming_minute:
                    dic[std_name]+=1
                elif end_hour==std_hour<streaming_hour and end_minute<=std_minute:
                    dic[std_name]+=1         
    except:
        break    
cnt=0

for i in dic.keys():
    if dic[i]>=2:
        cnt+=1
print(cnt)
