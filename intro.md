# Introduction

>I got reconnect properly with computers [...] I didn't have to use someone else's idea of what a delay, or a reverb, or a sequencer shoud do, or should sound like; I could start from the ground, and think in terms of sound and maths. It was like coming off the rails. -- *Jonny Greenwood*

In its early state, *cyberculture* promised a new kind of creative freedom, an innovative age of anarchistic collaboration and self-expression, but that dream was quickly overturned in favor of making money.
Watching the unstoppable force of the hyper-capitalist sector bringing down the fruits and spoils of open collaboration and transparency was heartbreaking to me.
I was too young to be part of *The Early Days* and could only dive into leftover pieces, such as the *Gaming Culture* which has dissolved into a market as well.
Today we realized that this tech explosion brought us an even higher degree of monetarization and commercialization.
Now it is our dreams, feelings, moments, culture, and intimacy that is sold.

The capitalist's logic poisons art.
It drives us into a state of endless consumption over creation.
There might be some short period in which something genuinely creative can emerge, but soon after, its singularity will be destroyed by its assimilation into a sellable thus quantifyable product.

To me, the *community of algorithmic composers* seems to be quite *egalitarian*, open and transparent.
It appears as a *counter-culture*.
Since it is such a niche, it is not yet stripped of its cultural connection.
As a left-leaning person, I enjoy such contra commercial trends.
Consequently, I got not only interested because of the matter but also because of its community.
I hope, at some day, my project will be helpful, and bring not money but joy and communal interest in the matter and its community.
Even if we lack an alternative to the money-making machine and seemingly silently accept this "fact", a reinvigorated *cyberculture* might act as a reminder that, despite *Mark Fisher's* declaration, we can still revolt against *Capitalist Realism*.

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
Is there anything like *The Self*, without others?
From the bottom of my heart, I am a computer scientist.
But I may have to clarify my interpretation of the term.
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
Today, I am a software developer for University that focuses on tools to support our education.
Furthermore, I try to influence the content as well as the structure of our lectures in a positive way.

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
It reminds me that something in this world expresses *The Concrete*.
Something that escapes our calculating minds; something unexplainable.
Music sets me free.
Coding sets me free.
Thus, for me, coding music is the ultimate freedom.

## Notes on Technology

>We might be in a collective state of existential crisis, but we are to busy to notice it.

In my opinion, technology should not be trusted naively.
Technology is neither inherently good nor bad -- it can be used for the good, the bad, the ugly, and the beautiful.
In addition, it is neither inherently progressive nor repressive.
We must rethink technology as something that, like nature, is not strictly separated from us.
Technology shapes our way of communication and our material realities; it opens up spaces of possibilities but, at the same time, closes the door to preexisting ways of life.

For example, the introduction of cars influenced how we plan and build cities and, consequently, possessing a car became mandatory in many areas.
Email changed our communication ethics at the workplace; it made the interaction with emails mandatory.
I see it as a privilege that my generation was one of the last growing up in an internet-free world.
Today, children are confronted with a world of spectacle distractions.
Their desires and their attention is channeled into the profit making fungus.

Massively widespread technology has this dictating ability -- once established, it dictates our way of communication.
It shapes our mundane life, and if we want to live within society, we can not escape it.
We live in an *age of disruption* where technology escapes any deep analysis because it evolves faster than we can blink.
Every-day people are busy.
They are constantly trying to keep up with all the news feeds poking at them, and it becomes hard to apply any narrative to their experiences.
They do not know what is going on.
They are just moving through their day, moment to moment.
It is a disorienting place to be.
Time slips away without any deep satisfaction; another day went to *Instagram*.

The danger is never to stop hustling.
We need spaces that help us not to escape but to **really** engage with technology!
To understand how it affects us, how it changes us, how it can help us and how it might destroy us.

We get used to the internet, smartphones, social media, and other platform economies, and endless repetition of the trivial.
As an individual, we seem powerless concerning new technologies.
If there is a market (built buy the creation of desire, i.e., marketing), we most certainly have to get used to yet another technological phantasy.
Is it *The Public* that wants to transfer another big chunk of reality into a *Metaverse*;
a virtual world based on a business ontology and governed by a corporate dictatorship?

I neither advocate for the denial nor for embracing technology in general.
I love technology.

>It certainly is not a matter of condemning the industrial and technological fate of humanity. Rather, it is a case of reinventing this fate. -- *Bernard Stiegler*

I think digital technology is powerful and could likely solve the majority of humanities problems; 
from climate change to income distribution, sensor-based agricultural practice, food, education and the abolishment of racialization, gender discrimination, ableism and classism.
Digital technology can be amazing, but when all decisions about how to deploy and use it are in the hands of business people, then we have a problem.
These people implement a hazardous form of technological-driven society with the economy at its absolute center: a form of *digital / computational capitalism* where algorithms produce money instead of value.

