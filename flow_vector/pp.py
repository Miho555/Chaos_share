# 2020.8.22 Vector flow map

import sympy as sm
import numpy as np
from scipy import integrate
from pylab import *


def Fix():
    x, y = sm.symbols('x, y', real=True)
    Y = y
    X = - y - x**3 + 2*x**2 + x - 2
    # use sympy's way of setting equations to zero
    YEqual = sm.Eq(Y, 0)
    XEqual = sm.Eq(X, 0)
    # compute fixed points
    equilibria = sm.solve( (XEqual, YEqual), x, y )
    print(equilibria)
    return equilibria


def main():

	fp = Fix()

	xvalues, yvalues = meshgrid(arange(-5, 5, 0.1), arange(-3, 3, 0.1))
	xdot = yvalues
	ydot = -yvalues - xvalues**3 + 2*xvalues**2 + xvalues - 2
	streamplot(xvalues, yvalues, xdot, ydot, color=xvalues)


	plot([-5,5],[0,0], 'k-', lw=2)# x 軸 (直線 x=0)
	plot([0,0],[-5,5], 'k-', lw=2)# y 軸 (直線 y=0)

	x_p = arange(-4, 4, 0.1)  # x座標を-10 から 10 まで 0.1 きざみで取得
	y_p = - x_p**3 + 2*x_p**2 + x_p - 2

	y_pp = arange(-4, 4, 0.1)  # x座標を-10 から 10 まで 0.1 きざみで取得
	x_pp = y_pp

	plot(x_p, y_p, 'b-')  # f1 plot
	plot(x_pp, y_pp, 'm-')  # f2 plot

	for point in fp:
		plot(point[0],point[1],"red", marker = "o", markersize = 5.0)

	xlim([-3, 3])
	ylim([-3, 3])
	xlabel('$x$')
	ylabel('$y$')
	#axis('square')
	savefig('image.jpg')
	grid(); show()

if __name__ == '__main__':
	main()
