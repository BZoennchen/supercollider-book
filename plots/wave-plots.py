import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dpi = 300
transparent = True
PI = np.pi
TWO_PI = 2*PI
NUM = 200
show = True


def lineplot(x, y, filename=None, title=None):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)
    if show:
        plt.show()
    if filename != None:
        fig.savefig(filename, bbox_inches='tight',
                    transparent=transparent, pad_inches=0, dpi=dpi)


def sine(f, filename=None):
    t = np.linspace(0, 1, NUM)
    amp = np.sin(TWO_PI * f * t)
    lineplot(t, amp, filename)


def sawtooth(f, filename=None):
    t = np.linspace(0, 1, NUM)
    amp = 2 * (f*t - np.floor(1/2 + f*t))
    lineplot(t, amp, filename)


def square(f, filename=None):
    t = np.linspace(0, 1, NUM)
    amp = np.sign(np.sin(TWO_PI * f * t))
    lineplot(t, amp, filename)


def triangle(f, filename=None):
    t = np.linspace(0, 1, NUM)
    amp = 4 * np.abs(f * (t+1/4) - np.floor(1/2 + f * (t + 1/4))) - 1
    lineplot(t, amp, filename)


def sawtooth_ap(f, n=20, filename=None):
    t = np.linspace(0, 1, NUM)
    result = 0
    for k in range(1, n+1, 1):
        sign = -1 if k % 2 == 1 else 1
        result += sign * np.sin(TWO_PI * k * f * t) / k
    amp = 1/2 - 1/PI * result
    lineplot(t, amp, filename)


def square_ap(f, n=20, filename=None):
    t = np.linspace(0, 1, NUM)
    result = 0
    for k in range(1, n+1, 1):
        result += np.sin(TWO_PI * (2*k - 1) * f * t) / (2*k-1)
    amp = 4/PI * result
    lineplot(t, amp, filename)


def triangle_ap(f, n=20, filename=None):
    t = np.linspace(0, 1, NUM)
    result = 0
    for k in range(n):
        sign = -1 if k % 2 == 1 else 1
        result += sign * np.sin(TWO_PI * f * (2 * k + 1)
                                * t) / ((2 * k + 1)**2)
    amp = 8/(PI**2) * result
    lineplot(t, amp, filename)


def exp_map(k, filename=None):
    x = np.linspace(0, 1, NUM)
    fx = np.power(x, 1+(k-1)/3)
    lineplot(x, fx, filename, title=r'$y(x) = x^{1+(k-1)/3}$')


def main():
    #sine(1, './../figs/sounddesign/sine.png')
    #sawtooth(1, './../figs/sounddesign/sawtooth.png')
    #square(1, './../figs/sounddesign/square.png')
    triangle(1, './../figs/sounddesign/triangle.png')
    triangle_ap(f=1, n=5, filename='./../figs/sounddesign/triangle_5.png')
    #sawtooth_ap(f=1, n=20, filename='./../figs/sounddesign/sawtooth_20.png')
    #square_ap(f=1, n=20, filename='./../figs/sounddesign/square_20.png')

    exp_map(k=2, filename='./../figs/sounddesign/add-synth-env_2.png')
    exp_map(k=10, filename='./../figs/sounddesign/add-synth-env_10.png')


if __name__ == "__main__":
    sns.set_theme()
    sns.set_style("whitegrid")
    main()
