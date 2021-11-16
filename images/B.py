t = int(input())

for _ in range(t):
    a = []
    b = []
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort(reverse = True)

    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
        else:
            break
    print(sum(a))

# 0 0 0 0 0 0 0
# 4 2 5 1 6 3 7
# 0 0 0 0 0 0 0 0 0
# 6 2 4 7 1 8 3 5 9
# 0 0 0 0 0 0 0 0  0 0 0 
# 4 8 2 5 9 1 6 10 3 7 11
# 2 5 8 11
# 1 4 7 10
# 3 6 9   