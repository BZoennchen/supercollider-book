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

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd

import numpy as np
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
import matplotlib.pyplot as plt
import scipy.special
import seaborn as sns

dpi = 300
transparent = True
PI = np.pi
TWO_PI = 2*PI
NUM = 44000
show = False

sns.set_theme('talk')
sns.set_style("whitegrid")
```

(sec-medium-and-form)=
# Medium and Form

>There is neither a medium without form nor a form without medium.
>The difference of mutual dependency and independency is pivotal. -- Niklas Luhmann {cite}`luhmann:1986`

What is art, and what qualifies a creation as a work of art? 
Even without a formal education in art history or aesthetics, I find this question compelling.
In my view, good art communicates an ineffable truth about our existence.
It challenges and disrupts by offering a glimpse into what we may call infinite or illusionary.
In the presence of the truly transcendent, we stand in awe, feeling both a sense of relief and a profound connection to the essence of being.
This description may be a vague articulation of a sensation, but that is precisely the point: The essence of what art means to me is beyond the confines of language.

The German sociologist Niklas Luhmann gives us a rather abstract but helpful analysis of art by relating it to his concept of *medium* and *form* inspired by Fritz Heider.
According to him, a medium consists of a large number of elements or, in the context of time, events.
There are so many elements within a medium that cognition must necessarily operate by selection.
The term *element* should not be mistaken for natural constants like particles or souls, which can be objectively observed. 
Instead, elements are units that are constructed---distinguished by an observing system.
Moreover, these elements cannot determine themselves; they are subjected to what is known as *coupling*.
Forms, conversely, arise through the concentration of dependency relations between elements, which the medium itself must support. 
It is the *loose coupling* and *separability* of a medium's elements that lead to the emergence of form. 
We do not perceive the medium itself, but rather the form which coordinates elements within the medium.

Luhmann's constructivism replaces concepts of inside and outside, of object and subject, with the distinction between medium and form, which is always constructed by a system. 
Medium and form require a system reference; without it, they do not exist.
They are not things in themselves.
Like information, they are a product internal to the system. 
Furthermore, there is no medium without form and no form without medium---a medium can only be recognized by the contingency of form construction (Formbildung) it enables.
The loose coupling of a medium's elements refers to the wide range of possible relations or connections that are still compatible with the unity of an element, for example, the number of sensible sentences that can be formed from a given word.

Luhmann's constructivism replaces the thing-oriented or thing-ontological differentiation of an inside and outside, of object and subject with the **distinction** of medium and form which is always constructed by a system.
Medium and form require a systemreference without they do not exist.
They are not *things for themselves*!
Like information they are a systeminternal product.
The loose coupling of elements of a medium refers to an open majority of possible relations or connections which are still compatible with the unit of an element, e.g. the number of sensible sentences which can be formed by a given word.

Luhmann defines medium in relation to form, i.e., relatively.
Therefore, forms can be the medium of a new form.
A *medium* is any set of loosely coupled elements that, if rigidly coupled, build a *form*.
Only by the detour of observing the form, can an observer relate to the medium.
The form catches attention and refers to the medium.
We can ask: How came this form into being?

Sound is the form of air.
It is literally the compression (rigid coupling) of air molekules our ear perceives.
And when the air is too thin, we recognize it because the creation of the form fails---no sound can be perceived.
In Luhmann's contructivist framework, sound requires a listener.
In other words, if a tree falls down in the deep forest and no one is listening, then the event won't make a sound.
Air will be compressed and a wave, that is, energy will travel from the event through the air but there will be no sound.

The relation between form and its medium is selection.
For example, a sentence is a selection from a language, i.e., its medium.
A computer program is a selection from a programming language.
A painting is a selection from the domain of all possible color arrangements.
A performance is a selection from all possible played tones, and each played tone is a form of the air.
Importantly, everything which is not there, i.e. everything what could be different, is also present as *unmarked space*.

From a point of information theory {cite}`shannon:1948`, a form reduces the entropy of its medium.
It reduces the number of possible connections.
Each drawn stroke, each played note, each move in a performance reduces the possibilities of what can be drawn, played, or performed next.
The *horizon of the possible* gets narrowed down.
Similar to Heidegger's understanding of a craftsman, the artist brings the medium into form and the medium 'uses' the artist to become a form.
The artist might has an idea of the final work but the process of making and shaping it inevitable influences the process itself---it is a contingency.
We can say that every artwork is **contingent**; other fixations, combinations and recombinations, that is, other forms of the medium would alse have been possible.
In its final stage, the artwork is confronted by the expectation of the audience and it has to convince---it has to make sense under the assumption of its contingency.
The audience knows that the artwork could have been different, and so it asks: Why is it this way? What does it mean? What is the intention of the artist?
Its singularity aspiration will be investigated and it has to stand its ground against other works of art and other possible realizations within their medium.
Critics will judge the artwork and the market will determine if they were right.

Luhmann is not so much interested in historical or cultural *horizons of the possible* but he asks a more general question:

>What is art beyond certain culturalistic, stylistic dependencies and genres?

But to answer this general question, in a typical Luhmannian fashion, he uses a very abstract framework:

>Artworks are not just traces of human activity [...].
>Neither do they arise as simple relicts of purposeful behavior like tools, houses, streets or radioactive radiation.
>They serve [...] as transmission of sense. -- Niklas Luhmann

A medium cannot take on any form but only those which can be composed by its elements.
The medium conditions its forms.
Fater all, form and medium share the same elements.
The difference consists solely in the loose and rigid coupling of elements.
How the medium passes the form to its elements depends on the properties of the medium itself.
The medium opens the possibilities of giving form and it also narrows it down.

The elements of a medium are rather independent.
For example, the color of a pixel of an image is technically independent of the colors of all other pixels.
Only because of this property can images picture almost anything.
We can arrange pixels as we desire.
Money is a medium since payments can be made in almost any denomination and they are independent of the sense and means of other payments.
Each letter in a programming code is inpdependent of any other letter.
Of course, similar to natural languages, only a small subset of programming code make sense, i.e. form a valid program that can be compiled, interpreted or executed.
Interestingly, the medium is very oblivious and the artist can utilize this property of the medium to manipulate the form.
The low interdependency of the medium's elements opens a space of fiction and simulation---of stories about unicorns.

In the relation between medium and form, the more rigid form prevails because it is less movable.
However, this is a risky endeavor for the form.
It might decay or, if it is reproducible, evolve.
Within forms, this assertive property repeats.
Sand adjusts to the stone, not the other way around.

According to Luhmann, a form can create a medium, Luhmann refers to a *second-order medium*.
Sound is a form of air but tones, which are sound, make up the medium of music.
We could also say that rhythyms (medium) make up a sound (form/medium) which can make up rhythyms (form).
Compare the following three sounds.
The first one is a rhythym, by increasing the frequency of the rhythym it turns into an infinite tone and by manipulating the amplitude of the tone, we arrive at a rhythym.

```isc
{Impulse.ar(5)!2}.play
{Impulse.ar(160)!2}.play
{Env.perc().ar(gate:Impulse.ar(1)) *  Impulse.ar(160)!2}.play
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/impulse_5_hz.mp3'
ipd.Audio(audio_path)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/impulse_160_hz.mp3'
ipd.Audio(audio_path)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/impulse_impulse.mp3'
ipd.Audio(audio_path)
```

In a musical piece, any tone can, in principle, follow or can be combined with any other tone except the form of the music piece "decides" otherwise.
Importantly, music functions as communication only for those who can recognize (and inform each other about) the difference between medium and form; only those who can hear the uncoupled space within the played music; only those who listen and recognize that, through its tonality, the music makes much more sounds possible than normally expected but it is disciplined by the form.

>Art establishes rules of inclusion that serves the difference of medium and form as medium. -- Niklas Luhmann

A *(second-order) medium* can be the difference of medium and form.
I think this statement is crucial because it explains why we have certain rules, e.g. music theory, despite art forming a medium to create alternative versions of reality.
These rules are contingent, that is, they could be very different but they are necessary to mark the outside (and with it the inside).
Rules exclude and include at the same time thus establish the possibility of making a difference.
What we call objects are in fact differences.
*Differentiation* and *indication* go hand in hand {cite}`brown:1969`.
Pointing to a chair and calling it 'chair' is not a representational operation in the sense that we are naming an object.
Instead it is an act of *differentiation* and *indication*---there are no objects, only differences.
A form might establish a medium of art by using it for the purpose of expression.
In other words, the difference between medium and form can function as a medium.
It can be the *released possibility* for the combination of mediums and forms for the forming through *communication*.
The more rigid form forces through greater flexibility but it is at risk of failing, it can be criticized, surpassed, or put into the museum.

Luhmann further argues that the art system (as a social system), like any social system, differentiates itself from its environment.
It is no longer part of religion or politics but does its own thing on its own terms.
In the cold world of functional differentiation, it serves a specific and unique function within society.
This naturally leads to the question of what function the art system actually fulfils?
A question we cannot answer here.

However, we can point out a precondition for the functional differentiation of the art system, that is, *second-order observation*.
One has to be able to observe what others observe.
Through second-order observation, the concrete bond between observer and artwork "as it is" dissolves.
An artwork signals to the observer that it earns attention.
If you observe an artwork, you can speculate about the artist's intention.
You can observe that others have their interpretation and you know that they know that you know about this fact.
They know that you can observe their interpretation and they can observe yours.
At the same time, the artist is aware of this too and it might prompt the artist to talk about her work.
Communication about works of art and the artwork itself are interdependent.
There is no art without communication and one can only communicate about art if there is an artwork to talk about.
This strange loop, this self-referential relation, sets the system of art in motion.
In a typical Luhmannian fashion (inspired by Spencer-Brown's concept of *re-entry* {cite}`brown:1969`): the paradox becomes a generator in time!

The constructive liberties of such a social system are solely grounded in communication.
If communication 'happens' everything else is secondary.
Crucial is the condition of symbolic generalization, that is, **the property of the medium to exceed the diversity of things** and the condition of **unification** to enable communication.
If art does not exceed the diversity of things, there is nothing worth communicating about and if there is no unification, sense and language fail as medium of communication---dissolution and recombination enable diversity and the selection of the particular.

Information can only be transmitted if the artwork could be different and *that which is not* is always also indicated by *that which is*.
The artwork fixes all possibilities and we can talk about reasons why it is constructed or performed this way and not any other way.
This seems consistent with the information theory of Claude Shannon {cite}`shannon:1948`.
To communicate about art we have to be aware of these liberties and we have to use them because, again, to gain information one has to eliminate uncertainty---artworks have to surprise us.

By the *re-entry* {cite}`brown:1969` communication about art can become a form of art.
Acknowledging the properties of the medium, events within the system of art have to be loosely coupled and there have to exist plenty of them.
This includes the system of art itself!
Consequently, art will be mocked by observers, exhibitors, buyers, and, in the end, by itself.
Dissolution can become an end in itself thus the medium no longer serves the form but the form serves the medium.
In that stage, form wants to show that it is in fact a medium.
For an observer, this kind of art is paradoxical.
Luhmann remarks that this path is narrow but the consideration of the dissolution of paradoxes can become fruitful.

It is plausible that there are limits to art determined by the limits of "natural" mediums, e.g., what we can see and hear.
But what are the limits of art with respect to society?
If a piece of art shows "facts" realistically, it indicates its flipside, its unmarked space, its contingency: reality could be different.
Therefore, we should be careful to judge the motionless dance, the toneless music, or the empty canvas.
These works of art rely on second-order observation and the re-entry.
But it is a risky business!
Whether these works are recognized as art is contingent.

Can we conclude that the form of art is an artwork?
Luhmann understands the artwork as **communication of order** in a form arrangement which does not happen by itself.
However, art does not utilize the medium to transmit a real order of the real world to the senses.
Instead, art forms its mediums to create a **contingent alternative version of reality**.
It does this by exploring the different possibilities of ordering elements within the medium.
Through art, we can explore new possibilities of the acoustic and optical world and make them available and experiential.
Thereby we gain more non-obvious possible ways of ordering the world.

Here we should ask how an artwork might achieves this effect?
Luhmann uses the concept of the *marked* and *unmarked space* introduced by Spencer-Brown's *Laws of Form* {cite}`brown:1969`.
Looking at the artwork one can see a marked space but also the other side, the unmarked space.
The unmarked space indicate an infinite amount of possibilities which can not be fixed in place.
Beginning an artwork consists of a first step, which leads from an unmarked into the marked space.
This establishes a border by crossing it {cite}`luhmann:1997`.
Luhmann continues by emphasising that the specificity of art forms is based on the fact that the determination of one side does not completely leave open what can happen on the other side. 
It does not determine the other side, but it removes the determination of the other side from whimsy.
What can occur there must fit, if not the impression of a discord, an error, a disturbance is to arise {cite}`luhmann:1997`.

## Code as Form

A computer program can be seen as a collection of commands or statements of advice.
Computer scientists, like me, emphasise the humanist perspective that a programming language is an inherently precise and rigid medium of expression.
Different from natural languages, programming languages are unambiguous.
Any syntactical error will lead to non-execution (compiled code) or an abrubt termination (interpreted code)---the computer stops making sense of the given advice.

From this rigidity and formality, programmers extrapolate the believe that if they can implement something, they really understand it.
The reasoning goes like the following:

1. **Major premise:** Programming languages are unambiguous.
2. **Implication:** Therefore, if one writes a program, it will do something particular
3. **Implication:** Therefore, if the idea that should be realized is vague, i.e., the programmer has no particular result in mind, the program won't do what she or he wants.
4. **Conclusion:** A correct program proofs the clarity of the programmers idea.

It is true that one has to be very precise with respect to syntax.
No spelling or punctuation errors are allowed.
But it is perfectly false that this makes programmers have a precise idea of what their program will do.
It is especially false to assume that programmers just write down their idea from start to finish much like it is false to believe that painters, poets or writers realize their idea from start to finish.
The whole progess is contingent.
Each steps narrows down what can come next.

Look at the following algorithm.
I assume that, for most readers, it is very unclear what the algorithm computes.

```{prf:algorithm} Newton's Algorithm to Approximate $\sqrt{2}$
:label: alg-newton

