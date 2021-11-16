t = int(input())
for _ in range(t):
    x,y,z,w = map(int, input().split())
    ans = 0
    if y >= x:
        print(y)
    else:
        x = x-y
        ans += y
        if w >= z:
            print(-1)
        # else:
        #     res += d
        #     a -= (c-d)
        else:
            k = 0
            if x//(z-w) < x/(z-w):
                k = x//(z-w)+1
            else:
                k = x//(z-w)
            ans += k*z
            print(ans)
