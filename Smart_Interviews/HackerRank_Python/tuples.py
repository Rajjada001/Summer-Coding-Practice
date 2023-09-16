# n = int(input())
# t = tuple()
# t = tuple(map(int, input().split()))[:n]
# print(t)
# print(hash(t))
n = int(input())
integer_list = map(int, input().split())

t = tuple(integer_list)
print(t)
print(hash(t))