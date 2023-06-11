# Preface

>Emancipatory politics must always destroy the appearance of a "natural order", must reveal what is presented as necessary and inevitable to be a mere contingency, just as it must make what was previously deemed to be impossible seem attainable. -- Mark Fisher

This book delves into the realm of sound design and music composition through the lens of the programming language and compositional environment known as SuperCollider, a creation of James McCartney and numerous other contributors.
Here, [SuperCollider](https://supercollider.github.io/) is not merely a tool but a conduit for unveiling the essence of sound and music. This book, therefore, transcends the mere learning of a programming language and development environment. 
SuperCollider offers us a low-level control that can foster a profound understanding of computer music at its roots.

The impetus behind this book draws from my experiences as a computer science lecturer, my firm belief in the oft-overlooked creative potential inherent in coding, and perhaps my own struggles with effective communication.

Music, a form of human communication that has evolved over time, is undeniably worth exploring. 
It can stir profound emotions, narrate tales, and touch us deeply, despite its capacity to be stark, brutal, and eerie. 
Algorithms, however, are characterized by their calculative nature. 
They are rigid, well-defined formal rules that computers execute in an unemotional, relentless manner. 
Yet, intriguingly, there exists a strong kinship between musical compositions and algorithms. 
Both hinge upon a sequence of actions and representations of time.

While music demands to be listened to and experienced, it's less common to *experience* algorithms. 
They are often subject to analytical scrutiny, their aesthetic allure arising from their efficiency, correctness, and elegance. 
My studies in complexity theory, automata theory, and other formal areas were geared towards gaining a deep analytical comprehension of algorithms.
However, I now believe that similar to music, a purely analytical approach to algorithms conceals some facets of their being-in-the-world and our *Dasein* as we experience their existence. 
Describing precisely what I mean is challenging, given the inherent limitations of written language, which is an abstraction of the real experience. 
Since I believe that a purely analytical approach cannot replace experiential knowledge, I posit that *computer music* can augment our understanding of algorithms and technology as a whole. 
To echo Fisher's sentiments, it can propel music and coding into new emancipatory realms by dismantling the illusion of a *natural order*, potentially rejuvenating selfless collaboration.

The sentiments expressed here resonate with a specific set of beliefs, and I make no attempt to disguise that my motivation for penning this book is intertwined with a particular belief system, which I will gradually reveal to the attentive reader. 
It would be deceptive to assert that I approach this work without any agenda. 
Indeed, the prospect of not possessing an agenda seems quite improbable.

## How I Started

I was introduced to the world of algorithmic composition and sound design using code in late 2021. The journey began when I watched an invigorating presentation by the highly motivated Sam Aaron, who was showcasing his project [Sonic Pi](https://github.com/sonic-pi-net/sonic-pi).
I was instantly captivated, especially by the context in which it was placed: educational live programming for children! The concept of merging playfulness with code to create music appealed to me instantly.

I eagerly started experimenting with Sonic Pi. 
However, soon after getting to grips with it, I craved more control; 
I yearned to craft my own synths, a task for which Sonic Pi wasn't particularly suited. 
While Sonic Pi is superb for sequencing your synth and samples, it doesn't offer the same level of flexibility when it comes to creating novel instruments. 
The process involves preparing your synth and samples beforehand, then using Sonic Pi to manipulate them.

I delved deeper and stumbled upon other intriguing tools like [TidalCycle](https://github.com/tidalcycles/Tidal), [FoxDot](https://foxdot.org/), and of course, [SuperCollider (SC)](https://supercollider.github.io/).
It's surprising that SuperCollider, despite its maturity and lack of a natural alternative, had not crossed my path earlier.

When compared with Sonic Pi, SuperCollider presents a more challenging learning curve. Its language possesses certain archaic, thus somewhat displeasing, syntax aspects. 
This makes it less accessible, yet, at the same time, SuperCollider is considerably more extendable and powerful.

SuperCollider quickly won me over. 
The language introduces engaging concepts that incite deep contemplation about signal-flow processing.
SC supports features commonly found in both modern languages, such as ``Python``, and older ones. 
Its integrated development environment (IDE) feels notably modern and supportive. 
The documentation is comprehensive, and there's a thriving community surrounding it. 
SuperCollider serves as a powerful tool for exploring new and exciting sounds and can act as a catalyst for learning sound design on a profound level.

It's time for me to delve deeper into the realms of *algorithmic compositions* and *sound design*. 
What better way to commence this journey than by leveraging what I might be most adept at: coding. 
Engaging creatively in sound production proved to be the pivotal element I had been seeking -- a robust link between computer science and art.

## Who is Speaking?

>One’s stories persuade one’s audience that one is a particular kind of person. When one is one’s own audience, the telling amounts to having a self. -- *Leslie Ervine*, Even Better Than the Real Thing

Who am I? Any self-description is inherently flawed as it dissects the whole, thereby limiting it. 
Such categorization is characteristic of the modern era -- often insufficient, and in its most extreme forms, discriminatory. 
So, interpret what follows with a degree of skepticism, acknowledging that it may merely feed into your preconceptions.

At my core, I perceive myself as an artist navigating my own intricate life -- a journey that is indeed fraught with challenges, but in the grandest sense of tragedy. 
In terms of my professional skills, however, I am a computer scientist. 
By this, I mean that I explore various facets of computation:

+ **information:** what is information, and how can we create, manipulate and interpret it?
+ **computation:** what is computable, and what do we mean by that?
+ **formal methods:** what can we express, and what do we need to express it?
+ **algorithms** and **data structures:** what can we build?

After completing school, I underwent practical training as a software developer and worked in the industry for four years. 
Driven by a sense of restlessness, I returned to school for an additional year before embarking on my computer science studies. 
I earned my Bachelor's degree in 2013, my Master's in 2017, and finally, my Ph.D. in 2021.

In my doctoral thesis, I examined various microscopic simulation models for pedestrian streams and developed algorithms capable of simulating the movements of many pedestrians within a large area faster than real time. This venture sparked my interest in *complex systems*, a subject that continues to captivate me.

During my Ph.D. candidacy, I discovered my love for teaching. 
Currently, I serve as a software developer for the university, where my primary role involves developing tools to support our educational efforts. 
I am also active in influencing both the content and structure of our lectures, aiming to bring about positive changes.

As you may have inferred, philosophy is a significant interest of mine in my leisure time.

After school, I did practical training as a software developer.
I worked for four years in the industry.
Then, in desperation, I finished an additional year in school and finally started studying computer science.
I finished my Bachelor's degree in 2013, my Master's in 2017, and my Ph.D. in 2021.
In my Ph.D. thesis, I analyzed different microscopic simulation models for pedestrian streams and developed algorithms to simulate many pedestrians in a large area faster than in real time.
This got me into the subject of *complex systems* which I am still highly interested in.
During my time as a Ph.D. candidate, I enjoyed teaching.
Today, I am a software developer for the university who focuses on tools to support our education.
Furthermore, I try to influence the content as well as the structure of our lectures in a positive way.
As you might notice, I like to engage with philosophy in my free time.

For other computer scientists interested in the topic of this book, it might be valuable to know which programming experience I had at the time of writing it.
I am very experienced in ``Java``.
Furthermore, I developed an introductory course for ``Python``.
I am also familiar with ``JavaScript``, ``PHP``, ``Scala``, and ``Go``.
Furthermore, I can read and understand ``C\C++`` code, but I am not very experienced in it.
I am familiar with GPU programming using ``OpenCL``.
Currently, I am trying to learn some ``Rust``.

Nor do I have any music theory education or play an instrument.
I am a self-taught "music theorist".
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
I want to learn more about *algorithmic composition*, *sound design* and *computer music*. 
This book is my attempt to do so;
To understand something, one has to pass through a grueling learning process.
One such strategy that works for me is called *the Feynman learning technique*.
It consists of the following steps:

1. pretend to teach a concept you want to learn about to a student in the sixth grade
2. identify gaps in your explanation
3. go back to the source material to understand it better
4. organize and simplify
5. transmit (optional)

This book is my attempt to follow *Feynman's technique* imperfectly.
In the end, someone else might find valuable ideas in this book.
Currently, I focus on [SuperCollider](https://supercollider.github.io/), *sound design*, little bit of *music theory* and *algorithmic composition*.
Within the book, I use ``Python`` to create some of the plots. 

I experiment with SuperCollider and other tools and write this book in my spare time. 
It is a hobby. 
Therefore, I will develop and update it over time.
This will take some time.
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
Without the already existing material, I would not be able to learn either SuperCollider or any of the other topics. 

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