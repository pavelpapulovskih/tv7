import numpy as np
import scipy.stats as stats
# Данные задач
data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
mu_0 = 2.5 # Среднее значение гипотезы
alpha = 0.05
n = len(data)
# Среднее значение и стандартное отклонение выборки
mean_X = np.mean(data)
std_dev_X = np.std(data, ddof=1)
# Т-статистика
t_stat = (mean_X - mu_0) / (std_dev_X / np.sqrt(n))
# Критическое значение для t-распределения
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
print(f"t-статистика: {t_stat}")
print(f"Критическое значение t: {t_crit}")
# Проверка гипотезы
if abs(t_stat) > t_crit:print("Отвергаем нулевую гипотезу.")
else:print("Нет оснований отвергать нулевую гипотезу.")