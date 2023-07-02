# Preface

>Emancipatory politics must always destroy the appearance of a "natural order", must reveal what is presented as necessary and inevitable to be a mere contingency, just as it must make what was previously deemed to be impossible seem attainable. -- Mark Fisher

```{only} html
[![](https://img.shields.io/github/stars/BZoennchen/supercollider-book?style=social)](https://github.com/BZoennchen/supercollider-book)
```

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

As a computer scientist who delved into the topic of this book, my programming experience at the time of writing may be valuable for other readers. 
I possess a wealth of experience in ``Java`` and have even developed an introductory course for ``Python``. 
Besides that, I am proficient in ``JavaScript``, ``PHP``, ``Scala``, and ``Go``. 
While I can read and comprehend ``C\C++`` code, my practical experience in these languages is somewhat limited. 
I am also well-acquainted with GPU programming, specifically using OpenCL. Currently, I'm in the process of learning ``Rust``.

I don't have any formal education in music theory, nor do I play an instrument. 
I am, in fact, a self-taught "music theorist". 
This represents a stark contrast to other significant contributors, such as [Eli Fieldsteel](https://www.elifieldsteel.com/). 
However, I have a profound love for music and have always yearned to create my own, never imagining that programming could facilitate this aspiration.

I am not a professional musician or a 'professional' artist. But I fervently believe that every individual is capable of creating a universe replete with meaning. We are storytellers thrust into a world that morphs depending on our moods. While we cannot alter our existence, we have the freedom to choose how to navigate it. Do we deny our surroundings, subsequently becoming estranged? Do we rebel against our inherent state of bewilderment? Do we make the place where we exist our home?

Music instills a sense of tranquility in me. It tenderly resonates with my soul, reminding me that something in this world embodies 'the concrete' - an element that eludes our analytical minds and defies explanation. Music liberates me. Coding does the same. Consequently, for me, coding music represents the epitome of freedom.

## Why Writing an Online-Book?

I am truly excited! 
I aspire to delve deeper into *algorithmic composition*, *sound design*, and *computer music*. 
This book serves as a vehicle for this journey. 
Grasping any concept demands an arduous learning process. 
A technique that consistently aids me in this endeavor is known as the Feynman learning technique. It consists of the following steps:

1. Pretend to teach a concept you wish to understand to a student in the sixth grade.
2. Identify gaps in your explanation.
3. Revert to the source material for a deeper understanding.
4. Organize and simplify.
5. Transmit (this step is optional).

This book is a result of my attempt to adhere to Feynman's technique, albeit imperfectly. 
I hope that others might find valuable insights within its pages. 
At present, my focus is on [SuperCollider](https://supercollider.github.io/), *sound design*, a bit of *music theory*, and *algorithmic composition*. 
I utilize ``Python`` within the book to generate some of the plots.

In my spare time, I experiment with SuperCollider and other tools while writing this book. 
It is a hobby, and as such, I will gradually develop and update it over time.
Patience will be required as the book, in its current state, is merely a blueprint.
I will add new chapters and revise old ones incrementally. 
Hence, professional-grade content should not be expected immediately.

In the future, you might be intrigued to augment the book with your contributions. 
This project could potentially evolve into a community-driven effort to make 
SuperCollider, sound design, and other tools and techniques more accessible.

Another exciting prospect I anticipate is the amalgamation of this book with a Jupyter-Kernel for SuperCollider, making the book interactive.

The source code of the Jupyter-Book can be found in one of the [GitHub](https://github.com/BZoennchen/supercollider-book) repositories. 
Currently, the book is published using [GitHub-Pages](https://bzoennchen.github.io/supercollider-book/intro.html).

## Silent Contributors

I would like to underscore that this book is a compilation of my discoveries, each one filtered and influenced by my perspectives. 
The creators of the material I explored and the content of the resources I studied are silent contributors. 
Without the pre-existing material, I would not have been able to learn about SuperCollider or any of the other topics.

A special note of gratitude is due to [Eli Fieldsteel](https://www.elifieldsteel.com/), who generously provides multiple excellent courses on [SuperCollider](https://supercollider.github.io/) openly and for free via his [YouTube-Channel](https://www.youtube.com/user/elifieldsteel). 

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
11. [Algorithmic Composition: A Gentle Introduction to Music Composition Using Common LISP and Common Music](https://quod.lib.umich.edu/s/spobooks/bbv9810.0001.001) by Mary Simoni {cite}`simoni:2003`
12. [Algorithmic Composition: Paradigms of Automated Music Generation](https://link.springer.com/book/10.1007/978-3-211-75540-2) by Gerhard Nierhaus {cite}`nierhaus:2010`

## Citing this Book

```bibtex
@misc{zoennchen:2022,
  title = {{A}lgorithmic {C}omposition with {SuperCollider}},
  year = {2022},
  author = {Benedikt Z{\"o}nnchen},
  url = {https://bzoennchen.github.io/supercollider-book/intro.html},
}
```