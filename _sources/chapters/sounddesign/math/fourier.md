---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(sec-fourier)=
# Spectral Analysis and Synthesis

>L’étude profonde de la nature est la source la plus féconde de découvertes mathématiques. -- Jean-Baptiste Joseph Fourier (1768–1830)

Given a signal $y(t)$ of a played piano key, how can we compute the pitch and how can we recreate that sound?
Spectral analysis and synthesis gives us some answers.
By *transforming* the representation of a signal, it catapultes from the space of amplitude over into the space of intensity over frequencies.

Spectral analysis works with two representations of sound:

1. **Inverse Fourier transform**: a signal in the time domain $y(t)$
2. **Fourier transform**: a signal in the frequency domain $Y(f)$

But before we start, let us discuss the immense importance of the Fourier transform and its inverse counterpart.

## Introduction

In mathematics, the meaning of *transform* and *transformation* is somewhat specific, but it still is rather wide or loose, when the definition sometimes found says it is a mathematical quantity obtained from a given quality by an algebraic, geometric, or functional operation.
In *transform theory*, mathematicians talk about a suitable choice of a function, called *kernel* (from the German *nucleus* or *core*), by which a problem may be simplified.
In 1822 *Jean-Baptise Joseph Fourier* discovered a truely remarkalbe *transformation* which gives us insights to our knowledge of waveforms in general and music in particular.

He claimed that any function, whether continuous or discontinuous, can be expanded into a series of sines.
That important work was corrected to

>Almost any periodic function can be represented by a Fourier series that converges.

and expanded upon by others to provide the foundation for various forms of the Fourier transform used since.

I find this result still fascinating.
At this point I have to mention that the great German mathematician *Carl Friedrich Gauß* already discovered this connection in 1805 and, what is even more remarkable, he formulated something quite similar as the *fast Fourier transform (FFT)*!
The reason his breakthrough was not widely adopted was because it only appeared after his death in volume three of his collected works and it was written with non-standard notation in a 19th century version of Latin. 

Especially since the re-discovery of the *fast Fourier transformation (FFT)* in 1965 by *Cooley* and *Tukey* to detect underground tests of atmoic bombs, the Fourier synthesis is a widespread technique performed in all areas of signal processing.
There are so many applications of the FFT, from solving differential equations to radar and sonar, studying crystal structures, WiFi and 5G.
It is no surprise that the mathematician *Gilbert Strang* called the FFT

>The most important numerical algorithm of our lifetime. -- Gilbert Strang

But why is that?
Well, it is all about computation speed!
The *FFT* reduces the time complexity of the *Discrete Fourier Transformation (DFT)* from $\mathcal{O}(n^2)$ to $\mathcal{O}(n\log(n))$ which makes the computation of the *DFT* fast thus applicable for many areas and purposes.

## Fourier Series

The process of constructing a periodic function by a *Foruier series* is called *Fourier synthesis*.

````{admonition} Fourier Series (FS)
:name: def-fourier-series
:class: definition
A *Fourier series* is a sum that represents a *periodic function* as a sum of *sine* and *cosine* waves.
The frequency of each wave in the sum is an integer multiple of the periodic function's fundamental frequency.
The *Foruier series* in amplitude-phase form $y_N(t)$ of a periodic function $y(t)$ is defined by

```{math}
:label: eq:fourier:series
y_N(t) = \frac{A_0}{2} + \sum\limits_{n=1}^N A_n \cdot \cos\left(\frac{2\pi \cdot n}{T}t - \phi_n\right)
```

where $N$ is potentially an infinite integer. 
$T$ is the period of $y(t)$, $A_n$ is the $n$-th hermonic's *amplitude* and $\phi_n$ is its *phase shift*.
$A_0/2$ is the DC component, it is the mean value of $y(t)$.
````

Except for pathological functions, any periodic function can be represented by a *Fourier series (FS)* that converges.
Convergence of *Fourier series* means that as more and more harmonics from the series are summed, each successive partial *Fourier series sum* will better approximate the function, and will equal the function with a potentially infinite number of harmonics.

```{admonition} Fourier Theorem
:name: theorem-fourier-synthesis
:class: theorem
Except for pathological functions, any periodic vibration, no matter how complicated it seems, can be built up from sinusoids whose frequencies are integer multiples of a fundamental frequency, by choosing the proper amplitudes and phases.
```

