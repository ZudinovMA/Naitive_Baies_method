import numpy as np
import matplotlib.pyplot as plt


x_train = np.array([[180, 90], [170, 60], [160, 50], [175, 75], [190, 100], [180, 65], [150, 45], [169, 70], [165, 50], [185, 80]])
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

mw1, ml1 = np.mean(x_train[y_train == 1], axis=0)
mw_1, ml_1 = np.mean(x_train[y_train == -1], axis=0)

# формула для вычисления дисперсии здесь другая 1/N*sum
sw1, sl1 = np.var(x_train[y_train == 1], axis=0)
sw_1, sl_1 = np.var(x_train[y_train == -1], axis=0)

print('МО: ', mw1, ml1, mw_1, ml_1)
print('Дисперсии:', sw1, sl1, sw_1, sl_1)

x = []
for i in range(0, 2):
    if i == 0:
        a = int(input('Введите рост человека: '))
        x.append(a)
    else:
        a = int(input('Введите вес человека: '))
        x.append(a)

#x = [179, 70]  # рост, вес человека


a_1 = lambda x: -(x[0] - ml_1) ** 2 / (2 * sl_1) - (x[1] - mw_1) ** 2 / (2 * sw_1)
a1 = lambda x: -(x[0] - ml1) ** 2 / (2 * sl1) - (x[1] - mw1) ** 2 / (2 * sw1)
y = np.argmax([a_1(x), a1(x)])

if y == 0:
    print('Мужчина')
else:
    print('Женщина')

