#task-> loops:The provided code stub reads and integer, , from STDIN. For all non-negative integers i<n , print i**2 .

n = int(input())
if n>=0:
    for i in range(0,n):
        print(i**2)