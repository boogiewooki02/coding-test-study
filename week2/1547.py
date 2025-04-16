# 공
n = int(input())
tmp = 1

for _ in range(n):
    x, y = map(int, input().split())
    if tmp == x:
        tmp = y
    elif tmp == y:
        tmp = x
print(tmp)