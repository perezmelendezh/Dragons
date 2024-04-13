#Homewrok number 6
#1 Random Plots
import matplotlib.pyplot as plt
import numpy as np

list_1 = np.random.randint(0, 101, 40)
list_2 = np.random.randint(0, 101, 40)
list_3 = np.random.randint(0, 101, 40)

fig, axs = plt.subplots(2)

axs[0].plot(list_1, color='orange', linewidth=10)
axs[0].plot(list_2, color='red', linestyle='dashed')

axs[1].scatter(range(len(list_3)), list_3, color='magenta', marker='D')

plt.show()

# 2 van der Waals Gas
#This are the constants in the equation

R = 0.083144 #barL/(mol)K
a = 16.02 #barL^2/(mol)^2
b = 0.1124 #L/mol

P = np.linspace(1, 10, 100) # bar
V = np.linspace(10, 30, 100) # L

P, V = np.meshgrid(P, V)

#3 Monte Carlo pi

import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N):
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)

    dist = np.sqrt(x**2 + y**2)

    Nin = np.sum(dist <= 1)

    pi_est = 4 * Nin / N

    return pi_est, x, y, dist

for N in [1e3, 1e4, 1e5, 1e6]:
    pi_est, _, _, _ = estimate_pi(int(N))
    print(f'N = {N}, Pi = {pi_est}')


N = int(1e4)
pi_est, x, y, dist = estimate_pi(N)

plt.figure(figsize=(6,6))
plt.scatter(x[dist <= 1], y[dist <= 1], color='blue', label='Within quarter circle')
plt.scatter(x[dist > 1], y[dist > 1], color='red', label='Outside quarter circle')

plt.text(0.5, 0.5, f'Pi = {pi_est}', fontsize=12, ha='center')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Monte Carlo Pi Estimation')
plt.axis('equal') 
plt.show()
