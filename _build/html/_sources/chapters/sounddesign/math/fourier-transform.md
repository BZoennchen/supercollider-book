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

The *Fourier transform (FT)* of an *integrable* function $y : \mathbb{R} \rightarrow \mathbb{C}$ is defined by

```{math}
:label: eq:fourier:transform:exp
Y(f) = \int\limits_{-\infty}^\infty y(t) e^{-i2\pi f t} dt, \quad \forall f \in \mathbb{R}.
```

The transform of function $y(t)$ at frequency $f$ is given by the complex number $Y(f)$.
````

Let me give you an intuition of how this follows from the coefficients of the *[Fourier series](def-fourier-series-exp)*. 
Consider an infinite period, i.e., $T$ goes to infinity. 
Therefore, we get

\begin{equation*}
\lim_{T \rightarrow \infty} c_n = \lim_{T \rightarrow \infty} \frac{1}{T} \int_T y(t) \cdot e^{-i2\pi n t / T}dt.
\end{equation*}

Since $T$ goes to infinity, the fundamental frequency $f_0 = 1 / T$ goes to zero.
Thus the discrete variables $n \cdot f_0$ all become continuous since $f_0 \rightarrow 0$.
Remember that, for the exponential form, $n$ goes from negative infinity to positive infinity.
We can summarize:

\begin{equation*}
\lim_{T \rightarrow \infty} \frac{n}{T} = \lim_{f_0 \rightarrow 0} n \cdot f_0 = f
\end{equation*}

following

\begin{equation*}
\lim_{T \rightarrow \infty} c_n = \left( \lim_{T \rightarrow \infty} \frac{1}{T}\right) \cdot \underbrace{\int_{-\infty}^\infty y(t) \cdot e^{-i2\pi f t}dt}_{Y(f)}.
\end{equation*}

Consequently,

\begin{equation*}
c_n = \frac{1}{T} Y\left( n \cdot f_0 \right) = \frac{1}{T} Y\left( n \cdot \frac{1}{T}\right)
\end{equation*}

holds, since the value of each part of the integral $Y(f)$ of length $T$ is equal to $T \cdot c_n$.
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
y(t) = \int\limits_{-\infty}^\infty Y(f) e^{i2\pi f t} df, \quad \forall t \in \mathbb{R}.
```

The inverse transform of function $Y(f)$ at time $t$ is given by the complex number $y(t)$.
````

The pair $(y, Y)$ are called *Fourier integral pair* or *Fourier transform pair* and we define $\mathcal{F}$ to be the Fourier transform operator with

$$\mathcal{F}\{y\} = Y, \quad \mathcal{F}^{-1}\{Y\} = y.$$

We are dealing with real-valued functions, but this is not a problem since $\mathbb{R} \subset \mathbb{C}$.
Real-valued functions are just a special case where $y(t) = \overline{y(t)}$ which implies

$$Y(f) = Y(-f),$$

i.e., we do not have to remember or compute anything for negative frequencies.