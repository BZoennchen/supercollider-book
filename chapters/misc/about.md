# About the Book

## How I Started

I discovered the world of algorithmic composition and sound design using code in late 2021.
It all started when I watched an energetic and really motivated Sam Aaron presenting his [Sonic Pi](https://github.com/sonic-pi-net/sonic-pi).
I was immediately hooked, especially given the context: educational live programming for kids!

I started experimenting with Sonic Pi.
However, soon after playing around with it, I wanted to write my own synths for which it is unsuitable.
Sonic Pi is perfectly appropriate for sequencing your synth and samples but not so much for creating new exciting instruments.
You create your synth and samples beforehand and then use Sonic Pi to play with them.

I digged deeper and discovered other interesting tools such as [TidalCycle](https://github.com/tidalcycles/Tidal), [FoxDot](https://foxdot.org/) and, of course, [SuperCollider (SC)](https://supercollider.github.io/).
I am surprised that I never heard about SC before, even if it matured a long time ago, and there seems to be no natural alternative.
Compared to Sonic Pi, SuperCollider has a much steeper learning curve.
The language has some awful-looking syntax; it is less accessible, but at the same time, SuperCollider is much more extensible and powerful.

I fell in love with SC.
The language offers fascinating concepts that keep you thinking about signal-flow processing.
SC supports features well known in modern languages, such as ``Python``, and rather old languages.
The IDE feels pretty modern and supportive.
The documentation is decent, and the community is healthy.
SC is a powerhouse for discovering new exciting sounds.
It can be a driving force for learning sound design on a deep level.

It is time for me to learn more about *algorithmic compositions* and *sound design*.
What better way to get started than doing what I may be best at: coding.
Being creative by producing sound was the essential puzzle I was always looking for -- a strong connection between computer science and art.

## Who is Speaking?

>One’s stories persuade one’s audience that one is a particular kind of person. When one is one’s own audience, the telling amounts to having a self. -- *Leslie Ervine*, Even Better Than the Real Thing

Who am I?
Any description of oneself is doomed because it is a disection of the whole.
It is a typical modern thing to do: categorization.
It is insufficient and in its worst manifestations, discriminatory.
So take this with a grain of salt.
I can only feed your biased imagination.

From the bottom of my heart, I see myself as an artist of my own troubled life.
However, regarding my skills, I am a computer scientist.
I mean computer scientist in the sense of studying different aspects of computation:

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
Today, I am a software developer for the university who focuses on tools to support our education.
Furthermore, I try to influence the content as well as the structure of our lectures in a positive way.
As you might noticed, I like to engage with philosophy in my free time.

For other computer scientists interested in the topic of this book, it might be valuable to know which programming experience I had at the time of writing it.
I am very experienced in ``Java``.
Furthermore, I developed an introductory course for ``Python``.
I am also familiar with ``JavaScript``, ``PHP``, ``Scala``, and ``Go``.
Furthermore, I can read and understand ``C\C++`` code, but I am not very experienced in it.
I am familiar with GPU programming using ``OpenCL``.
Currently, I am trying to learn some ``Rust``.

I have no music theory education and do not play an instrument.
So this is a solid contrast to other great contributors, such as [Eli Fieldsteel](https://www.elifieldsteel.com/).
However, I am a big music lover, and I have always wanted to make my own music and never thought programming could lead me to this goal.

I am neither a professional musician nor a "professional" artist.
However, I strongly believe that every human being is capable of creating a whole universe of meaning.
We are storytellers thrown (*geworfen*) into a world that changes depending on our mood.
We can not change our being (*Dasein*), but we can choose how we want to deal with it.
Do we reject our surroundings, becoming alienated in the process?
Do we revolt against our fundamental condition of confusion?
Do we make the place where we live our home?

Music gives me peace.
It gracefully touches my soul.
It reminds me that something in this world expresses *the concrete*.
Something that escapes our calculating minds; something unexplainable.
Music sets me free.
Coding sets me free.
Thus, for me, coding music is the ultimate freedom.



## Why Writing an Online-Book?

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

I experiment with SuperCollider and other tools and write this book in my spare time. 
It is a hobby. 
Therefore, I will develop and update it over time.
In its current state it is only a skeleton, and I will add new chapters and edit old ones. 
Therefore, do not expect anything professional.

In the future, you might be interested in extending the book with your content. 
Maybe this project will become a community effort to make SuperCollider, sound design, and other tools and techniques more accessible.

Another thing I am looking forward to is combining the book with a Jupyter-Kernel for SuperCollider such that the book becomes interactive.

The source code of the Jupyter-Book can be found inside one of [GitHub](https://github.com/BZoennchen/supercollider-book) repositories.
The book is currently published using [GitHub-Pages](https://bzoennchen.github.io/supercollider-book/intro.html).

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
10. [Musimathics](http://www.musimathics.com/) volume 1 & 2 by Gareth Loy {cite}`loy:2006`, {cite}`loy:2007`

## Citing this book

TODO