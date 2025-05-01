# 책 정리

n, m = map(int, input().split())
# box_list = [int(input()) for _ in range(n)]
# book_list = [int(input()) for _ in range(m)]

box_list = list(map(int, input().split()))
book_list = list(map(int, input().split()))

result = 0

for book in book_list:
    for i in range(len(box_list)):
        if box_list[i] < book:
            result += box_list[i]
            box_list[i] = 0
        else:
            box_list[i] -= book
            break

result += sum(box_list)

print(result)

# 스페이스 기준으로 입력 받기 <-> 엔터 기준으로 입력 받기
## 백준에서는 엄격하게 구분
