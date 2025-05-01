# 소수

a, b, n = map(int, input().split())
tmp = a

for _ in range(n+1):
    result = tmp // b
    tmp = (tmp%b) * 10

print(result)

# 수학
