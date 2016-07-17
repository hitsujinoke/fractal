# coding: utf-8


import matplotlib.pyplot as plt
import matplotlib.cm as cm


def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image


def mandelbrot():
    x_p = 400
    y_p = 400
    image = initialize_image(x_p+1, y_p+1)
    max_iteration = 16
    for i in range(x_p+1):
        print(i)
        for k in range(y_p+1):
            x = 3.5*i/x_p - 2.0
            y = 2.0*k/y_p - 1.0
            z1 = 0 + 0j
            c = x + y * 1j
            iteration = 0
            while (abs(z1) < 2) and (iteration < max_iteration):
                z1 = z1*z1 + c
                iteration += 1
            else:
                image[k][i] = iteration

    plt.imshow(image, origin='lower', extent=(-2.5, 1.0, -1.0, 1.0),
               cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()


def man(x0=0, y0=0, xp=400, yp=400, xc=0, yc=0, xr=2, yr=2, ma=1000):
    x_p = xp
    y_p = yp
    image = initialize_image(x_p+1, y_p+1)
    max_iteration = ma
    for i in range(x_p+1):
        if i % 10 == 0:
            print(i)
        for k in range(y_p+1):
            x = 2*xr*i/x_p - xr + xc
            y = 2*yr*k/y_p - yr + yc
            z1 = x0 + y0 * 1j
            c = x + y * 1j
            iteration = 0
            while (abs(z1) < 2) and (iteration < max_iteration):
                z1 = z1*z1 + c
                iteration += 1
            else:
                image[k][i] = iteration

    plt.imshow(image, origin='lower', extent=(-xr+xc, xr+xc, -yr+yc, yr+yc),
               cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    man(ma=16)
