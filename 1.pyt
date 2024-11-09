import scipy.stats as stats
# Данные задач
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]
# Тест Манна-Уитни
u_statistic, p_value = stats.mannwhitneyu(x1, y1,
alternative='two-sided')
print(f"U-статистика: {u_statistic}")
print(f"P-значение: {p_value}")
# Вывод результатов
alpha = 0.05
if p_value < alpha:print("Есть статистически значимые различия между выборками.")
else:print("Нет статистически значимых различий между выборками.")