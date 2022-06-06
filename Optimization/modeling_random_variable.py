import math
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = "DejaVu Sans" # рус
def func(y):
    return (1/(np.sqrt(2*math.pi*s*s*y*y)))*(np.exp(-1*((np.log(y)-m)*(np.log(y)-m)/2/s/s)))
def obr(y):
    return (np.exp(s*(y-6)+m))
N=4992
A = 11550123.24425
B = 4127123.19225
m=1
s=0.3
mas=[]
mas.append(A%1)
for i in range(1,N):
    mas.append((A-B*mas[i-1])%1)
mas1=[]
mas2=[]
for i in range(len(mas)):
    if i%2==0:
        mas1.append(mas[i])
    else:
        mas2.append(mas[i])
X=[]
Y=[]
a_n=1
b_n=7
X = np.linspace(a_n,b_n,1000)
for i in range(1,N):
    Y = func(X)
maximum=max(Y)
mas_itog=[]
mas_test=[]
k=0
sum=0
for i in range(1,N-12):
    while k<12:
        sum+=mas[i+k]
        k+=1
    mas_itog.append(obr(sum))
    sum=0
    k=0

D=np.var(mas_itog)
M=np.mean(mas_itog)
D_teor = (np.exp(s*s)-1)*np.exp(2*m+(s*s))
M_teor = np.exp(m+((s*s)/2))
F=M-M_teor/math.sqrt(D+D_teor)
print("Теоретическая дисперсия:", D_teor)
print("Практическа дисперсия:", D)
print("Теоретическое мат ожидание:", M_teor)
print("Практическое мат ожидание:", M)
print (F)
#otbr=(N-len(mas_itog))/N*100
#print (otbr)
plt.plot(mas1,mas2,".")
plt.title(u"Случайные величины")
plt.xlabel(u"Четные элементы массива")
plt.ylabel(u"Нечетные элементы массива")
plt.show()
plt.plot(X, Y, '--')
plt.title(u"Плотность вероятности")
plt.xlabel(u"Случайная величина")
plt.ylabel(u"Плотность вероятности")
plt.show()
plt.hist(mas_itog,30)
plt.title(u"Гистограмма распределения случайной величины")
plt.xlabel(u"Случайная величина")
plt.ylabel(u"Количество попаданий")
plt.show()