We are no longer in a free market.
We are not in a place where the people have the same access to tools and technology.
They are no longer the masters.
When a young person has an idea, they automatically go to a money person because they think that is the only way to get their product developed.
Developers and entrepreneurs often start with a genuine belief to make the world a better place.
They believe their contribution will help the world in some way and be empowering, not just to them and their investors, but to some industry or consumer base.
But then they take money from problematic angles forcing them into specific actions.
At the stock market, business becomes gamified, i.e., companies are no longer concerned about their product.
Their mind is occupied with winning; 
*Bezos* versus *Sergey Brin* versus *Mark Zuckerberg*.

We have to ask:

>Are we programmers, or are we programmed?

*Meta's* customer is not the little girl using it to make friends.
No, it is the company that is buying the little girl's *social graph*.
Who is *Uber's* customer?
It is not the driver that it should be.
It is not the passenger, which it could be.
It is the shareholder, the investor.
*Uber* does not care about creating a decent, sustainable taxi industry.

We must critically analyze what each technology does, implying that we disregard the *neutral point of view*.
However, I do not advocate for returning to some naturalistic past, i.e., some lost authenticity.
It would bring only disappointment because such authenticity was never there in the first place.
Nature is a beautiful beast; it is the real that hunts us; it is us.
*Going back to nature* in the sense that we withdraw from working on landscapes, bodies and psychic systems are unfounded from a naturalistic ontological perspective.
There is no reason why we should not challenge its normative power, especially if constructed power structures are disguised as *natural*!

While technology is not inherently good or bad, it can never be neutral.
It is always based on some value and intention, and if we use a particular technology, we have to know what these values and intentions are.
Does this technology empower the right people?
Is it emancipatory?
How does it change our way of thinking, feeling, and communicating?
Is it helpful for us?
Who is controlling it?
What does it intend to accomplish?
Does it really work as intended?
What spaces does it open up?
Does it offer artistic potential?
What realities does it destroy?
I advocate for a culture of conscious engagement -- a society of aware agents within the realm of technology.
A potent society should have the power to reject technological advances in favor of cultural progress.

To understand technology, we have to understand ourselves.
We have to know how we can be manipulated, what is good for us, and what we need.
For example, we know that non-virtual social interactions are important.
It is calming and reassuring for human organisms to look into someone else's eyes, so to literally move into sync with another person.
Today we have so much communication without synchronization.
The communication is shallow and abstract.
We end up feeling empty and more exhausted.

>The 21st century is oppressed by a crushing sense of finitude and exhaustion. -- *Mark Fisher*

We live between emails, calendars, and *Zoom*-Meetings, missing out on the things that really make us happy: talking to other people, playing with our kids, and giving love to others.
At the same time, there is always a *fear of missing out*:
Can I get in on this thing before it is completely gone?

What makes me optimistic about our use of technology are young people.
Even though we have an increase in suicide rates, probably due to the use of social media, I also observe more caution towards technology.
Young people seem to use technology much more appropriately because they are less fascinated by it.
They seem to understand that these big tech companies are not interested in improving their lives but in using them as vehicles.

I believe technology is always destructive as well as creative.
It disrupts existing spaces and opens up new ones. 
The artist's responsibility is to reveal and explore this process.
She is the one who create aesthetic symbols -- a horizon of a possible future.
Neither being prejudiced nor playing the devil's advocate but engaging with technology and its masters honestly.
The artifacts of our past are not given circumstances of nature but are invented by people.
We must disregard our automatic acceptance of how things are because it leads to a sense of helplessness about changing anything.
There is neither time for the bitter sweet melancholia nor the illusion that small local changes suffice.
Echoing the words of *Mark Fisher*: I am not worried about a zombie apocalypse, but I am worried that it is easier for people to imagine a zombie apocalypse than to visualize what life will be like in 10 or 20 years from now.
I am concerned that we have already given up, that we lack the imagination and courage to engage in the way that we really should be, and we will resort to reactions and seemingly easy but unreal solutions.

The digital is a critical factor in driving our pacification while we are looking into the abyss right in front of us.
So let us engage with it; let us be critical; let us fight back; let us sing a new song of technological empowerment of the people all around the world; let us reimagine our *cyberculture*.

>Digital is not here to put an end to anything.
Rather it is here to expand all things, to combine and to make more things attainable.
For the artist, it is the edgiest work of all; the biggest, most exciting challenge in a long history of the synthesis between technology and hand and mind and heart. -- *J.D. Jarvis*

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