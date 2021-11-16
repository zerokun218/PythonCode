t = int(input())
for _ in range(t):
    n,k = map(int, input().split())

    a = [0] + list(map(int, input().split()))
    k = k+1
    res = 0
    ma = 10**6
    while(k > 1):
        for i in range(1, n//2 + 1):
            if a[i] + a[-i] != k:
                res += 1
                if a[i] > k:
                    res += 1
                if a[-i] > k:
                    res += 1
        ma = min(res, ma)
        k -= 1
        res = 0
        # else:
    print(ma)