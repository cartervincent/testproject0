from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(14, 6))
ax = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)
total = 40  ## 点总数，限于文件大小，只进行40次
# 产生数据
x, y = np.random.random((2, total))
z = (x ** 2 + y ** 2 > 1)
# create the first plot
point, = ax.plot([], [], 'r.')
point2, = ax.plot([], [], 'b.')
line1, = ax1.plot([], [], 'red')
ax1.set_xlim(left=0, right=total)
# line, = ax.plot(x, y, z, label='parametric curve')
# ax.legend()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax1.set_ylim(bottom=0, top=5)
## 画园
x_ = np.array([i / 1000 for i in range(1000 + 1)])
y_ = np.sqrt(1 - x_ ** 2)
ax.plot(x_, y_, 'black')
dataInx = []
dataIny = []

dataOutx = []
dataOuty = []
counts = []
piValues = []


# second option - move the point position at every frame

def update_point(n, x, y, z, point):
    if z[n]:
        dataOutx.append(x[n])
        dataOuty.append(y[n])
    else:
        dataInx.append(x[n])
        dataIny.append(y[n])
    point.set_data(dataInx, dataIny)
    point2.set_data(dataOutx, dataOuty)

    # point.set_array([255,0,0])
    count = len(dataInx) + len(dataOutx)
    piValue = len(dataInx) / (count) * 4
    counts.append(count)
    piValues.append(piValue)
    line1.set_data(counts, piValues)
    ax.set_title('蒙特卡洛模拟，次数{:0>3}，圆周率估计值{:0<10}'.format(n, round(piValue, 10)), loc='center')
    ax1.set_title('蒙特卡洛模拟，次数{:0>3}，圆周率估计值{:0<10}'.format(n, round(piValue, 10)), loc='center')
    return point


ani = animation.FuncAnimation(fig, update_point, total, fargs=(x, y, z, point))
ani.save('test1.gif', writer='pillow')
plt.show()
