(sec-live-coding)=
# Live Coding

[SuperCollider](https://supercollider.github.io/) supports live programming via its powerful [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html).
It allows the use of dynamic modification and interconnection of proxies.
Quoting its documentation:

>Just in time programming (or: conversational programming, live coding, on-the fly-programming, interactive programming) is a paradigm that includes the programming actively in the program's operation. Here, a program is not taken as a tool that is made first to be productive later, but instead as a dynamic construction process of description and conversation. Writing code becomes an intergral part of musical or experimental practice.

In a live programming environment, we often want to use something before it is there to set up our setting in a non-linear way.
For this reason, the JITLib of SuperCollider offers us different ways to define proxies.
A proxy is a placeholder that is often used to operate on something that does not yet exist.
For example, an *OutputProxy* is used to represent multiple outputs of a UGen, even if only one UGen is created eventually.

Proxies can be redefined, making them highly flexible and dynamic.
They can refer to functions, patterns, or tasks and work at either audio ``ar`` or control ``kr`` rate.

## Node Proxy

NodeProxy objects (usually synth or event streams) can be replaced with other synths and event streams while they are played.
This replacement can be crossfaded automatically by setting up a ``fadeTime``.
Furthermore, the replacement time can be quantized.

A node proxy is a placeholder for something **playing on a server** that writes to a limited number of busses (e.g., a synth or an event stream).
After booting the server via ``s.boot``, we can create a new [NodeProxy](https://doc.sccode.org/Classes/NodeProxy.html) object and ``play`` it.

```isc
a = NodeProxy().play; // play to the hardware output
a.fadeTime = 2.0 // specify a 2 second fade time
a.source = { SinOsc.ar([350, 351.3], 0, 0.2) };
a.source = { Pulse.ar([350, 351.3] / 4, 0.4) * 0.2 }; // replace the synth
```

[Ndef](https://doc.sccode.org/Classes/Ndef.html) is a node proxy definition, i.e., a handy way to define a new node proxy.
``Ndef`` registers synths by key, i.e., all accesses to the registered synths go through the ``Ndef`` class via that key.

```isc
Ndef(\a).play; // play to the hardware output
Ndef(\a).fadeTime = 2; // specify a 2 second fade time
Ndef(\a, { SinOsc.ar([350, 351.3], 0, 0.2) });
Ndef(\a, { Pulse.ar([350, 351.3] / 4, 0.4) * 0.2 }); // replace the synth
```

Behind every ``Ndef`` there is one single instance of [ProxySpace](https://doc.sccode.org/Classes/ProxySpace.html) per server used (usually just the one for the default server).
This proxy space keeps default values for the proxies that can be set.

Sometimes I will use node proxy definitions because they offer a neat ``gui`` to play around with.
The GUI generator automatically introduces a slide for each controllable argument.
We can even specify the range of the argument using a [Spec](https://doc.sccode.org/Classes/Spec.html):

```isc
(
Spec.add(\freq, [40, 4000]); // specify the range of the frequency argument
Spec.add(\amp, [0.0, 1.0]);  // specify the range of the apmlitude argument
Ndef(\sine, {SinOsc.ar(\freq.kr(300)) * \amp.kr(0.7) }).gui;
)
```

That is quite nice to experiment with!

## Proxy Space

A proxy space is an [Environments](https://doc.sccode.org/Classes/Environment.html), i.e., a collection of things that can be accessed by name.
However, each *environmental variable* of a proxy space is a node proxy -- it returns placeholders on demand!
Therefore, a proxy space hides some of the functionality of JITLib.
It makes it easier and neater when it comes to creating or rewriting node proxies.
Using a proxy space frees us from dealing with ``Ndef`` or ``NodeProxy`` explicitly, but we have to deal with it implicitly instead!

When we start the SuperCollider IDE, it automatically creates an environment that can be evaluated by the following line:

```isc
currentEnvironment;
```

If this is your first evaluated command, the environment should be empty.
This environment contains variables, more specifically *environment variables*.
Something preceded by a tilde can define these variables:

```isc
~number = 100;
```

If we re-evaluate the first statement, we can observe that ``currentEnvironment`` contains the value ``100`` that can be accessed via the name ``number``.
In fact ``~number`` is a shortcut for 

```isc
currentEnvironment.at(\number);
```

and an assignment like ``~number = 100;`` stands for

```isc
currentEnvironment.put(\number, 100);
```

To switch to proxy space, we first have to boot the server. 
Then we can push the new environment, which replaces the current one.
The following line suffice:

```isc
p = ProxySpace.push(s.boot);
```

If you already booted the audio server use 

```isc
p = ProxySpace.push(s);
```

instead.

If we re-evaluate ``currentEnvironment``, we can see that we are indeed in an empty proxy space.
There are no "classical" environment variables within the proxy space.
If access a variable as before (with the tilde ``~``), it becomes a proxy instead, i.e., a placeholder for something.
We can still use *global variables*, that is, single letters except for ``s``.
If we need more variables, we can fix this problem but let us move on for now.

```isc
~sound = {Resonz.ar(Pulse.ar(5), Array.exprand(4, 120, 2500), 0.005).sum!2};
~sound.play;
~sound.fadeTime = 4.0;
```

We can stop it and modify it on the fly by changing the function.
Since there is (client-side) randomness at play, the sound changes each time we re-evaluate the function.
To achieve a smoother transition between changes, we can define fade time.

We can also define a fade time for the whole proxy space, which will then be used as the default fade time if nothing else is specified.

```isc
p.fadeTime = 3.0;
```

We can play around with the proxy and manipulate its function and values, but we can not change one thing!
We can not change the number of output buses the running proxy requires.
Changing a mono signal into a stereo one is not possible on-the-fly.

```{admonition} Bus Changes
:name: attention-proxy-bus-changes
:class: attention
You can not change the required busses of a running proxy.
```

If we execute the following code line by the audio server warns us

```isc
~monosine = {SinOsc.ar(250)*0.3};
~monosine.play;
~monosine = {SinOsc.ar(250)*0.3!2};
```

with the following message

>NodeProxy.audio(localhost, 1): wrapped channels from 2 to 1 channels

and the sound disappear after executing the third line.
Playing an empty proxy will set its number of output busses to two (stereo).

Proxies can be played ``play(fadeTime: 2)``, stopped ``stop(2)``, paused ``pause`` and resumed ``resume``.
The latter two methods do not offer a fade time parameter, and for ``play``, the fade time has to be explicitly named.
One can not play a paused proxy and can not resume a stopped one.

We can set these arguments without touching the proxy if we specify arguments using named controls.

```isc
~sine = {SinOsc.ar(\freq.kr(333))*0.3!2};
~sine.play;
~sine.fadeTime = 2.0;
~sine.xset(\freq, 190);
~sine.set(\freq, 100);
~sine.gui; // we can make use of the same gui
```

Using ``set`` will change the value immediately while ``xset``uses the ``fadeTime`` to crossfade between the current and the new value.
Of course, we can combine multiple proxies by building a signal-flow graph on the fly.

```isc
~sine = {~amp * SinOsc.ar(350)*[1.0,1.003]};
~sine.play;
~amp = {SinOsc.kr(3)*0.5};
```

The output of one proxy can be the input of multiple other proxies.
The combination JITLib and the proxy space offers extreme versatility and makes live coding easier and very flexible.
It gets more interesting when used with [pattern](sec-pattern), and one has multiple ``Pbinds`` sounding together.

TODO!

## Live Loops

[Sonic Pi](https://github.com/sonic-pi-net/sonic-pi) uses the concept of *live loops*, i.e., named threaded loops that can be synchronized and updated on the fly.
I found *live loops* extremely fun and useful, especially to explore new rythms and melodies.
Is there something similar in SuperCollider?
The answer is yes!

[Tdef](https://doc.sccode.org/Classes/Tdef.html) is part of the SuperCollider's [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html) and allows us to register *tasks* by key.
Registered tasks can be replaced with other task **while playing**.
The old task and its replacement can automatically crossfade and the repalcement time can be quantized.

Evaluate the following code, change the message and re-evaluate the code.
Observe the post window.

```isc
(
Tdef(\melody, {loop{
    "test".postln;
    0.25.wait;
}}).play;
)
```

This is great!
Let us combine ``Tdef`` with [Patterns](sec-pattern) play a melody that we can change on the fly:

```isc
(
Tdef(\melody, {
    var notes = Pseq([65, 70, 55, 63, 55, 70], inf).asStream;
    loop{
        Synth(\beep, [\freq: notes.next.midicps]);
        0.25.wait;
    }
}).play;
)
```

The same can be accomplished using a [TaskProxy](https://doc.sccode.org/Classes/TaskProxy.html).

```isc
~melody = TaskProxy().play;
(
~melody.source = {
    var notes = Pseq([65, 70, 55, 63, 55, 70], inf).asStream;
    loop{
        Synth(\beep, [\freq: notes.next.midicps]);
        0.25.wait;
    }
};
)
```