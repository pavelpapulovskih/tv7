# Данные задач
first_measurement = [150, 160, 165, 145, 155]
second_measurement = [140, 155, 150, 130, 135]
# Тест для независимых выборок (хотя данные парные, используемt-тест для независимых выборок)
t_stat, p_value = stats.ttest_ind(first_measurement,
second_measurement, equal_var=False)
print(f"t-статистика: {t_stat}")
print(f"p-значение: {p_value}")
if p_value < alpha:print("Есть статистически значимые различия между первым ивторым измерением.")
else:print("Нет статистически значимых различий между первым и вторымизмерением.")
