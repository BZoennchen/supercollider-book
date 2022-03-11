# Introduction

I discovered the world of algorithmic composition and sound design using code in 2021.
It all started when I watched an enthusiastic and really motivating presentation about [Sonic Pi](https://github.com/sonic-pi-net/sonic-pi) by Sam Aaron.
I was immediately hooked!

However, soon after experimenting with Sonic Pi, I wanted to write my own synth for which it is not really suitable.
I wanted to learn more about actual algorithmic composition and sound design, doing what I may be best at: coding.
Along the way I discovered [TidalCycle](https://github.com/tidalcycles/Tidal), [FoxDot](https://foxdot.org/) and, of course, [SuperCollider](https://supercollider.github.io/).

Being creative by producing sound was the essential puzzle piece I was always looking for -- a strong connection between computer science and art.

## Personal Background

From the bottom of my heart I am a computer scientist.
But I may have to clarify my interpretation of the term.
I mean computer scientist in the sense of studying 

+ information as a resource (What is it and how can we create, manipulate and interpret it?) 
+ computation (What can we compute? What does it mean to compute something?),
+ formal languages (What can we express? What do we need to express it?), and
+ algorithms and data structures

After school I did a practical training as software developer and after working for four years in the industry and finishing all requirements in one additional year, I started studying computer science.
I finished my Bachelor in 2013, my Master in 2017, and my PhD in 2021.
In my PhD thesis I analysed different microscopic simulation models for pedestrian streams and developed algorithms to successfully simulate a large amount of pedestrians within a large area faster than real-time.
During my time as PhD candidate I really enjoyed teaching.
Today, I am a software developer for University who focuses on tools to support our education.
Furthermore, I try to influence the content as well as the structure of our lectures in a positive way.

For other computer scientists interested in the topic of this book, it might be interesting to know which programming experience I have.
I am very experienced in ``Java``.
Furthermore, I developed an introductory course for ``Python``.
I am also familiar with ``JavaScript`` and ``Scala``.
Furthermore, I can read and understand ``C\C++`` code, but I am not very experienced in those languages.
I am familiar with GPU programming using ``OpenCL``.

From a musical perspective I know almost nothing.
So this is a strong contrast to other great contributors such as [Eli Fieldsteel](https://www.elifieldsteel.com/).
However, I am a big music lover and I always wanted to make my own music and never thought that programming can lead to this goal.

## Notes on Technology

In my opinion technology should not be trusted naively.
Technology is not inherently good or bad -- it can be used for the good, the bad, the ugly and the beautiful.
We have to rethink technology as something that, like nature, is not strictly separated from us.
Technology shapes our way of communication, it opens up spaces of possibilities, but at the same time closes the door to preexisting ways of life.
The introduction of cars influenced how we plan and build cities and, consequently, made the possession of a car mandatory in many areas.
E-Mail changed our communication at the working place, it made the interaction with E-Mails mandatory.

Technology has this dictating ability -- once established it dictates our way of communication.
If we want to live within society, we can not escape technology.
By not using or developing a new technology, we are dictated by others.
We, as a collective, can only choose which technology should shape our communication and how we interact with it.
On an individual level, we can only try to reduce or increase our dependence but at least we can be a conscious agent in the realm of technology.

Neither do I advocate for the denial nor for the embracing of technology in general.
Instead I advocate for an ongoing evaluation of all the different technologies.
Are they emancipatory?
How do they change our way of thinking, feeling and communicating?
Are they useful?
What space do they open up?
Do they offer artistic potentials?

I believe technology always opens up a space and the artist basically explores this space.
Take pen and paper.
We can imagine the infinite space of all drawings possible and it is the artist who discovers drawings and we, the audience, attach meaning to a piece of art.
Therefore, for me digital art is as real as non-digital art and with respect to my caution regarding technology, it is the artist who has to explore the new spaces technicians open up. 

>Digital is not here to put an end to anything. Rather it is here to expand all things, to combine and to make more things attainable. For the artist, it is the edgiest work of all; the biggest, most exciting challenge in a long history of the synthesis between technology and hand and mind and heart. -- J.D. Jarvis


## Why Writing a Book?

I’m very excited and want to learn more about the topic. 
This book is my attempt to do so, nothing more and nothing less (for now at least).
To really understand something, one has to pass through a grueling learning process.
One such strategy that works for me is called the Feynman learning technique:

1. Pretend to teach a concept you want to learn about to a student in the sixth grade.
2. Identify gaps in your explanation. Go back to the source material to understand it better.
3. Organize and simplify.
4. Transmit (optional).

This book is my attempt to follow Feynman's technique imperfectly.
Maybe, in the end, someone else will find some useful ideas in this book.
At the moment, I focus on [SuperCollider](https://supercollider.github.io/). 

## Source Code

The source code of the Jupyter-Book can be found here: [GitHub](https://github.com/BZoennchen/supercollider-book).

The book is currently published using [GitHub-Pages](https://bzoennchen.github.io/supercollider-book/intro.html).

## The Nature of an Online-Book

I experiment with SuperCollider and other tools and I write this book all in my spare time. 
It is a hobby. 
Therefore, I will develop and update it over time.
It is only a skeleton at its current state, and I will add new chapters and edit old ones. 
Therefore, do not expect anything professional.

In the future, you might be interested in extending the book with your content. 
Maybe this project will become a community effort to make SuperCollider, sound design, other tools and techniques more accessible.

Another thing I am looking forward to is combining the book with a Jupyter-Kernel for SuperCollider such that the book becomes interactive.

## Silent Contributors

I want to emphasize that this book is a mixture of my discoveries filtered and altered by my mind.
The creators of my discoveries and the content of the materials I studied are silent contributors.
Without the already existing material, I would not be able to learn SuperCollider or sound design in general. 

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
