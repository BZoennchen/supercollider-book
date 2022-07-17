# Complex Numbers

The history of mathematics is a history of discoveries and inventions.
The greeks focused on geometry and introduced natural and rational numbers.
Because of their fascianation with geometry, they did not come up with negative numbers.
A negative length makes no sense thus reality had to change before the mind was ready to see the concept of negative numbers.

To solve $2x = 4$ we rely on natural numbers.
We need negative numbers to solve $2x+4$, rational numbers for $4x = 2$ and real numbers for $x^2 = 2$.
How do we solve 

```{math}
:label: eq:complex:ex1
x^2 + 2 = 0?
```

Well we need *complex numbers*.
They extend real numbers by defintion.
We introduce a special symbol $i$ which is defined by

```{math}
:label: eq:complex:i
i^2 := -1.
```

Complex numbers are invented but they are also discovered because everything works out, i.e. they have all the rich mathematical properties we want to be helpful.
Let us solve Eq. {eq}`eq:complex:ex1`:

$$x^2 = -2 = 2 i^2 \iff x = \sqrt{2i^2} = \sqrt{2} \sqrt{i^2} = \sqrt{2}i$$

To make complex numbers useful they have to work with real numbers.
For example what is $i + 3$ where $i$ is a complex number and $3$ a real number.

```{admonition} Complex Numbers 
:name: def-complex-number
:class: definition
A *complex number* $z \in \mathbb{C}$

\begin{equation}
z = a + bi,
\end{equation}

with $i = \sqrt{-1}$, is the sum of a *real number* $a = \textbf{Re}(z) \in \mathbb{R}$ and an *imaginary number* $b = \textbf{Im}(z)$. 
```

Therefore a complex number $z$ has two parts: a real and imaginary part.
Note that squaring an imaginary number gives a real number, i.e. $(bi)^2 = -1b^2 = -b^2$.
Furthermore, we get $0 = 0 + 0i$, $bi = 0 + bi$, $a = a + 0i$.

Equality, addition, multiplication and negation works as expected.
There is a special operation called *complex conjugation*.

```{admonition} Complex Conjugation 
:name: def-complex-conjugate
:class: definition
The conjugation $\overline{z}$ of a complex number $z = a + bi$ is the negation of its imaginary part, i.e., 

\begin{equation}
\overline{z} = \overline{a + bi} = \overline{a} + \overline{bi} = a - bi.
\end{equation}
```

Multiplying a complex number $z = a + bi$ by its conjugate gives a real number:

$$z \cdot \overline{z} = (a + bi) \cdot (a - bi) = a^2 - (bi)^2 = a^2 + b^2.$$

## Complex Plane

We can use this fact to evaluate the division of two complex numbers $z_1 = a + bi, z_2 = c + di$:

$$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{ac-adi+bic+bdi^2}{c^2+d^2} = \frac{(ac+bd) + (bc-ad)i}{c^2+d^2}.$$

We can represent a complex number $z = a + bi$ by a point $p_z = (a, b)$ in the Cartesian plane which we then call complex plane.

```{figure} ../../../figs/sounddesign/math/complex-plane.png
---
width: 500px
name: fig-complex-plane
---
Numbers on the complex plane.
```

This gives us another representation using the angle $\phi$ and the magnitude $r$ of the vector $(a, b)$.
We have

\begin{equation}
\begin{split}
a &= r \cdot \cos(\phi)\\
bi &= r \cdot i\sin(\phi)
\end{split}
\end{equation}

thus 

\begin{equation}
\begin{split}
z &= a + bi\\
  &= (r \cdot \cos(\phi)) + (r \cdot i \sin(\phi))\\
  &= r \cdot (\cos(\phi) + i \sin(\phi))
\end{split}
\end{equation}

Given $a$ and $b$ we can compute $r$ by

\begin{equation}
r^2 = a^2 + b^2 = z \cdot \overline{z}
\end{equation}

and $\phi$ using 

\begin{equation}
\phi = \cos^{-1}(a/r)
\end{equation}

What happens geometrically if we multiply two complex numbers?
If one of the numbers is a real number, we just scale the magnitude.
Let $z_1 = r_1 \cdot (\cos(\alpha) + i \sin(\alpha))$ and $z_2 = r_2 \cdot (\cos(\beta) + i \sin(\beta))$ then

