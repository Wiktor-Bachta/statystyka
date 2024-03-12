# Wiktor Bachta

import random
import math
import matplotlib.pyplot as plt

# a, b, m, l = 0, 8, 2, 12
# a, b, m, l = 0, math.pi, 1, 2
# a, b, m, l = 0, 1, 27/64, 1/5
a, b, m, l = -1, 1, 2, math.pi
k = 50
x_avg = [50 * i for i in range(1, 101)]
y_avg = []
x = [item for item in x_avg for i in range(k)]
y  = []

def f(x):
    # return x ** (1/3)
    # return math.sin(x)
    # return 4 * x * (1 - x) ** 3
    return 2 * (1 - x ** 2) ** (1/2) 

for n in x_avg :
    avg = 0
    sum = 0
    for i in range(k):
        c = 0
        for j in range(n):
            if random.uniform(0, m) < f(random.uniform(a, b)):
                c += 1
        estimate = c * (b - a) * m / n
        y.append(estimate)
        sum += estimate
    avg = sum/k
    y_avg.append(avg)

plt.xlabel('n')
plt.ylabel('aproksymacja')
plt.title('Przybliżanie całki metodą Monte Carlo')
plt.scatter(x, y, s=1)
plt.scatter(x_avg, y_avg, s=10, c='red')
plt.axhline(y = l, color = '#90ee90', linestyle = '-') 
plt.figtext(0.2, 0.84, f"średnia dla n = 5000 to w przybliżeniu: {avg:.6f}")
plt.figtext(0.2, 0.82, f"błąd względny wynosi: {abs((avg- l)*100/l):.6f}%")
plt.show()