Non-periodic functions can be handled using an extension of the *Fourier series* called the *Fourier transform* which treats non-periodic functions as periodic with infinite period.
This transform thus can generate frequency domain representations of non-periodic functions as well as periodic functions, allowing a waveform to be converted between its time domain representation and its frequency domain representation.

In section [Additive Synthesis](sec-additive-synthesis) we use *Fourier synthesis* to construct complicated waveforms from a sum of simple sinusoids, i.e., a *Fourier series*.
For example, the (periodic) [sawtooth wave](sec-sawtooth-wave)

```{math}
    y_\text{saw}(t) = A \cdot 2 \left( f \cdot t -  \left \lfloor{ \frac{1}{2} + f \cdot t} \right \rfloor  \right),
```

can be constructed by an infinite sum

```{math}
    y_\text{saw}(t) = A \left( \frac{1}{2} - \frac{1}{\pi} \sum_{k=1}^{\infty} (-1)^k \frac{\sin(2\pi k f t)}{k} \right).
```

(sec-similarity-of-functions)=
## Similarity of Periodic Functions

Let us start from the assumption that the *Fourier Theorem* is correct (which it is) and let us consider a periodic function $y(t)$ and its *Fourier series (FS)* $y_N(t)$, see Eq. {eq}`eq:fourier:series`.
Than the question is: how can we compute all these amplitudes $A_n$ and phase shifts of the respective frequency?

$y_N(t)$ is a superposition of *sinusoidals* and we basically ask: how much of a specific sinusoidal is in $y(t)$.
Therefore, computing *sinusoidals* that are similar to $y(t)$ seems to be a good starting point.
Instead of similarity one speaks of *cross-correlation* which is a measure of similarity of two series as a function of the displacement of one relative to the other, also known as *sliding dot product* or *sliding inner-product*.

Functions are similar if their product result in a positive function.
In other words, if the integral of their product is positive.

In the following plot we can see this intuition at work.
The integral of $\sin(2\pi t)$ gives us $0.5$, i.e., there is alot of $\sin(2\pi t)$ in $\sin(2\pi t)$.
We also get a positive value for the integral of $\sin(2\pi t)$ multiplied with [sawtooth wave](sec-sawtooth-wave).
The integrals of the other products are zero.

```isc
( // generate the y(t) * sin(2*pi*u)
{[
    SinOsc.ar(1) * SinOsc.ar(1), 
    LFSaw.ar(1) * SinOsc.ar(1),
    SinOsc.ar(1) * SinOsc.ar(1,0.5*pi),
    LFTri.ar(0.5)*(-1)*SinOsc.ar(1)
]}.plot(1)
)
```

```{figure} ../../../figs/sounddesign/math/sin_product.jpeg
---
width: 800px
name: fig-sin-product
---
Product $y(t) \cdot \sin(2\pi t)$ for different $y(t)$.
```

Let's have a look at the sum of the first terms of the [sawtooth wave](sec-sawtooth-wave):

$$y(t) = \sum_{k=1}^8 \frac{1}{k}\sin(2\pi \cdot k \cdot t).$$

For shorthand let us also define the product with a sine wave of a certain frequency of $n \in \mathbb{N}$ Hz:

$$g_n(t) = y(t) \cdot \sin(2\pi \cdot n \cdot t).$$

```isc
({
    var sines = Array.fill(8, {arg i; 1/(i+1) * SinOsc.ar(i+1);});
    var y = Mix(sines);
    [y]++Array.fill(8, {arg i; y*SinOsc.ar(i+1)});
}.plot(1)
)
```

```{figure} ../../../figs/sounddesign/math/saw_analysis.jpeg
---
width: 800px
name: fig-saw-analysis
---
Multiplying functions: $y(t)$ in the upper left corner. In blue $\sin(2\pi \cdot f \cdot t)$, in orange the product $g_f(t)$ and in green the integral $\int_{0}^t g_f(t) dt$.
```

We get

$$\int_0^1 g_1(t)dt = \frac{1}{2}, \int_0^1 g_2(t)dt = \frac{1}{4}, \int_0^1 g_3(t)dt = \frac{1}{6}, \int_0^1 g_4(t)dt = \frac{1}{8}, \ldots$$

