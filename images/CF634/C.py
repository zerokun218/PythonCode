t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    f = [0]*(n+1)
    m = 0
    count = 0
    for i in a:
        f[i] += 1
        m = max( m, f[i])
        if f[i] == 1:
            count += 1
    
    print(max(min(m, count-1), min(m-1, count)))

