t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    o = 0
    e = 0
    for i in a:
        if i % 2 == 1:
            o += 1
        else:
            e += 1
    if o % 2 == 1:
        print('YES')
    else:
        if o > 0 and e > 0:
            print('YES')
        else:
            print('NO')   