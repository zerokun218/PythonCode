# zerokun181200
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    arr += list(map(int, input().split()))
    h = [0]*(n+2)
    for x in range(0,n):
        h[arr[x]] += 1
    ans = 0
    for x in range(1, n+1):
        ans += h[x]//x
        h[x+1] += h[x] % x
    print(ans)

