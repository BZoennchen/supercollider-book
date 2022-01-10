(sec-ecosystem)=
# The Ecosystem

[SuperCollider (SC)](https://supercollider.github.io/) is a package or platform that consists of three components:
+ **scsynth**: a real-time audio server, i.e., the part that creates and plays the sound.
+ **sclang**: an interpreted programming language for sound creation and signal processing. The user controls the server **scsynth** by sending Open Sound Control (OSC) messages to the audio server.
+ **scide**: a powerful Integrated Development Environment (IDE) for programming in **sclang**. It offers an integrated help system, analyzing tools, and an extensive documentation.

[SuperCollider (SC)](https://supercollider.github.io/) is written in ``C++`` and was developed by James McCartney.
It was released in 1996.
In 2002 McCartney transformed it into a free software under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
It is still maintained and developed by an active community.

All three parts of [SuperCollider (SC)](https://supercollider.github.io/) are independent, that is, there might be some other subsystem that replaces some of its parts.
One can code by using other IDEs such as VSCode.
We can also use **sclang** independently to program applications that have nothing to do with signal processing.
These use cases are rare.
However, we find many projects that replace **sclang** and **scide**, especially in the area of Live Programming, for example:

+ [Sonic Pi](https://sonic-pi.net/): highly accessible and therefore especially interesting in the context of education.
+ [TidalCycle](https://tidalcycles.org/): functional language that focuses on the creation of complex rhythms.
+ [FoxDot](https://foxdot.org/): similar to [TidalCycle](https://tidalcycles.org/) but focuses more on the melodic side of compositions.
+ ...

In that case, we can develop our synths using **sclang** and run them on the server **scsynth**, but we control them by these systems.
If we are only interested in using existing synth and samples, we can do no longer rely on [SuperCollider (SC)](https://supercollider.github.io/).

Of course, deciding between [Sonic Pi](https://sonic-pi.net/), [TidalCycle](https://tidalcycles.org/), [FoxDot](https://foxdot.org/), and plain [SuperCollider (SC)](https://supercollider.github.io/) comes down to personal preference and goals.
Each platform targets different objectives and has different advantages as well as disadvantages.
In my opinion, [SuperCollider (SC)](https://supercollider.github.io/) is the most powerful one but can be less intuitive and flexible, especially for the live coding experience.

I encourage readers that are interested in live coding to check them all out!

## SCSynth

The real-time audio server forms the core of the platform.
The server uses synth definitions ``SynthDef`` as templates for creating synth nodes.
Those synth instances can then be executed.
The user can trigger and influence the execution via OSC messages.
For example, one can change the arguments of a ``SynthDef`` while the synth is executed.

Very similar to object-oriented programming, a ``SynthDef`` is a blueprint for a synth instance.
The composer

1. defines the blueprint, that is, a ``SynthDef``,
2. adds the blueprint to the server,
3. creates a new instance, that is, a synth,
4. and executes, controls, and terminates it.

All those steps are done via the client-side interpreted programming language **sclang**.

## SCLang

The interpreted programming language **sclang** is an objective-oriented programming language.
It is similar to ``Smalltalk`` or ``Ruby`` with syntax similar to ``C`` or ``JavaScript``.
**sclang** is dynamically typed and has its own garbage collector.
Functions are first-class objects.

From a musical point of view, it has its own interactive programming and Live Coding packages and a subsystem for composing patterns and signal graphs.

## SCIDE

The [SuperCollider (SC)](https://supercollider.github.io/) Integrated Development Environment (IDE) is a Qt-based cross-platform application.
Code can be executed in a notebook-like manner, that is, interactively using the REPL (Read–Eval–Print Loop).

```{figure} ../../figs/ecosystem/ide.png
---
width: 800px
name: fig-ide
---
The **scide**.
```

The IDE offers some useful tools such as

+ the *Node Tree* displays the synth running currently on the server ``Server.local.plotTree;``
+ a *Levels* displays the current volume/amplitude for each channel ``Server.local.meter;``
+ a *Stethoscope* displays the scope of the current signal ``Server.local.scope;``
+ a *Freq Analyzer* that displays the frequencies of the current signal ``FreqScope.new;``
+ a *Server* displays useful information about the server such as the CPU workload ``Server.local.makeWindow;``.

```{figure} ../../figs/ecosystem/ide-tools.png
---
width: 600px
name: fig-ide-tools
---
Different **scide** tools for analyzing and observing what is going on.
One synth is running (a sine wave of 220 cycles per second).
```

These tools, depicted in {numref}`Fig. {number} <fig-ide-tools>`, can be used to observe and analyse the state of the server as well as the signal processing.
