import stat_formula as f

# 1) Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

a = 200
b = 800

exp_val = f.unif_dist_exp_val(a,b) # 500
print(exp_val)

dispersion = f.unif_dist_stand_dev_sq(a,b) # 30000
print(dispersion)

# ------------------------------------
# 2) О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

dispersion2 = 0.2
a2 = 0.5
# решаем через формулу дисперсии для равномерн. распределения, 
# в полученном квадратном уравнении 2 корня, но подходит только тот, который больше левой границы
b2 = 2.2 
exp_val2 = f.unif_dist_exp_val(0.5,2.2) # 1.35
print(exp_val2)

# ------------------------------------
# 3) Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X) 
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

# M(X) = -2 
# D(X) = 16
# std(X) = 4