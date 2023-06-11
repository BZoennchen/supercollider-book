# TidalCycles

As an example, I want to show how one can use other interesting environments such as [Sarine](https://sardine.raphaelforment.fr/) or [Sonic Pi](https://sonic-pi.net/) in combination of SuperCollider.
I choose to look into [*TidalCycles*](https://tidalcycles.org/) or *Tidal*.

## What is TidalCycles

As I alluded in my discussion of [pattern](sec-playing-pattern), a different syntax, environment, language, or in general technology opens the door to new possibility while also closing others.
Therefore, staying open to all sorts tools until we found what we invision is invaluable.

Similar to SuperCollder, *Tildal* is a free and open source coding environment written in ``Haskell`` by [Alex McLean](https://slab.org/).
But distinct from SC it focuses on live coding for algorithmic patterns.
Under the hood Tidal uses SuperCollider's audio server to run synth.
Basically, Tidal triggers event that will be executed by SuperCollider.

One might ask, why shall I be interested in Tidal when it just triggers SC events?
Well using Tidal transforms you into a completely different mindset because it is based on *the cycle* and more transformative and linear flow of information.

Using SuperCollider's [pattern](sec-playing-pattern), you have to think about the construction of events by combining multiple streams, each responsible for a specific argument, in your head.
Therefore, you have to deal with a *non-linear flow of information*.
This can make it hard to change or establish certain effects on the fly, since it is hard to keep the graph in your head and to achieve a simple "linear" change, you often have to change multiple streams.

Tidal introduces limitations (a certain structure), i.e., *the cycle* and mutations on the flow, that makes interesting on-the-fly changes easier.
It allows you to make the complex music in a view lines of code.
It relies on [SuperDirt](https://github.com/musikinformatik/SuperDirt), a general purpose framework for playing samples and synths, controllable over the [Open Sound Control](sec-osc) protocol, and locally from the SuperCollider language.
Basically, SuperDirt sits on top of SuperCollider.

## The Cycles

*TidalCycles* operates based on **cycles** that run (synchronized) in the background, meaning that the timing of events is not based on a flexible start time and duration but on how the event is aligned in relation to other events.
There is no need to specify absoulte timings.
By default an event starts at the beginning of a cycle and takes the duration of a complete cycle.

For example

```tidal
d1 $ s "drum"
```

Plays the sample "drum" starting the sample at the beginning cycle for duration of one cycle.