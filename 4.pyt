import numpy as np
import scipy.stats as stats
# Данные задач
group1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
group2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
group3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]
# ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3)
print(f"F-статистика: {f_statistic}")
print(f"p-значение: {p_value}")
alpha = 0.05
if p_value < alpha:print("Есть статистически значимые различия между группами.")
else:print("Нет статистически значимых различий между группами.")