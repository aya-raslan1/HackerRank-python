# task->Find the Runner-Up Score!
n = int(input())
arr = map(int, input().split())
# convert into list
x=list(arr)
# put the min value in first and secand
first,second=-100,-100 
# sort the list in ascending order 
x.sort()
for x in x:
    if x>first:
        second=first
        first=x
print(second)