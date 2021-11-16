t = int(input())
for _ in range(t):
    n = int(input())
    if (n//2) % 2 == 1:
        print('NO')
    else:
        print('YES')
        s = 2
        for i in range(0, n//2):
            print(s, end=' ' )
            s += 2
        x = 1
        for i in range(0, n//2 - 1):
            print(x, end = ' ')
            x +=2
        print(x  +  n//2)
        