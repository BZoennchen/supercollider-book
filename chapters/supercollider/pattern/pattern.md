(sec-playing-pattern)=
# Playing Patterns

>Patterns provide a facility for easily exploring generative music/algorithmic composition.
>Rather than making single synthesis events, we're looking much more at how we schedule lots of events over time. -- Nick Collins {cite}`collins:2004`

[UGens](sec-ugens) are the basic building blocks for our synth, i.e., instruments, i.e., a number generator that via our loudspeakers produces sound.
Sound design in SC is the process of combining unit generators, i.e., to build a *unit generator graph function* that spits out the floating-point numbers we desire.
Through the rigid coupling of air molekules (medium) sound (form) is constructed (see [Medium and Form](sec-medium-and-form)).
This coupling is realized by technology, in our case a digital synthesizer specified by code and this code (form) is the rigid coupling of words from a programming language (medium).

Next we understand this form (sound) as our new medium.
We want to create rhythms, textures, harmony, and melodies---we want to create music.
Interestingly, we find the corresponding representations for our new medium and form within our code.
Our synthesizer-code, and what the languages provides us with to use this code, build up a new medium.
It is our task to select from the new *horizon of possibilities*.

There are different ways to do this.
First of all, as mentioned in [The Ecosystem](sec-ecosystem), there are other software packages such as [Sonic Pi](https://sonic-pi.net/), [TidalCycle](https://tidalcycles.org/) or [FoxDot](https://foxdot.org/) which are designed to play synths and samples.
[Sonic Pi](https://sonic-pi.net/) goes the imperative way of combining iteration and threading in a single concept called ``live_loops``.
These threaded loops can be synced with other loops and follow a strict timing concept.
[FoxDot](https://foxdot.org/) uses the concept of players.
Each player can play a synth repeatedly and is synchronized to a clock.
[TidalCycle](https://tidalcycles.org/) went the functional route.
It also uses players but lets the user manipulate a signal in a functional style.
Each of these tools offers a distinct language and, therefore a way of thinking---a specific medium and it can be a creative pleasure to be limited by a certain medium.

However, [SuperCollider](https://supercollider.github.io/) offers its own excellent and powerful possibilities for composing a musical piece.
Within the language, we can use plain iteration and threading via [Routines](https://doc.sccode.org/Classes/Routine.html) and [Tasks](https://doc.sccode.org/Classes/Task.html), see section [Rountines and Tasks](sec-routines-tasks).
The advantage of using routines is that there is not much to remember or new to learn.
You build everything by the basic imperative programming concepts, i.e., *loops*, *cases*, *arrays* and *functions*.
As a programmer this medium feels familiar.
However, the freedom comes at a cost: a lot of typing.
Furthermore, your code becomes quite unreadable very fast.

Another option is the so-called [Pattern](https://doc.sccode.org/Classes/Pattern.html) library which uses [Pattern](https://doc.sccode.org/Classes/Pattern.html), [Streams](https://doc.sccode.org/Classes/Stream.html), and [Events](https://doc.sccode.org/Classes/Event.html) to abstract most of the technical burden away.
Instead of writing how your code operates, you can write what you want.
It is a switch from the *imperative* to the *declarative* paradigm.
Patterns are not better or worse than 'closer-to-metal' concepts like routines.
With routines you can start right away.
Using patterns requires you to learn a new vocabulary and until one has a critical mass of knowledge about the different pattern, it can be hard to trust them.
Furthermore, if there is not a pattern that does quite what you want, then it might take some ingenuity to combine patterns into new designs. 
(Custom behaviors can always be written using [Prout](https://doc.sccode.org/Classes/Prout.html).)

Later we will see how we can use the [live programming interface](sec-live-coding) to enhance our ability to create rhythms and melodic textures on the fly.