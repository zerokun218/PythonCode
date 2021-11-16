def func(n, m):
    k = n//2
    s = m//2
    if n == 1:
        return 0
    if n == 2:
        return m
    return 2*(s + m-s)

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(func(n,m))
    