In general we get

```{math}
    \int_0^1 g_n(t)dt = \frac{1}{2n}.
```

Note that $\forall n \in \mathbb{N}:$

$$\int_0^1 \sin(2\pi \cdot n \cdot t)^2 dt = \frac{1}{2}$$

holds, thus

$$\int_0^1 \frac{1}{n}\sin(2\pi \cdot n \cdot t)^2 dt = \frac{1}{n} \int_0^1 \sin(2\pi \cdot n \cdot t)^2 dt = \frac{1}{2n}.$$

Therefore,

$$\int_0^1 g_n(t) dt = \frac{1}{n}\int_0^1 \sin(2\pi \cdot n \cdot t)^2 dt$$

follows.
If we look at the integral of 

$$h_n(t) = \left( y(t) - \frac{1}{n}\sin(2\pi \cdot n \cdot t) \right) \cdot \sin(2\pi \cdot n \cdot t),$$

then $\forall n \in \mathbb{N}:$

$$\int_0^1 h_n(t) dt = \int_{-\infty}^\infty h_n(t) dt = 0$$

holds.
In fact, if we look at $h_{i,j}(t) = \sin(2\pi i \cdot t ) \cdot \sin(2\pi j \cdot t)$ 

```{math}
:label: eq:perp:sines
\begin{split}
\forall i, j \in \mathbb{N}, i \neq j: \int_0^1 h_{i,j}(t) dt &= \int_{0}^1 h_{i,j}(t) dt = 0\\
&= \int_{-\infty}^\infty \sin(2\pi i \cdot t) \cdot \sin(2\pi j \cdot t ) dt\\
&= \int_{-\infty}^\infty h_{i,j}(t) dt
\end{split}
```

holds.

```{admonition} Perpendicular Functions
:name: theorem-perp-sine
:class: theorem

For all frequencies $i, j \in \mathbb{N}$ with $i \neq j$ 

$$\int_0^1 \sin(2\pi i \cdot t) \cdot \sin(2\pi j \cdot t ) dt = \int_{-\infty}^\infty \sin(2\pi i \cdot t) \cdot \sin(2\pi j \cdot t ) dt= 0$$

holds. We say that $\sin(2\pi i \cdot t)$ is *perpendicular* to $\sin(2\pi j \cdot t)$.
```

```isc
({ // generate sin(2*pi*i*x) * sin(2*pi*j*x)
    var sines = Array.fill(3, {arg i; 1/(i+1) * SinOsc.ar(i+1);});
    var y = Mix(sines);
    var indices = Array.fill2D(3, 3, {arg row, col; [row,col];}).flatten;
    indices.collect({arg index; var i = index[0], j = index[1];
        SinOsc.ar(i+1)*SinOsc.ar(j+1)
    });
}.plot(1)
)
```

```{figure} ../../../figs/sounddesign/math/sine_perp.jpeg
---
width: 800px
name: fig-sine-perp
---
$\sin(2\pi i \cdot t )$ in blue, $\sin(2\pi j \cdot t)$ in orange and $h_{i,j}(t)$ in green.
```

We say that these functions are **perpendicular** to each other because their scalar product (the integral of their product) is zero!

One way to compare two vectors $\mathbf{a} = (a_1, \ldots, a_n)$ and $\mathbf{b} = (b_1, \ldots, b_n)$ is to compute their *inner product*.
If two vectors $\mathbf{a}, \mathbf{b}$ are perpendicular, i.e., if they are very different, their *inner product* 

$$<\mathbf{a}, \mathbf{b}> := \sum\limits_{i=1}^n a_i \cdot b_i$$

is zero.
Their inner product is large if they are similar.
We can define the inner product of two functions $h: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$ in a similar fashion.
The sum changes to an integral.

````{admonition} Inner Product of two Functions
:name: def-scalar-product
:class: definition

Let $h: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$ then 

```{math}
:label: eq:inner:product
    <h,g> := \int_{t \in \mathbb{R}} h(t)g(t) dt
```
is the inner product of $h$ and $g$.
````

## Fourier Analysis

Until know we assumed that all *phase shifts* are zero.
Then we concluded that if we compute the integral of signal $y(t)$ multiplied with a sinusoid of the same phase we get:

