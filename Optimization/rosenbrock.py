import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA


def quadratic(x, theta, a, c):
    # Число столбцов равно числу точек
    num_points = x.shape[1]
    f = []
    for i in range(0, num_points):
        pp = np.matrix([x.item(0, i), x.item(1, i)])
        f.append(pp * theta * pp.getH() + pp * a + c)
    return f


def rosenbrock(x):
    f = []
    cx_one_row_cube = []
    for i in range(0, len(cx_one_row)):
        cx_one_row_cube.append(pow(cx_one_row[i], 2))
        f.append(100 * pow((cy_one_row[i] - cx_one_row_cube[i]), 2) + pow((1 - cx_one_row_cube[i]), 2))
    return f

if __name__ == '__main__':
    x_limits = []
    # пределы и шаг измерения координат
    for x in np.arange(-1.0, 1.05, 0.05):
        x_limits.append(x)
    y_limits = x_limits
    # координатная сетка, cx  = -1, 0.95, 0.9,,, cy = -1, -1, -1 -1...
    cx, cy = np.meshgrid(x_limits, y_limits)
    # Объединение cx и cy в единый массив, содержащий координаты каждой точки в виде столбца
    cx_one_row = np.reshape(cy, -1)
    cy_one_row = np.reshape(cx, -1)
    xy = np.matrix([cx_one_row, cy_one_row])

    #theta = np.matrix('3 1 ; 1 2')
    #a = np.matrix('0 ; 0')
    # тета - симметричная, положительно определенная матрица размера nxn влияет на вид изолиний и куда будут повернуты
    theta = np.matrix('3 1;1 2')
    # a - вектор параметров, определяющий положение минимума по координатной сетке
    a = np.matrix('0; 0')
    # c - свободный параметр
    c = 1
    # Вычисление значений целевой функции
    f = quadratic(xy, theta, a, c)
    # Превращение f из вектора-строки в двумерный массив
    f = np.reshape(f, [len(cx), -1])

    # Вычисление значений целевой функции
    fr = rosenbrock(xy)
    # Превращение f из вектора-строки в двумерный массив
    fr = np.reshape(fr, [len(cx), -1])

    # графики
    plt.interactive(True)
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Построение графика функции в виде поверхности
    surf = ax.plot_surface(cx, cy, f)
    fig.show()
    # Построение изолиний
    plt.subplot(1, 1, 1)
    plt.contour(cy, cx, f)

    fg = plt.figure()
    ax = fg.gca(projection='3d')
    fr_surf = ax.plot_surface(cx, cy, fr)
    fg.show()

    # Собственные значения и собственные векторы заданной матрицы
    # вычисляет функция eigh. собственные значения находятся
    # на главной диагонали матрицы L, собственные векторы расположены в столбцах матрицы V.
    [l, v] = LA.eigh(theta)
    # Извлечение главной диагонали:
    # собственные значения и коэффициенты обусловленности
    print("Собственные значения: ", l[0], l[1])
    # Степень отличия линий равных значений от окружностей характеризует коэффициент обусловленности матрицы
    print("Коэффициент обусловленности: ", max(l) / min(l))
    # Расчет точки минимума.
    # При известных значениях матрицы teta и вектора a минимум квадратичной функции может быть найден аналитически
    x0 = -LA.inv(2 * theta) * a
    # Построение собственных векторов в виде отрезков, выходящих из точки x0
    for i in range(0, len(l)):
        vect = v[:, i]
        plt.plot([x0.item(0), x0.item(0) + vect.item(0)], [x0.item(1), x0.item(1) + vect.item(1)])

    plt.show()
    plt.subplot(1, 1, 1)
    plt.contour(cy, cx, fr)
    plt.show()
