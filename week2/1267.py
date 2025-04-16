# 핸드폰 요금
n = int(input())
# l = []
# for _ in range(n):
#     v = int(input())
#     l.append(v)
l = list(map(int, input().split()))

sum_y = 0
sum_m = 0
for v in l:
    sum_y += (v//30+1)*10
    sum_m += (v//60+1)*15
    
if (sum_y > sum_m):
    print("M", sum_m)
elif (sum_m > sum_y):
    print("Y", sum_y)
else:
    print("Y M", sum_m)