```{math}
:label: eq:complex:mul
\begin{split}
z_1 \cdot z_2 &= r_1 \cdot (\cos(\alpha) + i \sin(\alpha)) \cdot r_2 \cdot (\cos(\beta) + i \sin(\beta))\\
&= r_1r_2 \cdot (\cos(\alpha)\cos(\beta) + i\cos(\alpha)\sin(\beta) + i \sin(\alpha)\cos(\beta) + i^2 \sin(\alpha)\sin(\beta))\\
&= r_1r_2 \cdot [(\cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)) + i (\cos(\alpha)\sin(\beta)+\sin(\alpha)\cos(\beta))] \\
&= r_1r_2 \cdot [\cos(\alpha+\beta) + i \sin(\alpha+\beta)] 
\end{split}
```

The last step requires the trigonometry identities 

\begin{equation*}
\cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta) = \cos(\alpha + \beta)
\end{equation*}

and

\begin{equation*}
\cos(\alpha)\sin(\beta)+\sin(\alpha)\cos(\beta) = \sin(\alpha + \beta).
\end{equation*}

Eq. {eq}`eq:complex:mul` gives us some insights.
Product of two complex numbers equates to scaling and rotating by magnitude and angle of the second number respectively.

```{admonition} Product of Complex Numbers 
:name: theorem-complex-multiplication
:class: theorem
The product of two complex numbers is the product of their magnitudes and the sum of their angles.
```

Since $i = 1 \cdot (a \cos(90) + i\sin(90))$ holds, multiplying by $i$ equates to a counterclock rotation by 90 degrees.
Since $-i = 1 \cdot (a \cos(90) - i\sin(90)) = 1 \cdot (a \cos(90) + i\sin(-90))$, dividing by $i$ equates to multiplying by $-i$ thus

$$\frac{1}{i} = -i$$

and

$$\frac{1}{i} \cdot \frac{1}{i} = (-i)(-i) = -1.$$

From the rule of products of complex numbers follows *de Moivre's Theorem*.

```{admonition} de Moivre's Theorem 
:name: theorem-de-moivre
:class: theorem
Let $z = r \cdot (\cos(\phi) + i \sin(\phi))$ a *complex number* then

\begin{equation}
z^n = r^n (\cos(n\phi) + i \sin(n\phi)).
\end{equation}
```

## Euler's Formula

*Euler's formula* or *Euler's equation* is one of the most beautiful relationships one can think of.
It connects *Euler's number* $e$, $0$, $1$ and $\pi$.
To arrive at the formula we first have to do some work.

```{admonition} Taylor Sries 
:name: def-taylor-series
:class: definition
Let $f$ be a real or comlex-valued function that infinitely differentiable at real or complex number $z$ then 

\begin{equation}
\begin{split}
T_{f(z)}(x) &= f(z) + \frac{f'(z)}{1!}(x-z) + \frac{f''(z)}{2!}(x-z)^2 + \frac{f'''(z)}{3!}(x-z) + \ldots \\
&= \sum\limits_{k=0}^{\infty} \frac{f^{(k)}(z)}{k!}(x-z)
\end{split}
\end{equation}

is the *Taylor series* of $f(x)$ at $x = z$.
If $z = 0$ the series is also called *Maclaurin series*.

```

Often one approximate a function by using only the first $n$ terms of Tayler's serie.
Whet we now need is the Taylor series for the sine, cosine and the natural exponential function.
We know that $\sin'(x) = \cos(x)$ and $\cos'(x) = - \sin(x)$.
Furthermore $\sin(0) = 0$ and $\cos(0) = 1$.
Therefore, we get

```{math}
:label: eq:taylor:sin
\begin{split}
\sin(x) &= T_{\sin(0)}(x) = \sum\limits_{k=0}^{\infty} \frac{\sin^{(k)}(0)}{k!}(x)\\
&= 0 + x - 0 - \frac{x^3}{3!} + 0 + \frac{x^5}{5!} - 0 - \frac{x^7}{7!} + \ldots \\
&= x - \frac{x^3}{3!} +  \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots
\end{split}
```

for the sine function and 

```{math}
:label: eq:taylor:cos
\begin{split}
\cos(x) &= T_{\cos(0)}(x) = \sum\limits_{k=0}^{\infty} \frac{\cos^{(k)}(0)}{k!}(x)\\
&= 1 - 0 - \frac{x^2}{2!} + 0 + \frac{x^4}{4!} - 0 - \frac{x^6}{6!} + \ldots \\
&= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \ldots
\end{split}
```

