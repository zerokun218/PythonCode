# # def minn(a, b):
# #     if len(a) > len(b):
# #         return b
# #     elif len(a) < len(b):
# #         return a
# #     else:
# #         return min(a,b)
        
# # def dq(i, x, y):
# #     if(i == 10):
# #         return '9'*(101)
# #     if(x == 0 and y == 0):
# #         return ''
	
	
# #     if(i <= x and i * i <= y):
# #         print(i, end=' ')
# #         print(x, end =' ')
# #         print(y )
# #         tmp = ''
# #         tmp = minn(str(i) + dq(i, x - i, y - (i*i)), str(i) + dq(i+1, x - i, y - (i*i)))
# #         tmp = minn(tmp, dq(i+1, x, y))
# #         return tmp
# #     else:
# #         return dq(i+1, x, y)

# # # print(dq(1,9,41))

# # f = [[['' for i in range(10000)] for ii in range(1000)] for iii in range(12)]
# # inf = '9'*(101)
# # for i in range(0, 901):
# #     for j in range(0, 8101):
# #         # print(i, end=' ')
# #         # print(j)
# #         f[10][i][j] = inf
# # for i in range(1, 11):
# #     f[i][0][0] = ''
# # for i in range(9, 0, -1):
# #     for x in range(1, 901):
# #         for y in range(1, 8101):
# #             if (i<= x and i*i <=y):
# #                 t = ''
# #                 t = minn(str(i) + f[i][x-i][y-i*i], str(i) + f[i+1][x-i][y-i*i])
# #                 t = minn(t, f[i+1][x][y])
# #                 f[i][x][y] = t
# #             else:
# #                 f[i][x][y] = f[i+1][x][y]
# # t = int(input())
# # for _ in range(t):
# #     a,b = map(int, input().split())
# #     if a > 900 or b > 8100:
# #         print('No')
# #     elif f[1][a][b] == inf:
# #         print('No')
# #     else:
# #         print(f[1][a][b])



# s = []
# res = ''
# final =''
# count = 0
# avail = [1]*(11)
# def kth_special_number(arr,k):
#     arr.sort()
#     if len(arr) == 1 and arr[0] == 0:
#         return '-1'
#     global count
#     global final
#     for i in arr:
#         if i == 0:
#             count += 1
#     if count == k:
#         return
#     arr.sort()
#     def res(a):
#         global final
#         final += "".join(a[1:])
#         # print(final)
#     def func(c,n):
#         global count, avail
#         for i in range(0, len(arr)):
#             s[c] = str(arr[i])
#             # print(s)
#             # print(count)
#             st = ''
#             st = ''.join(s[:])
#             if st[0] == '0' and avail[len(st)] == 1:
#                 count -= len(arr)**(len(st)-1)
#                 avail[len(st)] = 0
#             if c == n:
#                 count += 1
#                 if count == k:
#                     res(s)
#                     return
#             else:
#                 if count == k:
#                     return
#                 func(c+1,n)
#                 if count == k:
#                     return
#             if count == k:
#                 break
#         if count == k:
#             return
    
#     s = ['']*(10**8+1)
#     final = ''
#     count = 0
#     for x in range(1, 10+1):
#         func(1,x)

#     return final
       
# print(kth_special_number([1], 12))


#################

# 20 % 9 = 2
# 20 // 9 = 2
# 9 * 2
# '19' + 2
# '22'
################


s = [-1]*(101+1)
arr = [1,2,3,0]
k = 100
def func(arr, k):
    arr.sort()
    global s
    if arr[0] == 0 and len(arr) == 1:
        print(-1)
    j = 0
    m = 0
    if arr[0] == 0:
        j = 1
    for _ in range(1, k+1):
        s[0] = j
        while j == len(arr):
            if arr[0] == 0 and s[m+1] == -1:
                s[m+1] = 1
            else:
                s[m+1] += 1
            s[m] = 0
            j = s[m+1]
            m += 1
        j = s[0] + 1
        m = 0
        # print(s)
func(arr, k)
# print(s)
ans = ''
for i in range(0, len(s)):
    if s[i] == -1:
        break
    else:
        ans = str(arr[s[i]]) + ans
print(ans)
