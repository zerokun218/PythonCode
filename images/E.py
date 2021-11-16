
# def dij(s, t):
#     global d
#     avail = [1]*(n+1)

#     while(True):
#         u = 0
#         for v in range(1, n+1):
#             if avail[v] == 1 and d[v] < d[u]:
#                 u = v
#         if u == 0 or u == t:
#             break
#         avail[u] = 0
#         for i in range(0, len(a[u])):
#             if d[a[u][i][0]] > d[u] + a[u][i][1]:
#                 d[a[u][i][0]] = d[u] + a[u][i][1]

# t = int(input())
# for _ in range(t):
#     n,m, e, b,c = map(int, input().split())

#     p = list(map(int, input().split()))

#     a = [[] for _ in range(n+1)]
#     for i in range(0, m):
#         x, y = map(int, input().split())
#         a[x].append((y,p[i]))
#         a[y].append((x,p[i]))
#     print(a)
#     d = [10**9]*(n+1)
#     d[e] = 0
#     dij(e,b)
#     res = d[b]
#     print(res)
#     d = [10**9]*(n+1)
#     d[b] = 0
#     dij(b,c)
#     print(d[c] + res)
      
    
