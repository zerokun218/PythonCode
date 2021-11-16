t = int(input())
for _ in range(t):
    k = 2
    n = int(input())
    s = 3
    while (n % s != 0 and s <= n):
        s += 2**k
        k += 1
    print(n//s)
