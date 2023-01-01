(sec-playing-pattern)=
# Playing Patterns

[UGens](sec-ugens) are the basic building blocks for our synth, i.e., instruments, i.e., sound.
Sound design in SC is the process of combining unit generators, i.e., to build a *unit generator graph function* that spits out the floating-point numbers we desire.
But having instruments is not enough, we also want to play them!
We want to create rhythms, textures, and melodies.

There are different ways to do this.
First of all, as mentioned in [The Ecosystem](sec-ecosystem), there are other software packages such as [Sonic Pi](https://sonic-pi.net/), [TidalCycle](https://tidalcycles.org/) or [FoxDot](https://foxdot.org/) which are designed to play synths and samples.
[Sonic Pi](https://sonic-pi.net/) goes the imperative way of combining iteration and threading in a single concept called ``live_loops``.
These threaded loops can be synced with other loops and follow a strict timing concept.
[FoxDot](https://foxdot.org/) uses the concept of players.
Each player can play a synth repeatedly and is synchronized to a clock.
[TidalCycle](https://tidalcycles.org/) went the functional route.
It also uses players but lets the user manipulate a signal in a functional style.
Each of these tools offers a distinct language and, therefore a way of thinking.

However, [SuperCollider](https://supercollider.github.io/) offers its own excellent and powerful interface for composing a musical piece.
Within the language, we can use plain iteration and threading.
Secondly, we can use so-called [Pattern](https://doc.sccode.org/Classes/Pattern.html), [Streams](https://doc.sccode.org/Classes/Stream.html), and [Events](https://doc.sccode.org/Classes/Event.html) to abstract most of the technical burden away!

Later we will see how we can use the live programming interface to enhance our ability to create rhythms and melodic textures on the fly.