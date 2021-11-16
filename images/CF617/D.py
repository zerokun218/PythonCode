n, a, b, k = map(int, input().split())
m = list(map(int, input().split()))
res = 0
x = []
for i in range(0, len(m)):
    tmp = 0
    tmp = m[i] % (a+b)
    if tmp != 0 and tmp <= a:
        res += 1
    else:
        if tmp == 0:
            x.append(a+b)
        else:
            x.append(tmp)
x.sort()
for i in x:
    j = 0
    if (i - a) % a != 0:
        j = (i-a)//a + 1
    else:
        j = (i-a)//a
    if k >= j:
        res += 1
        k -= j
print(res)