1. either $1/(2n)$, where $n \in \mathbb{N}$ is the **frequency** of the sinusoid (similarity)
2. or zero, in this case $y(t)$ is perpendicular to the sinusoid (non-similarity)

We can reformulate the problem of similarity using an optimization problem.
Let us start with an analog signal first $y(t)$.
And let us reconsider the *[Fourier series](def-fourier-series)*:

```{math}
y_N(t) = \frac{A_0}{2} + \sum\limits_{n=1}^N A_n \cdot \cos\left(\frac{2\pi \cdot n}{T}t - \phi_n\right)
```

We multiply some term of $y_N(t)$ with our signal and integrate it over the period of our signal:

$$X_n(\phi) = \frac{2}{T}\int_T y(t) \cdot \cos\left(\frac{2\pi \cdot n}{T}t - \phi_n\right) dt, \quad \phi \in [0;2\pi].$$

Following our discussion at the start of section [Similarity of Periodic Functions](sec-similarity-of-functions), at the maximum of $X_n(\phi)$ the integral is equal to the **amplitude** $A_n \cdot \frac{T}{2}$.
If the respective sinusoid is part of the *Fourier series* 

$$A_n = \max\limits_{\phi \in [0;T]} X_n(\phi)$$

is not zero, otherwise it is.
Therefore, we multiply the integral by $\frac{2}{T}$ to get $A_n$.
Furthermore, we get the missing **phase shift** defined by

$$\phi_n = \arg\max\limits_{\phi \in [0;T]} X_n(\phi)$$

Using the equivalence of polar and Cartesian forms, that is,

$$\cos\left(\frac{2\pi \cdot n}{T}t - \phi_n\right) \equiv \cos(\phi_n) \cdot \cos\left(\frac{2\pi \cdot n}{T}t \right) + \sin(\phi_n) \cdot \sin\left(\frac{2\pi \cdot n}{T}t \right)$$

We can simplify the $X(\phi)$:

\begin{equation*}
\begin{split}
X_n(\phi) &= \frac{2}{T}\int_T y(t) \cdot \cos\left(\frac{2\pi \cdot n}{T}t - \phi_n\right) dt\\
&= \cos(\phi) \cdot \frac{2}{T}\int_T y(t) \cdot \cos\left(\frac{2\pi \cdot n}{T}t \right)dt + \sin(\phi) \cdot \frac{2}{T}\int_T y(t) \cdot \sin\left(\frac{2\pi \cdot n}{T}t \right)dt\\
&= \cos(\phi) \cdot a_n + \sin(\phi) \cdot b_n
\end{split}
\end{equation*}

The derivative of $X_n(\phi)$ is zero at the **phase** of maximum correlation.
Threfore,

$$X'_n(\phi_n) = \sin(\phi_n) \cdot a_n - \cos(\phi_n) b_n = 0 \Rightarrow \tan(\phi_n) = \frac{b_n}{a_n}$$

holds and the correlation peak value is:

$$A_n = X_n(\phi_n) = \cos(\phi_n) a_n + \sin(\phi_n) b_n = \sqrt{a_n^2 + b_n^2}.$$

In other words, $a_n$ and $b_n$ are the *Cartesian coordinates* of a vector with *polar coordinates* $A_n$ and $\phi_n$.
That is quite remarkable.

