# 치킨 쿠폰

def get_result(n, k):
    sum = n
    tmp = n

    while tmp >= k:
        sum += tmp//k
        tmp = tmp//k + tmp%k

    return sum

try:
    while True:
        n, k = map(int, input().split())
        print(get_result(n, k))
except:
    exit()

# eof 처리
