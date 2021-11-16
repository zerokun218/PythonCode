# This is a sample Python script.
import numpy as np
from ordered_set import OrderedSet
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    # a = np.random.randn(10, 4)
    # print(a)
    # print(np.sum(a, axis=0, keepdims=True))
    # print()
    #
    # b = np.array(list(range(1, 11))).reshape(2, 5)
    # print(b)
    # print(np.sum(b, axis=0, keepdims=True))
    # print(np.maximum(b, 5))
    # print(np.max(b, axis=1, keepdims=True))

    # m, n, t = map(int, input().split())
    # l = 0
    # r = n
    # res = 10*16
    # remain = 0
    # while (l <= r ):
    #     mid = (r + l) // 2
    #     if id + mid//m <= n:
    #         res = mid
    #         remain = n - (mid + mid//m)
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # print(res*t + remain*t)

    a = list(random.randint(1, 3) for i in range(1, 10))
    print(a)
    print(OrderedSet(a))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
# def calc(a, b):
#     if m < a or n < b:
#         return 0
#     return (m - a + 1) * (n - b + 1)
#
#
# n, m, k = map(int, input().split())
# i = 1
# res = 0
# while i * i <= k:
#     if k % i == 0:
#         j = k / i
#         if j == i:
#             res += calc(i, j)
#         else:
#             res += calc(i, j) + calc(j, i)
#     i += 1
#
# print(int(res))