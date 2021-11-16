t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    tmp = a[0]
    ma = a[0]
    start = 1
    res = a[0]
    for i in a[1:]:
        if ma*i < 0:
            res += i
            ma = i
        else:
            res -= ma
            ma = max(ma, i)
            res += ma
    
    print(res)

