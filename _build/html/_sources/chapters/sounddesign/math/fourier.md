(sec-fourier)=
# Spectral Analysis and Synthesis

Jean-Baptise Joseph Fourier discovered a truely remarkable insights to our knowledge of waveforms in general and music in particular.

## Fourier Synthesis

```{admonition} Fourier Theorem (Synthesis)
:name: theorem-fourier-synthesis
:class: theorem
Any periodic vibration, no matter how complicated it seems, can be built up from sinusoids whose frequencies are integer multiples of a fundamental frequency, by choosing the proper amplitudes and phases.
```

I find this result still fascinating.
The process of constructing a periodic function by a *Foruier series* is called *Fourier synthesis*.

```{admonition} Fourier Series (FS)
:name: def-fourier-series
:class: definition
A *Fourier series* is a sum that represents a *periodic function* as a sum of *sine* and *cosine* waves.
The frequency of each wave in the sum is an integer multiple of the periodic function's fundamental frequency.
```

*Fourier series* can only represent periodic functions.
However, we will see later that an infinite period can be introduced.

In [additive synthesis](sec-additive-synthesis) we use *Fourier synthesis* to construct complicated waveforms from a sum of simple sinusoids, i.e., a *Fourier series*.

## Fourier Analysis

Fourier also observed that the process works in reverse.

```{admonition} Fourier Theorem (Analysis)
:name: theorem-fourier-analysis
:class: theorem
Any periodic vibration, no matter how complicated it seems, can be observed to be made up of a set of sinusiods whose frequencies are harmonics of a fundamental frequency, with particular amplitudes and phases.
```

The transform decomposes functions depending on space or **time** into functions depending on spatial frequency or **temporal frequency**.
This process is called *Fourier analysis*.
It provides a way to measure the strengths of individual components of a harmonic signal.
It starts with a time domain signal $x(t)$ and interprets it as a kind of recipe describing the spectral components and their strength that must be combined in order to preduce the corresponding frequency domain signal $X(f)$.

## Fourier Transform

The *Fourier transform* is the combination of *Fourier analysis* and *Fourier synthesis*.
Together they are called a *transform pair* because (ideally) the spectrum of a wave created by *Fourier synthesis* may be perfectly analyzed by *Fourier analysis*, and vice versa, with no loss of information.
A transform is just a way to represent the same information in an equivalent form.

## TODO

However, non-periodic functions can be handled using an extension of the [Fourier series](def-fourier-series) called *Fourier transform* which treats non-periodic functions as periodic with infinite period.
The transform decomposes functions depending on space or **time** into functions depending on spatial frequency or **temporal frequency**.
This process is called *Fourier analysis*.

```{admonition} Fourier Theorem
:name: theorem-fourier-1
:class: theorem
Any *piecewise continuous* and *bounded* function, can be represented by a *Fourier transform*.
```

In theory, the *Fourier series* of many functions consists of infinitely many terms.
Still, since our hardware resources are finite, we can only generate an approximation of the real thing.




How can we compute the pitch of a played piano key by analysing the signal genereated by the piano?
The answert to this problem is the Fourier transformation.
The Fourier transformation computes another representation of the audio signal called *Fourier transform*.
Instead of representing the sound by a signal, i.e., amplitudes $y(t)$ over time $t$, the Fourier transform represents the sound by frequency magnitude $d(f)$ over frequencies $f$.

While the signal displays the information across time, the Fourier transform displays the information across frequencies.
The signal tells us when certain notes are played in time, but hides the information about frequencies.
In contrast, the Fourier transform of music displays which notes (frequencies) are played, but hides the information about when the notes are played.

Let us start with an analog signal first.
And let us consider the basis for all possible audio signals, i.e., the **sinusoid** which is a function $y : \mathbb{R} \rightarrow \mathbb{R}$ defined by 

```{math}
:label: eq:sinusoid
    y(t) = A \cdot \sin(2\pi(f t - \phi))
```

for $t \in \mathbb{R}$.
As we know, the parameter $A$ corresponds to the **amplitude**, the parameter $f$ to the **frequency** (measured in Hz), and the parameter $\phi$ to the **phase** (measured in normalized radians with 1 corresponding to an angle of 360 degrees).

In the *Fourier analysis*, we consider prototype oscillations that are normalized with regard to their power (average energy) by setting $A = \sqrt{2}$.
Thus for each frequency parameter $f$ and phase parameter $\phi$ we obtain a sinusoid $\cos_{f,\phi}: \mathbb{R} \rightarrow \mathbb{R}$ given by

```{math}
:label: eq:sinusoid:norm
    \cos_{f,\phi}(t) = \sqrt{2} \cos(2\pi(f t - \phi))
```

for $t \in \mathbb{R}$.
Note that we get the same function for all $\phi + k$ with $k \in \mathbb{Z}$.

To model a signal $f(t)$ by $\cos_{f,\phi}(t)$ we want to find the best parameters $f, \phi$ such that we get the *best approximation* of $f(t)$.
In other words, we are searching for $f, \phi$ such that $g(t)$ and $\cos_{f,\phi}(t)$ are *most similar*.
One way to compare two functions is to compute their *inner product*.
If two vectors $\mathbf{a} = (a_1, \ldots, a_n), \mathbf{b} = (b_1, \ldots, b_n)$ are perpendicular, i.e., if they are very different, their *inner product* 

$$<\mathbf{a}, \mathbf{b}> := \sum\limits_{i=1}^n a_i \cdot b_i$$

is zero.
Their inner product is large if they are similar.
We can define the inner product of two functions $f: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$ in a similar fashion.
The sum changes to an integral:

```{math}
:label: eq:inner:product
    <f,g> := \int_{t \in \mathbb{R}} f(t)g(t) dt
```

For example, 

$$\int_{0}^1 \cos_{1,0}(t)\cos_{1,0.5}(t) dt = -1$$

and

$$\int_{0}^1 \cos_{1,0}(t)\cos_{1,0.25}(t) dt = 0$$

while 

$$\int_{0}^1 \cos_{1,0}(t)\cos_{1,0}(t) dt = 1.$$

If the term perpendicular is defined via the inner product one can say that $\cos_{1,0}$ is perpendicular to $\cos_{1,0.25}$.
Furthermore, $\cos_{1,0}$ and $\cos_{1,0.5}$ are very similar but they point in the opposite direction.

For a fixed frequency $f \in \mathbb{R}$, we define

```{math}
:label: eq:fourier:max
    d_f := \max\limits_{\phi \in [0;1)} \left( \int_{t \in \mathbb{R}} f(t) \cos_{f, \phi}(t) dt \right)
```

```{math}
:label: eq:fourier:maxarg
    \phi_f := \arg\max\limits_{\phi \in [0;1)} \left( \int_{t \in \mathbb{R}} f(t) \cos_{f, \phi}(t) dt \right)
```

where $d_f$ is the magnitude coefficient expressing the intensity of frequency $f$ within the signal $f$.
Additionally, the phase coefficient $\phi_f in [0;1)$ tells us how the sinusoid of frequency $f$ needs to be displaced in time to best fit the signal $f$. The **Fourier transform** of a function $f: \mathbb{R} \rightarrow \mathbb{R}$ is defined to be the collection of all coefficients $d_f$ and $\phi_f$ for $f \in \mathbb{R}$.