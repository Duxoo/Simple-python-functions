import matplotlib.pyplot as plt
import numpy as np


# вычисление вектора откликов модели
def eval_model(x, y, alfa):
    return (1 / (alfa[0] * np.sqrt(2 * np.pi))) * np.exp(-1 * ((np.power((x - alfa[1]), 2) + np.power((y - alfa[2]), 2)) / (2 * alfa[0] * alfa[0])))


# вычисление матрицы Якоби
def jacobian(x, y, alfa):
    num_points = x.size
    num_params = alfa.size
    J = np.zeros((num_points, num_params))

    for i in range(num_points):
        # производная по sigma
        J[i, 0] = ((pow(x[i] - alfa[1], 2) + pow(y[i] - alfa[2], 2)) *
                   (np.exp((-1) * ((pow(x[i] - alfa[1], 2) + pow(y[i] - alfa[2], 2)) / (2 * pow(alfa[0], 2)))))) / \
                  (np.sqrt(2 * np.pi) * pow(alfa[0], 4)) - (np.exp((-1) * ((pow(x[i] - alfa[1], 2) + pow(y[i] - alfa[2], 2))
                   / (2 * pow(alfa[0], 2))))) / (np.sqrt(2 * np.pi) * pow(alfa[0], 2))
        # производная по x0
        J[i, 1] = ((x[i] - alfa[1]) * (np.exp((-1) * ((pow(x[i] - alfa[1], 2) + pow(y[i] - alfa[2], 2)) /
                  (2 * pow(alfa[0], 2)))))) / (np.sqrt(2 * np.pi) * pow(alfa[0], 3))
        # производная по y0
        J[i, 2] = ((y[i] - alfa[2]) * (np.exp((-1) * ((pow(x[i] - alfa[1], 2) + pow(y[i] - alfa[2], 2)) /
                  (2 * pow(alfa[0], 2)))))) / (np.sqrt(2 * np.pi) * pow(alfa[0], 3))
    return J


# оптимизация параметров модели от начального приближения методом Гаусса-Ньютона
def gaussnewton(x, y, z, alfa, max_iter, stop_norm=1e-10):
    error_fn = []
    for i in range(max_iter):
        # вычисление вектора откликов
        r = eval_model(x, y, alfa) - z
        J = jacobian(x, y, alfa)
        # подстройка параметров модели
        alfa_new = alfa - np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(J), J)), np.transpose(J)), r)
        # норма изменения вектора параметров
        change = np.linalg.norm(alfa_new - alfa) / np.linalg.norm(alfa)
        # норма вектора остатков
        error_fn.append(np.linalg.norm(r))
        print(alfa_new, change)
        if change < stop_norm:
            break
        alfa = alfa_new
    if error_fn[-1] < error_fn[0]:
        print('Поиск завершился удачно, ошибка={}'.format(error_fn[-1]))
    else:
        print('Поиск завершился неудачно')
    return alfa, error_fn


n = 70  # кол-во точек
xs = np.random.uniform(-5, 5, n)  # предиктор
ys = np.random.uniform(-5, 5, n)  # предиктор
X, Y = np.meshgrid(xs, ys)
system = [2, 0.1, 1]  # эталонные параметры
noise = 0.001  # амлитуда погрешности
Z = eval_model(X, Y, system) + np.random.uniform(-noise, noise, n)  # зависимая переменная
alfa = np.array([2.5, 0.3, 1.8])  # начальные значения параметров модели: сигма, x0, y0
iterations = 20  # кол-во итераций
alfa, err = gaussnewton(X.ravel(), Y.ravel(), Z.ravel(), alfa, iterations)

# эталонное
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.scatter(X, Y, Z, color="red")
Z = eval_model(X, Y, system)
axes.plot_surface(X, Y, Z)
plt.show()

# искомый
fig2 = plt.figure()
axes2 = fig2.gca(projection='3d')
axes2.scatter(X, Y, Z, color="green")
Z = eval_model(X, Y, alfa)
axes2.plot_surface(X, Y, Z)
plt.show()

# ошибка
plt.plot(range(len(err)), err)
plt.xlabel('итерация')
plt.ylabel('ошибка')
plt.show()
