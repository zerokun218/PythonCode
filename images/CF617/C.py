t = int(input())
for _ in range(t):
    n = int(input())
    x, y = 0, 0
    a = input()
    for i in a:
        if i == 'L':
            x -= 1
        if i == 'R':
            x += 1
        if i == 'U':
            y += 1
        if i == 'D':
            y -= 1
    print('{}///{}'.format(x,y))