**Output** Approximation of $\sqrt{2}$

1. $x \leftarrow 2$
2. $r \leftarrow 1$
3. $v \leftarrow 1$

4. While $|v| > 0.001$
    1. $m \leftarrow x / r$
    2. $t \leftarrow r + m$
    3. $r \leftarrow t / 2$
    4. $u \leftarrow r^2$
    5. $v \leftarrow x - u$
5. return $r$
```

Can we unravel the mystery hidden behind the complexity of these statements?
We can see that if $x$ and $u$ are similar, the computatation stops.
Since $u \leftarrow r^2$ and $x = 2$ the computation stops when $r$ is close to $\sqrt{2}$.

How is $r$ computed?
Well, if we substitude all the variables we get

$$r \leftarrow t / 2 \Rightarrow r \leftarrow (r+m)/2 \Rightarrow r \leftarrow \left(r+\frac{x}{r}\right) \cdot \frac{1}{2}$$

and since $x = 2$, we get

$$r \leftarrow \left(r+\frac{2}{r}\right) \cdot \frac{1}{2}.$$

Substituting $r$ for $\sqrt{2}$ gives us

$$r \leftarrow \left(\sqrt{2}+\frac{2}{\sqrt{2}}\right) \cdot \frac{1}{2} = \frac{4}{2\sqrt{2}} = \frac{2}{\sqrt{2}} = \frac{\sqrt{2}^2}{\sqrt{2}} = \sqrt{2}.$$

Therefore, if $r$ would be exactly $\sqrt{2}$ (which is impossible since it is a irrational number) then $r$ would not change.

Let's say $r = (\sqrt{2} \pm \epsilon)$ then we get

$$r \leftarrow \left((\sqrt{2} \pm \epsilon)+\frac{2}{\sqrt{2} \pm \epsilon}\right) \cdot \frac{1}{2}$$

We know that for small $\epsilon$ the sum is close to $2\sqrt{2}$ and each of the summands is close to $0.5\sqrt{2}$.
From the formula we can see that the first summand is about $\epsilon$ larger or smaller than $\sqrt{2}$.
So what about the second summand?
Clearly it is the opposite, i.e., if $\epsilon > 0$ the second summand is smaller than $\sqrt{2}$.

If $r = \sqrt{2} + \epsilon$, we want $r$ to go down thus 

$$\frac{2}{\sqrt{2} + \epsilon} < \sqrt{2} + \epsilon$$

should hold. This follows from the following inequation:

$$2 < 2 + 2\sqrt{2}\epsilon + \epsilon^2 = (\sqrt{2} + \epsilon)^2.$$

On the other hand, if $r = \sqrt{2} - \epsilon$, we want the opposite, thus 

$$\frac{2}{\sqrt{2} - \epsilon} > \sqrt{2} - \epsilon$$

should hold.
This follows from the following inequation, which holds for $\epsilon < 2\sqrt{2}$:

$$2 > 2 - 2\sqrt{2}\epsilon + \epsilon^2 = (\sqrt{2} - \epsilon)^2.$$

If we look at the starting value for $r$ and all the operations, we can clearly see that $r$ will never be negative thus $\epsilon < 2\sqrt{2}$ holds for the execution of the algorithm.

We did a lot of work and thinking to analyse Newton's algorithm.
In the end we figured out that $r$ approches $\sqrt{2}$. 
We still don't know how fast $r$ converges towards $\sqrt{2}$.
We also did not look at possible numerical pitfalls---after all computers are not that good at dealing with the infinite.
It is likely that Newton started with mathematical equations before writing down the statements of advice.
If we just implement the steps without a proper analysis we do not really understand what is going on and simply looking at the algorithm does not help either.

These kind of algorithms echo the humanistic perspective: Humans are in total control by advicing the computer precisely what commands it should execute.
The *form* is the written down algorithm in a specific language (medium), e.g. ``sclang``---the SuperCollider programming language.

```isc
(
x = 2;
r = 1;
v = 1000;
while({abs(v) > 0.001}, 
{
  m = x / r;
  t = r + m;
  r = t / 2;
  u = r * r;
  v = x - u;
});
r.postln; // 1.4142156862745
)
```

```{code-cell} python3
---
tags: 
    - remove-input
