# Abstract and Physical Synthesis

Before we are diving into the topic of sound design via sound synthesis it is worth to mention that there are two distinct methods for sound synthesis:

1. abstract digital sound synthesis, and
2. physical modeling.

In abstract digitial sound synthesis we try to synthesis sound by focusing **perception** while in physical modeling we focus on the **phyisical world** (objects and their properties) and try to model them via, e.g., differential equations.

The advantage of physical modeling is that we have well interpretable parameters.
Therefore, it is much easier for the composer to generate the sound she desires.
In contrary, abstract synthesis such as [additive synthesis](sec-additive-synthesis), [substractive synthesis](sec-filters) or [frequency modulation](sec-fm) lack this interpretability.
Furthermore, these methods often require thousand of parameters to generate interesting sounds which makes it hard to control them or to explore high-dimensional space of they span.
However, the downside of *physical modeling* is that it requires a lot of computation.
For example, in *FM synthesis* we achieve a rich sound by using only two oscillators, which is computational cheap.
To generate the same richness using *physical modeling* requires much more operations.

The following techniques fall under the category of *abstract digital sound synthesis*:

+ [additive synthesis](sec-additive-synthesis)
+ [subtractive synthesis](sec-filters)
+ [amplitude modulation](sec-am)
+ [frequency modulation](sec-fm)

Using *abstract modeling* we try to construct what we want directly and in *physical modeling* we try to create a model of 'the world' that is capable of generating what we want.