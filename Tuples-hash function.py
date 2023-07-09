n = int(input())
integer_list = map(int, input().split())
x=tuple(integer_list)
print(str(hash(x)))