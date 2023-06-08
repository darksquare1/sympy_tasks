from scipy.fftpack import fft, ifft
import sympy as sp
import numpy as np

f = sp.simplify(input())
x = sp.Symbol('x')
x_min, x_max, n_points = map(int, input().split())
lp = np.linspace(x_min, x_max, n_points)
f_x = sp.lambdify(x, f)
values = f_x(lp)
fft_y = fft(values)
ifft_y = ifft(values)
print(*fft_y)  # дискретная трансформация Фурье
print(*ifft_y)  # обратное значение дисркетной трансормации Фурье
