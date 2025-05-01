# 국회의원 선거

n = int(input())
li= [int(input()) for _ in range(n)]

count = 0

max_value = max(li)
while (li[0] != max(li)) or (li.count(max(li)) > 1):
    idx = li.index(max_value)
    if idx == 0: # 처음부터 최댓값인 경우
        idx = li.index(max_value, 1)
    li[idx] -= 1
    li[0] += 1
    count += 1
    max_value = max(li)

print(count)

# 특정 케이스 고려
