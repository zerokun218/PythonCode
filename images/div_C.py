a,b,c,d = map(int, input().split())

x = [ i for i in range(a, b+1)]
y = [ i for i in range(b, c+1)]
z = [ i for i in range(c, d+1)]

res = 0
i = 0
j = 0
k = 0
while(k < len(z)):
    # print(i)
    # print(j)
    # print(k)
    # print('---')
    if j == len(y):
        break
    if x[i] + y[j] > z[k]:
        res += (len(x) - i)*(len(y)-j) + (len(y) - j - 1)
        h, g = i, j
        # i -= 1
        # j += 1
        # while ( j < len(y) and i >= 0):
        #     if x[i] + y[j] > z[k]:
        #         res += len(y)-j
        #         j += 1
                
        #     else:
        #         i -= 1
        k += 1
        i = h
        j = g

    else:
        i += 1
        if i == len(x):
            i = len(x)-1
            j += 1
        if j == len(y):
            break
    
    print(res)
# res = 0
# for i in range(0, len(y)):
#     if x[0] + y[i] > z[0]:
#         res += len(x)*(len(y)-i)*(len(z))
print(res)