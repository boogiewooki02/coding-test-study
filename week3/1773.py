# 폭죽쇼

# n, c = map(int, input().split())

# timetable = {i: 0 for i in range(1, c)}

# for _ in range(n):
#     t = int(input())
    
#     for key in timetable:
#         if key%t == 0:
#             timetable[key] += 1

# result = 0

# for v in timetable.values():
#     if v != 0:
#         result += 1

# print(result)
## 메모리 초과

n, c = map(int, input().split())
timetable = set()

for _ in range(n):
    t = int(input())
    tmp = t
    while tmp <= c:
        timetable.add(tmp)
        tmp += t

print(len(timetable))
