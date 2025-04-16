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

# 문제 최적의 풀이 파악하기
# 무작정 코드작성부터 x
