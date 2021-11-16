t = int(input())
for _ in range(t):
    s = int(input())
    res = 0
    while(s >= 10):
        re = s//10
        res += (s - s%10)
        s = s % 10
        s = s + re
    res += s
    print(res)
