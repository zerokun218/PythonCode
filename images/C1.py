# 360/(2*4) = 45
# pi*(R**2)
# sin(x) = 0.5/R
# R = (0.5/sin(x))
# x = (360/(2*n))/2
import math
import decimal
t = int(input())
for _ in range(t):
    k = int(input())
    # if n == 2:
    #     print(1)
    # else:
    print(decimal.Decimal(str((2*(0.5/(math.tan(math.radians(360/((2*k)*2)))) ) ))).quantize(decimal.Decimal('0.000000000')))
# zero
