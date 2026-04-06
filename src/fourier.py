import numpy as np
import matplotlib.pyplot as plt

def f(x, mode="piecewise"):
    if mode == "square":
        return np.sign(x)
    elif mode == "sawtooth":
        return x
    elif mode == "piecewise":
        return np.where(x >= 0, x**2, -x)

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

    a = np.zeros(N+1)
    b = np.zeros(N+1)

    n = np.arange(1, N+1)
    
    cos_terms = np.cos(np.outer(n, np.pi*x/L))
    sin_terms = np.sin(np.outer(n, np.pi*x/L))
    
    a[1:] = (1/L) * np.trapezoid(y * cos_terms, x, axis=1)
    b[1:] = (1/L) * np.trapezoid(y * sin_terms, x, axis=1)

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
    n = np.arange(1, len(a))
    
    cos_terms = np.cos(np.outer(n, np.pi*x/L))
    sin_terms = np.sin(np.outer(n, np.pi*x/L))
    
    s = a0/2 + np.sum(a[1:, None]*cos_terms + b[1:, None]*sin_terms, axis=0)
    
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