for the cosine function.

```{figure} ../../../figs/sounddesign/math/taylor_sin.png
---
width: 400px
name: fig-taylor-sine
---
*Taylor series* that approximates $\sin(x)$ at $x=0$ using $1, 2, 3, 4, 5$ terms.
```

Furthermore, the natural exponential function has a quite nice form too

```{math}
:label: eq:taylor:euler
\begin{split}
e^x &= T_{e^0}(x) = \sum\limits_{k=0}^{\infty} \frac{\text{exp}^{(k)}(0)}{k!}x^k \\
&= \sum\limits_{k=0}^{\infty} \frac{x^k}{k!}
\end{split}
```

since $\text{exp}^{(k)}(x) = \text{exp}(x)$ for all $k \in \mathbb{N}_0$ and $e^0 = 1$.
Note that we donte $e^x$ by $\text{exp}(x)$.

```{figure} ../../../figs/sounddesign/math/taylor_exp.png
---
width: 400px
name: fig-taylor-exp
---
*Taylor series* that approximates $e^x$ at $x=0$ using $1, 2, 3, 4, 5$ terms.
```

What happens if we plug in an imaginary number like $\phi i$, with $\phi\in \mathbb{R}$?
Well let's see:

```{math}
\begin{split}
e^{\phi i} &= T_{e^0}(\phi i) = \sum\limits_{k=0}^{\infty} \frac{(\phi i)^k}{k!}\\
&= 1 + \frac{\phi i}{1!} + \frac{\phi^2i^2}{2!} + \frac{\phi^3i^3}{3!} + \frac{\phi^4i^4}{4!} + \frac{\phi^5i^5}{5!} + \frac{\phi^6i^6}{6!} \ldots \\
&= 1 + \frac{\phi i}{1!} - \frac{\phi^2}{2!} - \frac{\phi^3i}{3!} + \frac{\phi^4}{4!} + \frac{\phi^5i}{5!} - \frac{\phi^6}{6!} - \ldots \\
&= \left( 1 - \frac{\phi^2}{2!} + \frac{\phi^4}{4!} - \frac{\phi^6}{6!} + \ldots  \right) + i\left(\frac{\phi}{1!} - \frac{\phi^3}{3!} + \frac{\phi^5}{5!} - \ldots \right)\\
&= \cos(\phi) + i \sin(\phi).
\end{split}
```

We arrive at *Euler's formula* which links the hyperbolic functions involving $e$ to trigonomeitric functions involving $\pi$!

````{admonition} Euler's Formula
:name: theorem-euler-formula
:class: theorem
Let $i \phi$ be an imaginary number then

```{math}
:label: eq:euler
e^{i\phi} = \cos(\phi) + i \sin(\phi)
```

holds. This relation is called *Euler's formula*.

````

We can immidiatly follow that

$$e^{i\pi} = \cos(\pi) + i \sin(\pi) = -1 + i0 = -1$$

Therefore, the most beautiful of all times, called *Euler's identity* emerges

\begin{equation}
e^{i\pi} + 1 = 0.
\end{equation}

```{admonition} Phasor
:name: def-phasor
:class: definition
A *phasor* is the polar representation of any complex variable.

\begin{equation}
z = r e^{i\phi},
\end{equation}

where $r, \phi \in \mathbb{R}$.
```

Using Eq. {eq}`eq:euler` we can use the exponential function to represent our trigonometric functions.
We start with

$$(\cos(\phi) + i\sin(\phi)) + (\cos(\phi) - i\sin(\phi)) = 2 \cos(\phi) = e^{i\pi} + e^{-i\pi}.$$

Therefore, we get

\begin{equation}
\cos(\phi) = \frac{e^{i\pi} + e^{-i\pi}}{2}.
\end{equation}

For the sine we start with

$$(\cos(\phi) + i\sin(\phi)) - (\cos(\phi) - i\sin(\phi)) = 2i \sin(\phi) = e^{i\pi} - e^{-i\pi}.$$

Therefore, we get

\begin{equation}
\sin(\phi) = \frac{e^{i\pi} - e^{-i\pi}}{2i} = -i\frac{e^{i\pi} - e^{-i\pi}}{2}.
\end{equation}
