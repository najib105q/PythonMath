import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Input:
        x: numpy array of points
    Output:
        numpy array representing any user-defined function evaluated at x
    """
    return np.where(x >= 0, x**2, -x)  # change this to any function you want

def fourier_series_coeffs(f, L, N, num_points=2000):
    """
    Input:
        f: callable function f(x)
        L: half-period
        N: number of Fourier terms
        num_points: number of integration points
    Output:
        a0: scalar Fourier coefficient
        a: numpy array of cosine coefficients
        b: numpy array of sine coefficients
    """
    x = np.linspace(-L, L, num_points)
    y = f(x)

    a0 = (1/L) * np.trapezoid(y, x)

    # Padding arrays to make indexing easier
    a = np.zeros(N+1)
    b = np.zeros(N+1)

    for n in range(1, N+1):
        a[n] = (1/L) * np.trapezoid(y * np.cos(n*np.pi*x/L), x)
        b[n] = (1/L) * np.trapezoid(y * np.sin(n*np.pi*x/L), x)

    return a0, a, b

def fourier_approx(x, L, a0, a, b):
    """
    Input:
        x: numpy array of evaluation points
        L: half-period
        a0: scalar Fourier coefficient
        a: cosine coefficient array
        b: sine coefficient array
    Output:
        numpy array of Fourier series values at x
    """
    N = len(a) - 1
    s = a0 / 2
    for n in range(1, N+1):
        s += a[n] * np.cos(n*np.pi*x/L) + b[n] * np.sin(n*np.pi*x/L)
    return s

if __name__ == "__main__":
    L = np.pi
    N = 20

    a0, a, b = fourier_series_coeffs(f, L, N)

    x_plot = np.linspace(-L, L, 2000)
    y_true = f(x_plot)
    y_approx = fourier_approx(x_plot, L, a0, a, b)

    plt.figure(figsize=(10, 5))
    plt.plot(x_plot, y_true, label="Original function", linewidth=2)
    plt.plot(x_plot, y_approx, label=f"Fourier approximation (N={N})", linewidth=2)
    plt.title("Fourier Series Approximation")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
