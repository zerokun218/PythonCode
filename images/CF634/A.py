t = int(input())

for _ in range(t):
    n = int(input())
    
    a = n//2 + 1
    res = 0
    res = n - a 
    if a == 1:
        print(0)
    else:
        print(res)
