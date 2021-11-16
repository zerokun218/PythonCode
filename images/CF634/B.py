t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    s = ['']*(n+1)
    i = 1
    x = 0
    l = 0
    while i <= n:
        s[i] = chr(97 + x)
        x += 1
        l += 1
        if x == b:
            if l < a:
                x -= 1
                i += 1
                continue
            
            x = 0
            l = 0
            

        i += 1

        
    print(''.join(s))