mystnb:
  image:
    width: 400px
  figure:
    name: fig-newton-convergence
    caption: The value $r$ converges towards $\sqrt{2}$.
---
steps = []
values = []
step = 1
x = 2
r = 1
v = 1000
while abs(v) > 0.000001:
    steps.append(step)
    step += 1
    m = x / r
    t = r + m
    r = t / 2
    u = r * r
    v = x - u
    values.append(r)
    
plt.figure()
plt.plot(steps, values)
plt.xlabel('iteration step')
plt.ylabel(r'$r$')
plt.yticks([1.5, 1.48, 1.46, 1.44, 2**0.5, 1.40], [1.5, 1.48, 1.46, 1.44, r'$\sqrt{2}$', 1.40]);
plt.xticks([1, 2, 3, 4], [1, 2, 3, 4]);
```

In any programming language, there exists an inherent intelligence.
This is due to the fact that the language allows only a specific range of statements to be syntactically correct, thereby enforcing its own logic. 
The structure and rules of the language dictate how programmers can express commands and algorithms, guiding them to adhere to its logical framework. 
This intrinsic design ensures that programming adheres to a consistent and rational set of principles, which is a fundamental aspect of how these languages function and are understood.

Libraries in programming are repositories of intelligence, created by numerous developers. 
When a large language model (LLM) like ChatGPT solves a problem using ``Python`` code, we should not imply that it understands the problem.
This limitation often also applies to programmers. 
Both scenarios reflect the illusion of having a direct and complete understanding of reality, which is likely impossible.

Programming is almost always a collective, cultural effort. 
In such an environment, it's rare for any single individual to fully grasp every aspect. 
This collaborative nature of programming means that solutions and advancements are often the result of pooled knowledge and shared expertise, rather than the sole understanding or capability of one person.
This reality underscores the interconnectedness and complexity inherent in both programming and our broader attempts to comprehend and interact with the world.

## Artistic Coding

In the realm of artistic or creative coding, the perception of programming as a rigorous and precise activity completely dissolves. 
Here, artists use code akin to a musical instrument. 
For instance, when utilizing creative coding libraries such as [p5.js](https://p5js.org/), [Processing](https://processing.org/) or [nannou](https://nannou.cc/) for visual projects, the process is rarely about transcribing a preconceived idea directly. 
Instead, it begins with something simple: a circle, a line, a loop, or a combination of these elements.

The approach involves tinkering and experimenting, repeatedly running the program to observe how changes affect the visuals. 
This method is more exploratory and iterative, allowing the artist to evolve their work organically through trial and error. 
It's a dynamic process where the outcome is often discovered through the act of coding itself, rather than being strictly planned from the outset.
The artist helps the artwork to come into being.
It is a contigent process.
What comes next depends on the horizon of the possible, i.e. the language, libraries and what is already present.

For me, the allure of (classical) generative art lies in the exploration of simple rules and the emergent complexity produced by repetition and recursion.
One example was a piece for which I limited myself to draw only perpendicular lines.
I start drawing a line and while the line is drawn there is a probability, that another line will be drawn starting at the current endpoint.
This line has to be perpendicular to its parent.
The child can spawn further lines and also the parent can continue to spawn new lines.
Secondly, I mirrowed the emerging tree around a circle.
I had no idea what to expect.
And I played around with the parameters, e.g. probability values, coloring, the number of copies etc.
I found the result impressive because of the simplicity of the rules it depends on.

````{panels}
:container: container-genart 
:column: col-lg-6 col-md-6 col-sm-6 col-xs-12 
:card: shadow-none border-0
:body: bg-panel

```{figure} ../../figs/preamble/red-flake-4.jpg
:width: 100%
:name: example1
```

---

```{figure} ../../figs/preamble/red-flake-5.jpg
:width: 100%
:name: example2
```

---

```{figure} ../../figs/preamble/red-flake.jpg
:width: 100%
:name: example3
```

---

```{figure} ../../figs/preamble/red-flake-2.jpg
:width: 100%
:name: example4
```

````


The concept of exploratory and iterative development in creative coding also applies to the acoustic domain and, notably, to live programming. 
An interesting aspect of live programming is how it exposes the technology behind the artwork, especially when something unexpected occurs and the system 'breaks'. 
In such moments, the distinction between *form* and *medium* becomes clear.

In live programming, the process and the technology used are as much a part of the artistic expression as the final product. 
When glitches or errors occur, they reveal the underlying mechanisms and constraints of the technology, offering a unique insight into the medium itself. This contrast between the artistic intent (form) and the tools and methods used (medium) is a key characteristic of creative coding, highlighting the dynamic interplay between the artist's vision and the technology employed.