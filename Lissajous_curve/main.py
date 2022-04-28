import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init():
    line.set_data([], [])
    return line,


def function_x(a_b):
    return 30 * np.sin(a_b * t)


def function_y():
    return 30 * np.sin(1 * t)


def animate(i):
    a_b = 0.001 + 0.003 * i

    x = function_x(a_b)
    y = function_y()

    xdata, ydata = [], []
    xdata.append(x)
    ydata.append(y)

    line.set_data(xdata, ydata)
    return line,


if __name__ == "__main__":
    plt.style.use('dark_background')
    fig = plt.figure()
    ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))

    plt.title('Фигуры Лиссажу')
    plt.axis('off')

    line, = ax.plot([], [], lw=2)
    t = np.arange(-10, 10, 0.001)
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=5000, interval=1, blit=True)
    plt.show()