If we use [Euler's formula](theorem-euler-formula), we can write the *Fourier series* in its exponential form.

````{admonition} Fourier Series (FS) in its Exponential Form
:name: def-fourier-series-exp
:class: definition

The *Foruier series* in *exponential form* $y_N(t)$ of a periodic function $y(t)$ is defined by

$$y_N(t) = \sum\limits_{n = -N}^N c_n \cdot e^{i2\pi n t / T}$$

where $N$ is potentially an infinite integer. 
$T$ is the period of $y(t)$, $A_n$ is the $n$-th hermonic's *amplitude*
$c_n$ is defined by

$$
c_n = \frac{1}{T} \int_T y(t) \cdot e^{-i2\pi n t / T} = \begin{cases} 
A_0/2 &= a_0 / 2 & \text{ if } n = 0\\
\frac{A_n}{2}e^{-i \phi_n} &= \frac{1}{2} (a_n - i b_n), & \text{ if } n > 0\\
\overline{c}_{|n|}, & & \text{ if } n < 0
\end{cases}
$$

This form generalizes to **complex-valued functions**.
````

Finally, we can define 

$$Y_N(n) = (A_n, \phi_n),$$

to be the tupel of amplitude $A_n$ and the **phase shift** $\phi_n$ of the respective sinusoid with **frequency** $n$ of the *Fourier series* of a (real) **periodic function** $y(t)$.

## Fourier Transform

*Fourier series* are limited to *periodic functions*.
Musical signals are mostly periodic but what if they are not?
Well, the *Fourier series* is used to represent a *periodic function* by a discrete sum of *complex exponentials*, while the *Fourier transform* is then used to represent a **general, non-periodic function** by a *continuous superposition* or *integral of complex exponentials*.
The *Fourier transform* can be viewed as the limit of the *Fourier series* of a function with the period approaches to infinity.
We switch from a *discrete superposition* to a *continuous superposition*.
Of course the *Fourier transform* can also deal with periodic functions.
Therefore, one might say that it is more powerful.

````{admonition} Fourier Transform (TF) (in its Exponential Form)
:name: def-fourier-transform-exp
:class: definition

the *Fourier transform* of an *integgrable* function $y : \mathbb{R} \rightarrow \mathbb{C}$ is defined by

```{math}
:label: eq:fourier:transform:exp
Y(f) = \int\limits_{-\infty}^\infty y(t) e^{-i2\pi f t} dt, \quad \forall f \in \mathbb{R}.
```

The transform of function $y(t)$ at frequency $f$ is given by the complex number $Y(f)$.

````

Evaluating $Y(f) \in \mathbb{C}$ for all values of $f$ produces the **frequency-domain** function.
The complex number $Y(f)$, conveys both **apmplitude** and **phase** of the **frequency** $f$.

Under suitable conditions $y(t)$ cen be represented as a recombination of *complex exponentials* of all possible frequencies:

$$y(t) = \int\limits_{-\infty}^\infty Y(f) e^{i2\pi f t} df, \quad \forall t \in \mathbb{R}.$$

The pair $(y, Y)$ are called *Fourier integral pair* or *Fourier transform pair*.

## The Discrete Fourier Transform

Up to this point, we considered continuous signals $y(t)$.
However, on a computer everything is digitalized, i.e. discretized.
Calling 

```isc
s.sampleRate // 44100 Hz
```

gives us the *sample rate* of our audio signals.
On my machine, I use a sample rate of 44100 Hz, i.e. 44100 samples per second.
Therefore, a audio signal $y$ represents 1 seconds by 44100 samples (rational numbers)

$$y[i], y[i+1], \ldots y[i+44099]$$

When the highest frequency of a signal is less than one-half of the sample rate, the resulting discrete-time sequence is said to be free of the distortion known as **aliasing** (different signals become indistinguishable to each other).
In other words, the sample rate has to more than double the highest frequncy of the sampled signal to avoid aliasing.

```{figure} ../../../figs/sounddesign/math/sampling.png
---
width: 500px
name: fig-complex-plane
---
Discretized sine wave using a sample rate of 4 (green), 9 (orange), and 99 (blue).
```

To deal with a **periodic** and **discrete** signal we switch from the *Fourier transform* to the *discrete Fourier transform*.
Note that if we want to handle a **non-periodic** and **discrete** signal we apply the discrete-time Fourier transform*.

````{admonition} Discrete Fourier Series (DFS) in its Exponential Form
:name: def-fourier-series-exp-discrete
:class: definition

The *discrete Foruier series* $y_N[n]$ in *exponential form* of a periodic and discrete function $y[n]$ is defined by

$$y_N[n] = \sum\limits_{k=0}^{N-1} c[k] \cdot e^{\frac{i2\pi k}{N}n}, \quad n \in \mathbb{Z},$$

which are harmonics of a fundamental frequency $1/N$, for some positive integer $N$ (the period of the signal).
````

This looks very similar to the [Fourier series](def-fourier-series-exp) except that $e^{ikn\frac{2\pi}{N}}$ is not a function but a value!
Instead of a sum of functions, the *discrete Fourier Series* is a sum of discrete functions.
Furthermore, there are only $N$ distinct coefficients $c[0], \ldots c[N-1]$.