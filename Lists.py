N=int(input())
u=[]
for i in range(N):
    s=list(input().split())
    if s[0]=="insert":
        u.insert(int(s[1]),int(s[2]))
    if s[0]=="remove":
        u.remove(int(s[1]))
    if s[0]=="append":
         u.append(int(s[1]))
    if s[0]=='sort':
         u.sort()
    if s[0]=='pop':
         u.pop()
    if s[0]=='reverse':
         u.reverse()     
    if s[0]=='print':
          print(u)