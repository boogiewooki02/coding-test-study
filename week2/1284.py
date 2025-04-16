# 집 주소
def getLength(num):
    # num = str(num)
    sum = 0
    for n in num:
        if n == '1':
            sum += 2
        elif n == '0':
            sum += 4
        else:
            sum += 3
    return sum + len(num) + 1

n = input()
while n != "0":
    print(getLength(n))
    n = input()

# 함수 분리
