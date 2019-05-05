import matplotlib.pyplot as plt

f1 = []
f2 = []
n = 10

for x1 in range(-n, n):
    for x2 in range(-n, n):
        if (x1**2) + (x2**2) <= n:
            f1.append(x1)
            f2.append(x2**3)

plt.plot(f1,f2,'o')
plt.xlabel("f1")
plt.ylabel("f2")
plt.axis([-5,5,-30,30])
plt.show()