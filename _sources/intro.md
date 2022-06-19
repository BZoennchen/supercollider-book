# Introduction

I discovered the world of algorithmic composition and sound design using code in late 2021.
It all started when I watched an energetic and really motivated Sam Aaron presenting his [Sonic Pi](https://github.com/sonic-pi-net/sonic-pi).
I was immediately hooked, especially given the context: educational live programming for kids!

I started experimenting with Sonic Pi.
However, soon after playing around with it, I wanted to write my own synths for which it is unsuitable.
Sonic Pi is perfectly suitable for sequencing your synth and samples but not so much for creating new exciting instruments.
You create your synth and samples beforehand and then use Sonic Pi to play with them.

I digged deeper and discovered other interesting tools such as [TidalCycle](https://github.com/tidalcycles/Tidal), [FoxDot](https://foxdot.org/) and, of course, [SuperCollider (SC)](https://supercollider.github.io/).
I am surprised that I never heard about SC, even if it matured a long time ago, and there seems to be no natural alternative.
Compared to Sonic Pi, SuperCollider has a much steeper learning curve.
The language has some awful-looking syntax; it is less accessible, but at the same time, SuperCollider is much more extensible and powerful.

I fell in love with SC.
The language offers fascinating concepts that keep you thinking about signal-flow processing.
SC supports features well known in modern languages such as ``Python``and rather old languages.
The IDE feels pretty modern and supportive.
The documentation is decent, and the community is healthy.
SC is a powerhouse for discovering new exciting sounds.
It can be a driving force for learning sound design on a deep level.

It is time for me to learn more about *algorithmic compositions* and *sound design*.
What better way to get started than doing what I may be best at: coding.
Being creative by producing sound was the essential puzzle I was always looking for -- a strong connection between computer science and art.

## Personal Background

From the bottom of my heart, I am a computer scientist.
But I may have to clarify my interpretation of the term.
I mean computer scientist in the sense of studying. 

+ **information:** what is information, and how can we create, manipulate and interpret it?
+ **computation:** what is computable, and what do we mean by that?
+ **formal methods:** what can we express, and what do we need to express it?
+ **algorithms** and **data structures:** what can we build?

After school, I did practical training as a software developer.
I worked for four years in the industry.
Then, in desperation, I finished an additional year in school and finally started studying computer science.
I finished my Bachelor's degree in 2013, my Master's in 2017, and my Ph.D. in 2021.
In my Ph.D. thesis, I analyzed different microscopic simulation models for pedestrian streams and developed algorithms to simulate many pedestrians in a large area faster than in real-time.
During my time as a Ph.D. candidate, I enjoyed teaching.
Today, I am a software developer for University that focuses on tools to support our education.
Furthermore, I try to influence the content as well as the structure of our lectures in a positive way.

For other computer scientists interested in the topic of this book, it might be interesting to know which programming experience I had at the time of writing it.
I am very experienced in ``Java``.
Furthermore, I developed an introductory course for ``Python``.
I am also familiar with ``JavaScript``, ``PHP``, ``Scala``, and ``Go``.
Furthermore, I can read and understand ``C\C++`` code, but I am not very experienced in it.
I am familiar with GPU programming using ``OpenCL``.
Currently, I am trying to learn some ``Rust``.

I am not a musician. I have no music theory education and do not play an instrument.
So this is a solid contrast to other great contributors, such as [Eli Fieldsteel](https://www.elifieldsteel.com/).
However, I am a big music lover, and I have always wanted to make my own music and never thought programming could lead me to this goal.

## Notes on Technology

In my opinion, technology should not be trusted naively.
Technology is neither inherently good nor bad -- it can be used for the good, the bad, the ugly, and the beautiful.
We must rethink technology as something that, like nature, is not strictly separated from us.
Technology shapes our way of communication; it opens up spaces of possibilities but, at the same time, closes the door to preexisting ways of life.

For example, the introduction of cars influenced how we plan and build cities and, consequently, made possessing a car mandatory in many areas.
E-Mail changed our communication ethics at the workplace, it made the interaction with E-Mails mandatory.
I see it as a privilege that my generation was one of the last growing up in an internet-free world.
Today, children are confronted with a world of spectacle distractions.

Massively widespread technology has this dictating ability -- once established, it dictates our way of communication.
It shapes our mundane life, and if we want to live within society, we can not escape it.
We live in an *age of disruption* where technology escapes any deep analysis because it evolves faster than we can blink.
The danger is never to stop hustling.
We need spaces that help us not to escape but to **really** engage with technology!
To understand how it affects us, how it changes us, how it can help us and how it might destroy us.

We get used to the internet, smartphones, social media, and other platform economies, and endless repetition of the trivial.
As an individual, we seem powerless concerning new technologies.
If there is a market, we most certainly have to get used to yet another technological phantasy.

I neither advocate for the denial nor for embracing technology in general.
Instead, I advocate for an ongoing evaluation of all the different technologies.
Are they emancipatory?
How do they change our way of thinking, feeling, and communicating?
Are they useful?
What space do they open up?
Do they offer artistic potential?
What realities do they destroy?
I advocate for a culture of conscious engagement -- a society of aware agents within the realm of technology.
A potent society should have the power to reject technological advances in favor of cultural progress.

I believe technology is always destructive as well as creative.
It disrupts existing spaces and opens up new ones. 
The artist's responsibility is to reveal and explore this process.
Neither being prejudiced nor playing the devil's advocate but engaging with technology honestly.
The digital is here to stay.
So let us engage with it, honestly.

>Digital is not here to put an end to anything. Rather it is here to expand all things, to combine and to make more things attainable. For the artist, it is the edgiest work of all; the biggest, most exciting challenge in a long history of the synthesis between technology and hand and mind and heart. -- J.D. Jarvis


## Why Writing a Book?

I am very excited!
I want to learn more about the *algorithmic composition*. 
This book is my attempt to do so; nothing more and nothing less (for now at least).
To understand something, one has to pass through a grueling learning process.
One such strategy that works for me is called *the Feynman learning technique*.
It consists of the following steps:

1. pretend to teach a concept you want to learn about to a student in the sixth grade
2. identify gaps in your explanation. Go back to the source material to understand it better
3. organize and simplify
4. transmit (optional)

This book is my attempt to follow *Feynman's technique* imperfectly.
In the end, someone else might find valuable ideas in this book.
Currently, I focus solely on [SuperCollider](https://supercollider.github.io/) and *sound design*. 

## Source Code

The source code of the Jupyter-Book can be found inside one of [GitHub](https://github.com/BZoennchen/supercollider-book) repositories.
The book is currently published using [GitHub-Pages](https://bzoennchen.github.io/supercollider-book/intro.html).

## The Nature of an Online-Book

I experiment with SuperCollider and other tools and write this book in my spare time. 
It is a hobby. 
Therefore, I will develop and update it over time.
It is only a skeleton in its current state, and I will add new chapters and edit old ones. 
Therefore, do not expect anything professional.

In the future, you might be interested in extending the book with your content. 
Maybe this project will become a community effort to make SuperCollider, sound design, and other tools and techniques more accessible.

Another thing I am looking forward to is combining the book with a Jupyter-Kernel for SuperCollider such that the book becomes interactive.

## Silent Contributors

I want to emphasize that this book is a mixture of my discoveries filtered and altered by my mind.
The creators of my discoveries and the content of the materials I studied are silent contributors.
Without the already existing material, I would not be able to learn either SuperCollider or sound design. 

A special thank goes to [Eli Fieldsteel](https://www.elifieldsteel.com/), who provides multiple excellent courses for [SuperCollider](https://supercollider.github.io/) openly and for free via his [YouTube-Channel](https://www.youtube.com/user/elifieldsteel). 

In the following, I list all the material I looked into:

1. [SuperCollider Online-Course](https://www.youtube.com/user/elifieldsteel) by Eli Fieldsteel {cite}`fieldsteel:2021`
2. [Musical Sound Design in SuperCollider](https://www.youtube.com/channel/UCypLRZiSlIQjsT_7J4Vz35Q) by Alik Rustamoff {cite}`rustamoff:2021`
3. [A Gentle Introduction into SuperCollider](https://scholarcommons.scu.edu/faculty_books/91/) by Bruno Ruviaro {cite}`ruviaro:2014`
4. [SuperCollider Tutorial](https://composerprogrammer.com/teaching/supercollider/sctutorial/tutorial.html) by Nick Collins {cite}`collins:2004`
5. [The SuperCollider Book](https://mitpress.mit.edu/books/supercollider-book) by many {cite}`wilson:2011`
6. [Synth-Secrets Series](https://www.soundonsound.com/series/synth-secrets) by Gordon Reid {cite}`reid:2021`
7. [Computer Music in SuperCollider 3](https://www.e-booksdirectory.com/details.php?ebook=10110) by David Michael Cottle {cite}`cottle:2006`
8. [Introduction to SuperCollider](https://www.logos-verlag.de/cgi-bin/engbuchmid?isbn=4017&lng=eng&id=) by Andrea Valle {cite}`valle:2016`
9. [Fundamentals of Music Processing](https://link.springer.com/book/10.1007/978-3-319-21945-5) by Meinard Müller {cite}`mueller:2015`
10. [Musimathics](http://www.musimathics.com/) by Gareth Loy {cite}`loy:2006`