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
