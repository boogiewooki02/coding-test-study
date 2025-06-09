# 11531.ㅔㅛ

d = {}
sum = 0
solved = set()

line = input()
while line != '-1':
    m, name, sol = line.split()
    m = int(m)
    
    if sol == 'wrong':
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
    elif sol == 'right':
        if name not in solved:
            sum += m
            if name in d:
                sum += d[name] * 20
            solved.add(name)

    line = input()

print(len(solved), sum)