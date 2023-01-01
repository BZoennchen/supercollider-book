# Convolution

Convolution is an operation that takes two functions and outputs a new function.
In that sense, it is very similar to addition or multiplication.
Given two function $y_1, y_2$ we can compute a new function

$$y_3(t) = (y_1 \cdot y_2)(t) = y_1(t) \cdot y_2(t).$$

The same is true for the convolution of these two functions:

$$y_3(t) = (y_1 * y_2)(t).$$

But what does the *convolution operator* $*$ really do?

## Discrete Convolution

Let us start with two arrays of numbers which represent discrete functions $y_1, y_2$.

We can use component-wise multiplication to generate a new function:

```isc
[1,2,3,4] * [-1,3,-1,3] // [ -1, 6, -3, 12 ], y_1[k] * y_2[k]
```

In that case,

$$y_3[k] = y_1[k] \cdot y_2[k].$$

The convolution is defined very differently.
The idea is to mirrow the second function and to compute the weighted sum of a sliding window.

```{figure} ../../../figs/sounddesign/math/array_conv.png
---
width: 900px
name: fig-array-conv
---
Visualization of the computation of a convolution of two discrete signals (arrays of numbers).
```

Given $y_1 = [1,2,3,4]$ and $y_2 = [ -1, 6, -3, 1]$, we use sliding window to compute the new function by a weighted sum.

\begin{equation*}
\begin{split}
y[-3] &= -1 \cdot 1 &= -1 \\
y[-2] &= -1 \cdot 2 + 3 \cdot 1 &= 1 \\
y[-1] &= -1 \cdot 3 + 3 \cdot 2 - 1 \cdot 1 &= 2 \\
y[+0] &= -1 \cdot 4 + 3 \cdot 3 - 1 \cdot 2 + 3 \cdot 1 &= 6 \\
y[+1] &= +3 \cdot 4 -1 \cdot 3 + 3 \cdot 2 &= 15\\
y[+2] &= -1 \cdot 4 + 3 \cdot 3 &= 5 \\
y[+3] &= +3 \cdot 4 &= 12
\end{split}
\end{equation*}

Interestingly, the lengths of the signals do not have to match, and the new length of the new signal is equal to the sum of the length of the original signals minus 2.

The following ``sclang`` function computes the convolution of two discrete function:

```isc
(
~convolve = {arg a, b;
    var a_pad, b_pad, result, val;

    a_pad = Array.fill(b.size-1, 0) ++ a;
    b_pad = b.reverse ++ Array.fill(a.size-1, 0);

    result = [];
    for(0, a.size+b.size-2, {
        val = (a_pad * b_pad).sum;
        result = result ++ [val];
        b_pad = b_pad.rotate(1);
    });
    result;
};
)

~convolve.([1,2,3,4], [-1,3,-1,3]); // [ -1, 1, 2, 6, 15, 5, 12 ]
```

````{admonition} Convolution of Discrete Signals
:name: def-discrete-convolution
:class: definition

Given two discrete and finite signals $y_1, y_2 : \mathbb{N} \rightarrow \mathbb{R}$ of length $N_1$ and $N_2$ respectively. Then the convolution of those two singals is defined by

\begin{equation}
(y_1 * y_2)[n] = y[n] = \sum\limits_{k=0, n-k\geq 0}^{N_1} y_1[k] \cdot y_2[n-k],
\end{equation}

where $y: \{0, \ldots, N_1 + N_2 - 2\} \rightarrow \mathbb{R}$.
````

Since we are most interested in peridic functions, a more useful definition is given by the *circular discrete convolution*.
In that case, we $y_2$ to be $N_2$-periodic.

````{admonition} Circular Discrete Convolution
:name: def-circular-discrete-convolution
:class: definition

Given two discrete signals $y_1, y_2$, where $y_1$ is defined for $0, \ldots N-1$ and $y_2$ is a periodic function with period equal to $N_2$. Then the circular convolution of those two singals is defined by

\begin{equation}
(y_1 * y_2)[n] = y[n] = \sum\limits_{k=0}^{N-1} y_1[k] \cdot y_2[n-k],
\end{equation}

where $y : \mathbb{Z} \rightarrow \mathbb{R}$ is periodic.
````

```{figure} ../../../figs/sounddesign/math/array_conv_periodic.png
---
width: 900px
name: fig-array-conv-periodic
---
Visualization of the computation of a convalution of two discrete signals (arrays of numbers) where the second is (infinite) and periodic.
```

