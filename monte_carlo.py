import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2

# Метод Монте-Карло
n = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)
below_curve = y_random < f(x_random)
integral_mc = (b - a) * f(b) * np.mean(below_curve)

# Аналітичний обчислення за допомогою функції quad
result, _ = quad(f, a, b)

# Виведення результатів
print("Метод Монте-Карло:", integral_mc)
print("Аналітичне значення інтеграла:", result)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
