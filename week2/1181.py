# 단어 정렬
n = int(input())
l = []

for _ in range(n):
    word = input()
    l.append(word)

l = list(set(l))
l.sort(key=lambda x: (len(x), x))

for v in l:
    print(v)

# set은 중복 데이터 처리
# sort 함수 사용법
# lambda 함수 형태 (lambda 받는값: 반환형태)
