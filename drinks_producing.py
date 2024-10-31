from pulp import LpMaximize, LpProblem, LpVariable

# Оголошуємо модель
model = LpProblem("Maximize-Production", LpMaximize)

# Змінні
lemonade = LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

# Обмеження
model += 2 * lemonade + fruit_juice <= 100  # Вода
model += lemonade <= 50  # Цукор
model += lemonade <= 30  # Лимонний сік
model += 2 * fruit_juice <= 40  # Фруктове пюре

# Функція мети
model += lemonade + fruit_juice

# Розв'язок задачі
model.solve()

# Результати
print("Оптимальна кількість Лимонаду:", lemonade.varValue)
print("Оптимальна кількість Фруктового соку:", fruit_juice.varValue)
print("Максимальна кількість продуктів:", model.objective.value())
