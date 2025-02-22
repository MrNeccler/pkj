import numpy as np

# Определяем коэффициенты системы уравнений
A = np.array([[4, -3, 2],
              [2, 5, -3],
              [5, 6, -2]])

B = np.array([9, 4, 18])

# 1. Решение с использованием формул Крамера
def cramer_method(A, B):
    D = np.linalg.det(A)  # Определитель матрицы A
    if D == 0:
        return None  # Система не имеет единственного решения

    # Определители для x, y, z
    D_x = np.linalg.det(np.column_stack((B, A[:, 1:])))
    D_y = np.linalg.det(np.column_stack((A[:, 0], B, A[:, 2])))
    D_z = np.linalg.det(np.column_stack((A[:, :2], B)))

    # Решения
    x = D_x / D
    y = D_y / D
    z = D_z / D

    return x, y, z

# 2. Решение с использованием метода Гаусса
def gauss_method(A, B):
    # Объединяем матрицы A и B
    augmented_matrix = np.column_stack((A, B))
    # Применяем метод Гаусса
    n = augmented_matrix.shape[0]
    
    for i in range(n):
        # Нормализация текущей строки
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        for j in range(i + 1, n):
            augmented_matrix[j] = augmented_matrix[j] - augmented_matrix[j, i] * augmented_matrix[i]

    # Обратная подстановка
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.sum(augmented_matrix[i, i + 1:n] * x[i + 1:n])

    return x

# Решаем систему
solution_cramer = cramer_method(A, B)
solution_gauss = gauss_method(A, B)

print("Решение с использованием формул Крамера:", solution_cramer)
print("Решение с использованием метода Гаусса:", solution_gauss)
