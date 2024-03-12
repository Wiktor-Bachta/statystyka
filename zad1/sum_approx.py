# Wiktor Bachta

import random
import math
import matplotlib.pyplot as plt

# a, b, m, l = 0, 8, 2, 12
# a, b, m, l = 0, math.pi, 1, 2
# a, b, m, l = 0, 1, 27/64, 1/5
a, b, m, l = -1, 1, 2, math.pi
x = [50 * i for i in range(1, 101)]
y  = []

def f(x):
    # return x ** (1/3)
    # return math.sin(x)
    # return 4 * x * (1 - x) ** 3
    return 2 * (1 - x ** 2) ** (1/2) 

for n in x:
    res = 0
    for k in range(n):
        res += f(a + k*(b - a)/n)*(b - a)/n
    y.append(res)

plt.scatter(x, y, s=1)
plt.axhline(y = l, color = '#90ee90', linestyle = '-') 
plt.plot([], [], ' ', label=f"średnia dla n = 5000 to w przybliżeniu: {res:.6f}")
plt.plot([], [], ' ', label=f"błąd względny wynosi: {abs((res - l)*100/l):.6f}%")
plt.legend()
plt.show()