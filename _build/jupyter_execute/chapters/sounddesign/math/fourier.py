#!/usr/bin/env python
# coding: utf-8

# (sec-fourier)=
# # Spectral Analysis and Synthesis
# 
# Given the signal $y(t)$ of a played piano key, how can we compute the pitch and how can we recreate that sound?
# Spectral analysis and synthesis gives us some answers.
# It combines two representations of sound:
# 
# 1. **Inverse Fourier transform**: a signal in the time domain $y(t)$
# 2. **Fourier transform**: a signal in the frequency domain $Y(f)$
# 
# ## Fourier Synthesis
# 
# *Jean-Baptise Joseph Fourier* discovered the following truely remarkable insights to our knowledge of waveforms in general and music in particular.
# 
# ```{admonition} Fourier Theorem (Synthesis)
# :name: theorem-fourier-synthesis
# :class: theorem
# Any periodic vibration, no matter how complicated it seems, can be built up from sinusoids whose frequencies are integer multiples of a fundamental frequency, by choosing the proper amplitudes and phases.
# ```
# 
# I find this result still fascinating.
# The process of constructing a periodic function by a *Foruier series* is called *Fourier synthesis*.
# 
# ```{admonition} Fourier Series (FS)
# :name: def-fourier-series
# :class: definition
# A *Fourier series* is a sum that represents a *periodic function* as a sum of *sine* and *cosine* waves.
# The frequency of each wave in the sum is an integer multiple of the periodic function's fundamental frequency.
# ```
# 
# *Fourier series* can only represent periodic functions.
# In [additive synthesis](sec-additive-synthesis) we use *Fourier synthesis* to construct complicated waveforms from a sum of simple sinusoids, i.e., a *Fourier series*.
# For example, the (periodic) [sawtooth wave](sec-sawtooth-wave)
# 
# ```{math}
#     y_\text{saw}(t) = A \cdot 2 \left( f \cdot t -  \left \lfloor{ \frac{1}{2} + f \cdot t} \right \rfloor  \right),
# ```
# 
# can be constructed by an infinite sum
# 
# ```{math}
#     y_\text{saw}(t) = A \left( \frac{1}{2} - \frac{1}{\pi} \sum_{k=1}^{\infty} (-1)^k \frac{\sin(2\pi k f t)}{k} \right).
# ```
# 
# In fact, we can extend Fourier's result to functions that are  
# 
# 1. **piecewise continuous** and
# 2. **bounded**
# 
# by using an infinite period!
# 
# ## Fourier Analysis
# 
# Fourier also observed that the process works in reverse.
# 
# ```{admonition} Fourier Theorem (Analysis)
# :name: theorem-fourier-analysis
# :class: theorem
# Any periodic vibration, no matter how complicated it seems, can be observed to be made up of a set of sinusiods whose frequencies are harmonics of a fundamental frequency, with particular amplitudes and phases.
# ```
# 
# In *Fourier analysis* we decompose functions depending on space or **time** into functions depending on spatial frequency or **temporal frequency**.
# It provides a way to measure the strengths of individual components of a harmonic signal.
# It starts with a time domain signal $y(t)$ and interprets it as a kind of recipe describing the spectral components and their strength that must be combined in order to preduce the corresponding frequency domain signal $Y(f)$.
# 
# ## Fourier Transform
# 
# The *Fourier transform* is the combination of *Fourier analysis* and *Fourier synthesis*.
# Together they are called a *transform pair* because (ideally) the spectrum of a wave created by *Fourier synthesis* may be perfectly analyzed by *Fourier analysis*, and vice versa, with no loss of information.
# A transform is just a way to represent the same information in an equivalent form.
# I call the tuple $(y(t), Y(f))$ the *Fourier transform*.
# However, sometimes we refer to $Y(f)$ as the *Fourier transform*.
# 
# ## Similarity of Periodic Functions
# 
# Let us assume Fourier is right, i.e. we can reconstruct any *piecewise continuous* and *bounded* function $y(t)$ by an infinite sum of *sine* and *cosine* waves, i.e.
# 
# $$y(t) = \sum_{k=1}^\infty A_k \sin(2\pi \cdot (f_k t - \alpha_k)) + B_k \sin(2\pi (f_k t - \beta_k))$$
# 
# Computing *sinusoidals* that are similar to $y(t)$ seems to be a good idea.
# Functions are similar if their product result in a positive function.
# In other words, if the integral of their product is positive.
# 
# ```isc
# ( // generate the y(t) * sin(2*pi*u)
# {[
#     SinOsc.ar(1) * SinOsc.ar(1), 
#     LFSaw.ar(1) * SinOsc.ar(1),
#     SinOsc.ar(1) * SinOsc.ar(1,0.5*pi),
#     LFTri.ar(0.5)*(-1)*SinOsc.ar(1)
# ]}.plot(1)
# )
# ```
# 
# ```{figure} ../../../figs/sounddesign/math/sin_product.jpeg
# ---
# width: 800px
# name: fig-sin-product
# ---
# Product $y(t) \cdot \sin(2\pi t)$ for different $y(t)$.
# ```
# 
# Let 
# 
# $$y(t) = \sum_{k=1}^8 \frac{1}{k}\sin(2\pi \cdot k \cdot t)$$
# 
# and let 
# 
# $$g_k(t) = y(t) \cdot \sin(2\pi \cdot k \cdot t).$$
# 
# ```isc
# ({
#     var sines = Array.fill(8, {arg i; 1/(i+1) * SinOsc.ar(i+1);});
#     var y = Mix(sines);
#     [y]++Array.fill(8, {arg i; y*SinOsc.ar(i+1)});
# }.plot(1)
# )
# ```
# 
# ```{figure} ../../../figs/sounddesign/math/saw_analysis.jpeg
# ---
# width: 800px
# name: fig-saw-analysis
# ---
# Multiplying functions: $y(t)$ in the upper left corner. In blue $\sin(2\pi \cdot k \cdot t)$, in orange the product $g_k(t)$ and in green the integral $\int_{0}^t g_k(t) dt$.
# ```
# 
# We get
# 
# $$\int_0^1 g_1(t)dt = \frac{1}{2}, \int_0^1 g_2(t)dt = \frac{1}{4}, \int_0^1 g_3(t)dt = \frac{1}{6}, \int_0^1 g_4(t)dt = \frac{1}{8}, \ldots$$
# 
# In general we get
# 
# ```{math}
#     \int_0^1 g_k(t)dt = \frac{1}{2k}.
# ```
# 
# Note that $\forall k \in \mathbb{N}$
# 
# $$\int_0^1 \sin(2\pi \cdot k \cdot t)^2 dt = \frac{1}{2}$$
# 
# holds, thus
# 
# $$\int_0^1 \frac{1}{k}\sin(2\pi \cdot k \cdot t)^2 dt = \frac{1}{k} \int_0^1 \sin(2\pi \cdot k \cdot t)^2 dt = \frac{1}{2k}.$$
# 
# Therefore,
# 
# $$\int_0^1 g_k(t) dt = \frac{1}{k}\int_0^1 \sin(2\pi \cdot k \cdot t)^2 dt$$
# 
# If we look at the integral of 
# 
# $$h_k(t) = \left( y(t) - \frac{1}{k}\sin(2\pi \cdot k \cdot t) \right) \cdot \sin(2\pi \cdot k \cdot t)$$
# 
# then $\forall k \in \mathbb{N}$
# 
# $$\int_0^1 h_k(t) dt = \int_{-\infty}^\infty h_k(t) dt = 0.$$
# 
# In fact, if we look at $h_{i,j}(t) = \sin(2\pi i \cdot t ) \cdot \sin(2\pi j \cdot t)$ 
# 
# ```{math}
# :label: eq:perp:sines
# \begin{split}
# \forall i,j \in \mathbb{N}, i \neq j: \int_0^1 h_{i,j}(t) dt &= \int_{0}^1 h_{i,j}(t) dt = 0\\
# &= \int_{-\infty}^\infty \sin(2\pi i \cdot t) \cdot \sin(2\pi j \cdot t ) dt\\
# &= \int_{-\infty}^\infty h_{i,j}(t) dt
# \end{split}
# ```
# 
# holds.
# 
# ```{admonition} Perpendicular Functions
# :name: theorem-perp-sine
# :class: theorem
# 
# For all $i,j \in \mathbb{N}$ with $i \neq j$ 
# 
# $$\int_0^1 \sin(2\pi i \cdot t) \cdot \sin(2\pi j \cdot t ) dt = \int_{-\infty}^\infty \sin(2\pi i \cdot t) \cdot \sin(2\pi j \cdot t ) dt= 0$$
# 
# holds. We say that $\sin(2\pi i \cdot t)$ is *perpendicular* to $\sin(2\pi j \cdot t)$.
# ```
# 
# ```isc
# ({ // generate sin(2*pi*i*x) * sin(2*pi*j*x)
#     var sines = Array.fill(3, {arg i; 1/(i+1) * SinOsc.ar(i+1);});
#     var y = Mix(sines);
#     var indices = Array.fill2D(3, 3, {arg row, col; [row,col];}).flatten;
#     indices.collect({arg index; var i = index[0], j = index[1];
#         SinOsc.ar(i+1)*SinOsc.ar(j+1)
#     });
# }.plot(1)
# )
# ```
# 
# ```{figure} ../../../figs/sounddesign/math/sine_perp.jpeg
# ---
# width: 800px
# name: fig-sine-perp
# ---
# $\sin(2\pi i \cdot t )$ in blue, $\sin(2\pi j \cdot t)$ in orange and $h_{i,j}(t)$ in green.
# ```
# 
# We say that these functions are **perpendicular** to each other because their scalar product (the integral of their product) is zero!
# 
# One way to compare two vectors $\mathbf{a} = (a_1, \ldots, a_n)$ and $\mathbf{b} = (b_1, \ldots, b_n)$ is to compute their *inner product*.
# If two vectors $\mathbf{a}, \mathbf{b}$ are perpendicular, i.e., if they are very different, their *inner product* 
# 
# $$<\mathbf{a}, \mathbf{b}> := \sum\limits_{i=1}^n a_i \cdot b_i$$
# 
# is zero.
# Their inner product is large if they are similar.
# We can define the inner product of two functions $h: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$ in a similar fashion.
# The sum changes to an integral.
# 
# ````{admonition} Inner Product of Two Functions
# :name: def-scalar-product
# :class: definition
# 
# Let $h: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$ then 
# 
# ```{math}
# :label: eq:inner:product
#     <h,g> := \int_{t \in \mathbb{R}} h(t)g(t) dt
# ```
# is the inner product of $h$ and $g$.
# ````
# 
# We can reformulate the problem of similarity using an optimization problem.
# Let us start with an analog signal first.
# And let us consider the basis for all possible audio signals, i.e., the **sinusoid** which is a function $\sin_{f,\phi} : \mathbb{R} \rightarrow \mathbb{R}$ defined by 
# 
# ```{math}
# :label: eq:sinusoid
#     \sin_{f,\phi}(t) = A \cdot \sin(2\pi(f t - \phi))
# ```
# 
# for $t \in \mathbb{R}$.
# As we know, the parameter $A$ corresponds to the **amplitude**, the parameter $f$ to the **frequency** (measured in Hz), and the parameter $\phi$ to the **phase** (measured in normalized radians with 1 corresponding to an angle of 360 degrees).
# 
# In the *Fourier analysis*, we consider prototype oscillations that are normalized with regard to their power (average energy) by setting $A = \sqrt{2}$.
# Thus for each frequency parameter $f$ and phase parameter $\phi$ we obtain a sinusoid $\cos_{f,\phi}: \mathbb{R} \rightarrow \mathbb{R}$ given by
# 
# ```{math}
# :label: eq:sinusoid:norm
#     \cos_{f,\phi}(t) = \sqrt{2} \cos(2\pi(f t - \phi)) = \sin_{f,\phi+1/2}(t)
# ```
# 
# for $t \in \mathbb{R}$.
# Note that we get the same function for all $\phi + k$ with $k \in \mathbb{Z}$.
# 
# To model a signal $y(t)$ by $\cos_{f,\phi}(t)$, we want to find the best parameters $f, \phi$ such that we get the *best approximation* of $y(t)$.
# In other words, we are searching for $f, \phi$ such that $y(t)$ and $\cos_{f,\phi}(t)$ are *most similar*.
# 
# For a fixed frequency $f \in \mathbb{R}$, we define
# 
# ```{math}
# :label: eq:fourier:max
#     d_f := \max\limits_{\phi \in [0;1)} \left( \int_{t \in \mathbb{R}} y(t) \cos_{f, \phi}(t) dt \right) = \max\limits_{\phi \in [0;1)} <y,\cos_{f, \phi}> 
# ```
# 
# ```{math}
# :label: eq:fourier:maxarg
#     \phi_f := \arg\max\limits_{\phi \in [0;1)} \left( \int_{t \in \mathbb{R}} y(t) \cos_{f, \phi}(t) dt \right) = \arg\max\limits_{\phi \in [0;1)} <y,\cos_{f, \phi}> 
# ```
# 
# where $d_f$ is the magnitude coefficient expressing the intensity of frequency $f$ within the signal $y(t).$
# Additionally, the phase coefficient $\phi_f \in [0;1)$ tells us how the sinusoid of frequency $f$ needs to be displaced in time to best fit the signal $f$.
# In the example above we knew that for all frequencies $\phi = 0.5$ holds.
# Furthermore, we knew all the frequencies $f$ such that $<y,\cos_{f, \phi}> = 0.$
# If we would have used $A = \sqrt{2}$ instead of $A = 1$, the coefficient would have been $\frac{1}{\sqrt{2}k}$ instead of $\frac{1}{2k}$.
# 
# The **Fourier transform** $(y(t), Y(f))$ is a tuple conistent of a function $y: \mathbb{R} \rightarrow \mathbb{R}$ and the collection $Y(f)$ of all coefficients $d_f$ and $\phi_f$ for $f \in \mathbb{R}$.
# 
# ## TODO
# 
# However, non-periodic functions can be handled using an extension of the [Fourier series](def-fourier-series) called *Fourier transform* which treats non-periodic functions as periodic with infinite period.
# The transform decomposes functions depending on space or **time** into functions depending on spatial frequency or **temporal frequency**.
# This process is called *Fourier analysis*.
# 
# ```{admonition} Fourier Theorem
# :name: theorem-fourier-1
# :class: theorem
# Any *piecewise continuous* and *bounded* function, can be represented by a *Fourier transform*.
# ```
# 
# In theory, the *Fourier series* of many functions consists of infinitely many terms.
# Still, since our hardware resources are finite, we can only generate an approximation of the real thing.
# 
# 
# 
# 
# The Fourier transformation computes another representation of the audio signal called *Fourier transform*.
# Instead of representing the sound by a signal, i.e., amplitudes $y(t)$ over time $t$, the Fourier transform represents the sound by frequency magnitude $d(f)$ over frequencies $f$.
# 
# While the signal displays the information across time, the Fourier transform displays the information across frequencies.
# The signal tells us when certain notes are played in time, but hides the information about frequencies.
# In contrast, the Fourier transform of music displays which notes (frequencies) are played, but hides the information about when the notes are played.
# 
# 
# 
# 
# 
# 
# 
# For example, 
# 
# $$\int_{0}^1 \cos_{1,0}(t)\cos_{1,0.5}(t) dt = -1$$
# 
# and
# 
# $$\int_{0}^1 \cos_{1,0}(t)\cos_{1,0.25}(t) dt = 0$$
# 
# while 
# 
# $$\int_{0}^1 \cos_{1,0}(t)\cos_{1,0}(t) dt = 1.$$
# 
# If the term perpendicular is defined via the inner product one can say that $\cos_{1,0}$ is perpendicular to $\cos_{1,0.25}$.
# Furthermore, $\cos_{1,0}$ and $\cos_{1,0.5}$ are very similar but they point in the opposite direction.

# In[1]:


# test
3+4
def test(arg):
    return true and arg


# However, we will see later that an infinite period can be introduced.
