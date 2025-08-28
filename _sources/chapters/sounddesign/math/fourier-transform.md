(sec-fourier-transform)=
# Fourier Transform

The *Fourier transform* is an extension or generalization of the *Fourier series*.
Instead of a finite period, we deal with an infinite period $T$.
Using this trick, we can represent aperiodic functions as well.
Similar to the concept of the *Fourier series* we are looking in two directions:

1. **Fourier transform**: going from the time domain $y: \mathbb{R} \rightarrow \mathbb{C}$ to the frequency domain $Y: \mathbb{R} \rightarrow \mathbb{C}$
1. **Inverse Fourier transform**: going from the frequency domain $Y: \mathbb{R} \rightarrow \mathbb{C}$ to the time domain $y: \mathbb{R} \rightarrow \mathbb{C}$.

*Fourier series* are limited to *periodic functions*.
Musical signals are mostly periodic, but what if they are not?
Well, the *Fourier series* is used to represent a *periodic function* by a discrete sum of *complex exponentials*, while the *Fourier transform* is then used to represent a **general, non-periodic function** by a *continuous superposition* or *integral of complex exponentials*.

The *Fourier transform* can be thought of as the *Fourier series* of a function with a period that approaches infinity.
We switch from a *discrete superposition* to a *continuous superposition*.
Of course, the *Fourier transform* can also deal with periodic functions.
Therefore, one might say that it is more powerful.

````{admonition} Fourier Transform (TF)
:name: def-fourier-transform-exp
:class: definition

The *Fourier transform (FT)* of an complex-valued *(Lebesgue) integrable* function function $y : \mathbb{R} \rightarrow \mathbb{C}$ is defined by

```{math}
:label: eq:fourier:transform:exp
\mathcal{F}\{y\} = Y(f) = \int\limits_{-\infty}^\infty y(t) e^{-i 2\pi f t} dt, \quad \forall f \in \mathbb{R}.
```

The transform of function $y(t)$ at frequency $f$ is given by the complex number $Y(f)$.
````

Let me give you an intuition of how this follows from the coefficients of the *[Fourier series](def-fourier-series-exp)*.
First remember, for a $T-$periodic function $y(t)$, the Fourier series is

$$y(t) = \sum\limits_{n=-\infty}^{\infty} c_n e^{i 2 \pi n t / T}$$

where the coefficients are 

$$c_n = \frac{1}{T} \int_T y(t) e^{-i 2 \pi n t / T}$$

So:

+ The spectrum consists of discrete frequencies at integer multiples of $2\pi / T$.
+ The spacing between frequencies is $2\pi / T$.

Consider now an infinite period, i.e., $T$ goes to infinity, that is, $T \rightarrow \infty$.
Then the fundamental frequency $1 / T = f_0$ becomes very small---it approaches zero.
Therefore, the harmonic frequencies $f_n = n f_0 = n / T$ get closer and closer together as $T$ approaches infinity.

Let us define 

$$Y_T(f) := Tc_n = \int_T y(t) e^{-i 2 \pi n t / T}$$

making the corresponding Fourier series

$$y_T(t) = \sum\limits_{n=-\infty}^{\infty} Y_T(f) e^{i 2 \pi n t / T} \frac{1}{T}.$$

As the period increases, the spectral lines become closer together, becoming a continuum.
The sum becomes an integral, that is,

$$\lim_{T \rightarrow \infty} y_T(t) = y(t) = \int_{-\infty}^\infty Y(f) e^{i 2 \pi f t} df.$$

Let's do it a little more slowly in multiple steps. 

```{math}
:label: eq:transform:step1
y(t) =& \lim_{T \rightarrow \infty} \sum\limits_{n=-\infty}^{\infty} (Tc_n) e^{i 2 \pi n t / T} \frac{1}{T}\\
=& \lim_{T \rightarrow \infty} \sum\limits_{n=-\infty}^{\infty} \int_T y(t) e^{-i 2 \pi n t / T} e^{i 2 \pi n t / T} \frac{1}{T}\\
=& \int_{-\infty}^{\infty} y(t) e^{-i 2 \pi f t} e^{i 2 \pi f t} df\\
=& \int_{-\infty}^\infty Y(f) e^{i 2 \pi f t} df
```

where $\Delta f = f_0 = 1 / T$ thus for $T \rightarrow \infty$, $\Delta f$ approaches $df$ and with

$$Y(f) = \int_{-\infty}^\infty y(t) e^{-i 2\pi f t} dt$$

\begin{equation*}
\lim_{T \rightarrow \infty} T c_n = Y\left( n \cdot \frac{1}{T}\right) = Y(f)
\end{equation*}

Everything works out.
Thus we can use the *Fourier transform* to compute the coefficients for the *[Fourier series](def-fourier-series-exp)*.

Evaluating $Y(f) \in \mathbb{C}$ for all values of $f$ produces the **frequency-domain** function.
Similar to $Y(n)$ of the *Fourier series*, the complex number $Y(f)$ (a [phasor](def-phasor)), conveys both **apmplitude** and **phase** of the **frequency** $f$.

The effect of multiplying $y(t)$ by $e^{-i2\pi f t}$ is to subtract $f$ from every frequency component of $y(t)$.
So the component that was at $f$ ends up at zero herz.
The integral produces its amplitude because all the other components are orthogonal and consequently integrate to zero over an infinite interval.
In section [Similarity of Periodic Functions](sec-similarity-of-functions), I tried to give an intuition for this phenomenon.

````{admonition} Inverse Fourier Transform (ITF)
:name: def-inverse-fourier-transform-exp
:class: definition

Under suitable conditions $y: \mathbb{R} \rightarrow \mathbb{C}$ can be represented as a recombination of *complex exponentials* of all possible frequencies, called *inverse Fourier transform (IFT)*:

```{math}
:label: eq:inverse:fourier:transform:exp
\mathcal{F}\{Y\} = y(t) = \int\limits_{-\infty}^\infty Y(f) e^{i2\pi f t} df, \quad \forall t \in \mathbb{R}.
```

The inverse transform of function $Y(f)$ at time $t$ is given by the complex number $y(t)$.
````

The pair $(y, Y)$ are called *Fourier integral pair* or *Fourier transform pair* and we define $\mathcal{F}$ to be the Fourier transform operator with

$$\mathcal{F}\{y\} = Y, \quad \mathcal{F}^{-1}\{Y\} = y.$$

We are dealing with real-valued functions, but this is not a problem since $\mathbb{R} \subset \mathbb{C}$.
Real-valued functions are just a special case where $y(t) = \overline{y(t)}$ which implies

$$Y(f) = Y(-f),$$

i.e., we do not have to remember or compute anything for negative frequencies.