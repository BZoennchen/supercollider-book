(sec-ecosystem)=
# The Ecosystem

[SuperCollider (SC)](https://supercollider.github.io/) is a package and a platform that consists of three components:
+ **scsynth**: a real-time audio server, i.e., the part that creates and plays the sound.
+ ``sclang``: an interpreted programming language for sound creation and signal processing. The user controls the audio server (**scsynth**) by sending Open Sound Control (OSC) messages to it.
+ **scide**: a powerful Integrated Development Environment (IDE) for programming in ``sclang``. It offers an integrated help system, analyzing tools, and extensive documentation.

[SuperCollider (SC)](https://supercollider.github.io/) is written in ``C++`` and was developed by James McCartney.
It was released in 1996.
In 2002 McCartney transformed it into a free and open software project under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
It is still maintained and developed by an active community.

```{figure} ../../figs/supercollider/ecosystem/architecture-dark.png
---
width: 800px
name: fig-architecture
---
```

All three parts of [SuperCollider (SC)](https://supercollider.github.io/) are independent, i.e., there might be some other subsystem that replaces some of its features.
One can code by using other IDEs such as [VSCode](https://code.visualstudio.com/).
We can also use ``sclang`` independently to program applications that have nothing to do with signal processing.
These use cases are rare.
However, we find many projects that replace ``sclang`` and **scide**, especially in the area of *live programming*, for example:

+ [Sonic Pi](https://sonic-pi.net/): highly accessible and therefore fascinating in the context of education.
+ [TidalCycle](https://tidalcycles.org/): functional language that focuses on the creation of complex rhythms via pattern.
+ [FoxDot](https://foxdot.org/): similar to [TidalCycle](https://tidalcycles.org/) but focuses more on the melodic side of compositions.
+ [Sardina](https://github.com/Bubobubobubobubo/Sardine): a ``Python`` based live coding library
+ [Overtone](https://github.com/overtone/overtone): open source audio environment designed to explore new musical ideas from synthesis and sampling to instrument building, live-coding and collaborative jamming
+ [ORCA](https://github.com/hundredrabbits/Orca): esoteric programming language designed to quickly create procedural sequencers
+ [Punkt](https://github.com/pjagielski/punkt): live coding music library/environment for Kotlin, for software developers who want to dive into live coding music
+ ...

In that case, we can develop our synths using ``sclang`` and run them on the server **scsynth**, but we control them by these systems.
If we are only interested in using existing synths and samples, we can do so without relying on [SuperCollider (SC)](https://supercollider.github.io/).
Furthermore, there are many more projects that use their own audio server, i.e., do not rely on SuperCollider:

+ [ChucK](https://chuck.cs.princeton.edu/): strongly-timed, concurrent, and on-the-fly music programming language
+ [Gibber](https://github.com/gibber-cc/gibber): live coding environment for the web browser
+ [Gwion](https://github.com/Gwion/Gwion): a programming language designed for making music and sound inspired by [ChucK](https://chuck.cs.princeton.edu/) but also has a REPL mode you can use for live-coding
+ [GLICOL](https://glicol.web.app/): a graph-oriented live coding language written in ``Rust`` (I have my eyes on that project ;)!)
+ ...

Of course, deciding between [Sonic Pi](https://sonic-pi.net/), [TidalCycle](https://tidalcycles.org/), [FoxDot](https://foxdot.org/), or any other environment/language and plain [SuperCollider (SC)](https://supercollider.github.io/) comes down to personal preference and goals.
The ``sclang`` is rather *close to the metal*.
It offers a lot of control but might be less productive if you want to get things done quickly.
Each platform targets different objectives and has various advantages as well as disadvantages.
In my opinion, [SuperCollider (SC)](https://supercollider.github.io/) is the most powerful one but can be less intuitive and flexible, especially for a collaborate live coding experience.
I encourage readers interested in live coding to check them all out!

(sec-audio-sever)=
## The Audio Server

The real-time audio server *scsynth* forms the core of the platform.
The server uses synth definitions, i.e., [SynthDefs](https://doc.sccode.org/Classes/SynthDef.html) as templates for creating synth nodes.
Those synth instances can then be executed.
A [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) represents a signal-flow-graph and executing a synth equates with creating an instance of a specific [SynthDef](https://doc.sccode.org/Classes/SynthDef.html), i.e., such a graph.
The user can trigger and influence the execution via [OSC](https://en.wikipedia.org/wiki/Open_Sound_Control) messages.
For example, one can change the arguments of a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) while the synth is executed.
In fact, many ``sclang`` classes abstract away the explicit communication via OSC messages.

Very similar to object-oriented programming, a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) is a blueprint for a synth instance.
The composer

1. defines the blueprint, that is, a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html),
2. adds the blueprint to the server,
3. creates a new instance, that is, a synth,
4. and executes, controls, and terminates it.

All those steps are done via the client-side interpreted programming language ``sclang``.
It abstracts away thus simplifies the communication with the audio server such that we do not have to write pure OSC messages.

## Tha Language

The interpreted programming language ``sclang`` is an objective-oriented programming language.
It is similar to ``Smalltalk`` or ``Ruby`` with syntax similar to ``C`` or ``JavaScript``.
``sclang`` is dynamically typed and has its own garbage collector.
Functions are first-class objects and everything is an object, i.e., there are no primitive data types.

From a musical point of view, it has its own interactive programming and lives coding packages and a subsystem for composing patterns and signal graphs.
Its strength lies in opening up the possibility of dealing, creating, manipulating, and combining signal-flow graphs.
One has to get used to its aged syntax.

(sec-scide)=
## The Development Environment

The [SuperCollider (SC)](https://supercollider.github.io/) integrated development environment (IDE) is a Qt-based cross-platform application.
Code can be executed in a notebook-like manner, i.e., interactively using the REPL (Read–Eval–Print Loop).

```{figure} ../../figs/supercollider/ecosystem/ide.png
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

```{figure} ../../figs/supercollider/ecosystem/ide-tools.png
---
width: 600px
name: fig-ide-tools
---
Different **scide** tools for analyzing and observing what is going on.
One synth is running (a sine wave of 220 cycles per second).
```

These tools are depicted in {numref}`Fig. {number} <fig-ide-tools>`.
They can be used to observe and analyze the state of the server as well as the signal processing.
