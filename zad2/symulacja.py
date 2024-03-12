import random
import csv

k = 50
N = [1000 * i for i in range(1, 101)] 
f = open('./data.csv', 'w')
writer = csv.writer(f)
writer.writerow(['n', 'b', 'u', 'c', 'd', 'd - c'])

for n in N:
    for i in range(k):
        slots = [0 for i in range(n)]
        balls = 0
        b, u, c, d = 0, 0, 0, 0
        empties = n
        ones = n #ones = less than 2s
        while True:
            r = random.randint(0, n - 1)
            balls += 1
            slots[r] += 1
            if b == 0 and slots[r] == 2:
                b = balls
            if balls == n:
                u = empties
            if slots[r] == 1:
                empties -= 1
                if empties == 0:
                    c = balls
            elif slots[r] == 2:
                ones -= 1
                if ones == 0:
                    d = balls
                    break
        writer.writerow([n, b, u, c, d, d - c])
    print(f'n = {n} done')
f.close()