The circular convolution of a finite signal with a infinite periodic discrete function is an infinite periodic funciton.
This in our code we do not construct an ``Array`` but a new function.

```isc
(
~cconvolve = {arg a, b;
    var func = {arg n;
        (a *.s (b.reverse.rotate).rotate(n)).sum;
    };
    func;
};
f = ~cconvolve.([1,2,3,4], [-1,3,-1,3]);
y = Array.fill(12, {arg i; f.(i);});
y // [ 14, 6, 14, 6, 14, 6, 14, 6, 14, 6, 14, 6 ]
)
```

The ``sclang`` code is relatively short.
``cconvolve`` returns the function, i.e., $y$, based on the two arrays, but here we assume the second one is circular.
Since our second array has a period of 2, the resulting signal $y$ also has a period of 2.

Note that the convolution is like multiplying two functions, but one is mirrored and shifted.
$(y_1 \cdot y_2)[n]$ is positive if the two functions are either both positive or both negative at $n$.
Therefore, if $y_1, y_2$ are periodic functions with DC = 0, $(y_1 \cdot y_2)(t)$ says something about their similarity, see section [Similarity of Periodic Functions](sec-similarity-of-functions).

Since the convolution is the sum of these similarity measures, it tells us something about the similarity of the two functions too.
In our example, we can see that $y_2$ mirrored is most similar if it is not shifted.
The argument $n$ of $(y_1 * y_2)[n]$ defines the shift of the second function, which determines the **phase** if we are in the domain of periodic functions!

If both signals are discrete but infinite (and defined on $\mathbb{Z}$), the discrete convolution of $y_1, y_2$ is given by:

\begin{equation}
(y_1 * y_2)[n] = \sum\limits_{k=-\infty}^{\infty} y_1[k] \cdot y_2[n-k] = \sum\limits_{k=-\infty}^{\infty} y_1[n-k] \cdot y_2[k].
\end{equation}

## Continuous Convolution

If $y_1, y_2$ are continuous functions then the sum becomes an integral.

````{admonition} Convolution
:name: def-convolution
:class: definition

Given two functions $y_1, y_2 : \mathbb{R} \rightarrow \mathbb{R}$ then the *convolution* is defined by 

\begin{equation}
(y_1 * y_2)(t) = y(t) = \int_{-\infty}^{\infty} y_1(\tau) \cdot y_2(t-\tau) d\tau,
\end{equation}
````

This looks intimidating but there is nothing to fear.
Instead of a sum over an index $k$ we have the integration over $\tau$ and $t$ represents the shift of our second (mirrored) funciton.

## Examples

Imagine the function $y$ which is 1 between 0 and 1 and zero elsewhere.
$y$ represents a square.
Consequently, $(y * y)$ represents the overlapping area of two squares.
Since the second square is mirrored at the y-axis, $(y * y)(t) = 0$ for $t=0$.
However, if we increase $t$, $(y * y)$ increases linearly until it reaches its maximum at $(y * y)(1) = 1$.
Then it decreases again.
Therefore, $(y * y)(t)$ is a triangle!

We can compute a discrete convolution on the audio server using the [Convolution](https://doc.sccode.org/Classes/Convolution.html) unit generator.
Let's try to contruct a triangle wave by convoluting two pulse waves.

```isc
({
    var n, sig;
    n = 512;
    sig = LFPulse.ar(s.sampleRate/n);
    sig = Convolution.ar(sig, sig, 2*n) * n.reciprocal;
    sig
}.plot(512*5/s.sampleRate);
)
```

```{figure} ../../../figs/sounddesign/math/sc-convolution-pulse.png
---
width: 400px
name: fig-sc-convolution-pulse
---
Convoluting two pulse waves results in a triangle wave.
```

As you can see, we get the expected result!

```isc
({
    var n, sig, kernel;
    n = 512;
    sig = LFSaw.ar(s.sampleRate/n);
    kernel = LFSaw.ar(s.sampleRate/n);
    sig = Convolution.ar(sig, kernel, 2*n) * n.reciprocal;
    sig
}.plot(512*5/s.sampleRate);
)
```

```{figure} ../../../figs/sounddesign/math/sc-convolution-saw.png
---
width: 400px
name: fig-sc-convolution-pulse
---
Convoluting two sawtooth waves results in parabola-like wave.
```