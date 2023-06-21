(sec-proxy-space)=
# Proxy Space

From the three possibilities ([NoteProxy](https://doc.sccode.org/Classes/NoteProxy.html), [Ndef](https://doc.sccode.org/Classes/Ndef.html), and [ProxySpace](https://doc.sccode.org/Classes/ProxySpace.html)) to interact with server nodes, I prefer the [ProxySpace](https://doc.sccode.org/Classes/ProxySpace.html).
Note however, that you can do everything also with the two other methods.
It is just a stylistic choice.

```{admonition} Proxy Space
:name: def-proxy-space
:class: definition
A proxy space is an [Environments](sec-environments) consisting of node proxies only (instead of normal variables).
```

The advatange to use [ProxySpace](https://doc.sccode.org/Classes/ProxySpace.html) is a shorter and often cleaner syntax.
The downside is that we can no longer use *environment variables* for client side code.
Note however that we can still use *global variables*, e.g. ``a, b, c, d, ...``.

A proxy space is an [Environments](sec-environments), i.e., a collection of things that can be accessed by name.
However, each *environment variable* of a proxy space is a node proxy -- it returns placeholders on demand!
Therefore, a proxy space hides some of the functionality of JITLib.
It makes it easier and neater when it comes to creating or rewriting node proxies.
Using a proxy space frees us from dealing with [Ndef](https://doc.sccode.org/Classes/Ndef.html) or [NoteProxy](https://doc.sccode.org/Classes/NoteProxy.html) explicitly, but we have to deal with it implicitly instead!

## Initialization

To push a proxy space onto the stack, we first have to boot the server because the proxy space lives and operates on an audio server instance of *scsynth*.
The following line suffice to push an environment representing the server side proxy space onto the stack:

```isc
p = ProxySpace.push(s.boot); // s.boot returns s
```

If you already booted the audio server use 

```isc
p = ProxySpace.push(s);
```

instead.

## Usage

If we re-evaluate ``currentEnvironment``, we can see that we are indeed in an empty proxy space.
There are no "classical" environment variables within the proxy space.
If we access a variable as before (with the tilde ``~``), it becomes a node proxy instead, i.e., a placeholder for something that runs on the audio server.
We can still use *global variables*, that is, single letters except for ``s``.
If we need more variables, we can fix this problem but let us move on for now.

Let us create a first node proxy and lets play it.

```isc
~sound = {Resonz.ar(Pulse.ar(5), Array.exprand(4, 120, 2500), 0.005).sum!2};
~sound.fadeTime = 4.0;
~sound.play;
```

We can stop it and modify it on the fly by changing the function.
Since there is (client-side) randomness at play, the sound changes each time we re-evaluate the function.
To achieve a smoother transition between changes, we can define a ``fadeTime``.

We can also define a ``fadeTime`` for the whole proxy space, which will then be used as the default fade time if nothing else is specified.

```isc
p.fadeTime = 3.0;
```

We can play around with the proxy and manipulate its function and values, but we can not change the number of output buses the running proxy requires.
Changing a mono signal into a stereo signal on-the-fly is impossible.

```{admonition} Bus Changes
:name: attention-proxy-bus-changes
:class: attention
You can not change the number of required busses of a running proxy.
```

If we execute the following code line, the audio server warns us of our mistake

```isc
~monosine = {SinOsc.ar(250)*0.3};
~monosine.play;
~monosine = {SinOsc.ar(250)*0.3!2};
```

by providing us the following message:

``NodeProxy.audio(localhost, 1): wrapped channels from 2 to 1 channels``

The sound disappears after executing the third line.

```{admonition} Number of Channels
:name: attention-proxy-number-of-channels
:class: remark
Playing an empty proxy will set its number of output busses to two (stereo) by default.
```

Node proxies can be played ``play(fadeTime: 2)``, stopped ``stop(2)``, paused ``pause`` and resumed ``resume``.
The latter two methods do not offer a fade time parameter, and for ``play``, the fade time has to be explicitly named.
One can not play a paused proxy and one can not resume a stopped proxy.

We can set these arguments without touching the proxy if we specify arguments using named controls.

```isc
~sine = {SinOsc.ar(\freq.kr(333))*0.3!2};
~sine.play;
~sine.fadeTime = 2.0;
~sine.xset(\freq, 190);
~sine.set(\freq, 100);
~sine.gui; // we can make use of the same gui
```

Using ``set`` will change the value immediately while ``xset`` uses the ``fadeTime`` to crossfade between the current and the new value.

We can inspect the note proxy of our choice by posting its ``nodeMap``.

```isc
~sine.nodeMap.postln;
```

## Routing Signals

Of course, we can combine multiple proxies by building a signal-flow graph on the fly.

```isc
~sine = {~amp * SinOsc.ar(350)*[1.0,1.003]};
~sine.play;

~amp = {SinOsc.kr(3)*0.25};

~tri = {~amp * LFTri.ar(350)*[1.0,1.003]};
~tri.play;
```

As you can see, the output of one proxy can be used as an argument of multiple other proxies.
Note that we do not ``play`` the ``~amp`` proxy because this would route the signal to the output.

We can use syntactical sugger to do the same in an even more modular and clean way by using either ``source <>>.[argname] target`` or ``target <<>.[argname] source`` and normal arguments.
This operation is inspired by the binary composition operator ``<>`` defined on [functions](sec-function-composition), streams and patterns.

```isc
~sine = {\amp.kr(0.25) * SinOsc.ar(350)*[1.0,1.003]};
~tri = {\amp.kr(0.25) * LFTri.ar(350)*[1.0,1.003]};
~sine.play;
~tri.play;

~amp = {SinOsc.kr(3)*0.25};

~amp <>>.amp ~sine; // shorthand for ~sine.set(\amp, ~amp);
~tri <<>.amp ~amp;  // shorthand for ~tri.set(\amp, ~amp);
```

````{admonition} Bus Changes
:name: attention-node-proxy-composition
:class: attention
The composition operator ``<<>`` does only work for node proxies, i.e., it does not work for constant values. 
The following will **not** work:

```isc
~tri <<>.amp 0.5;
```

````

The advantages of modularity is that one can repatch control and audio rate signals on the fly and, as we saw, one signal can be easily patched to multiple node proxies at once.

Let us try to simulate a global clock by using the [Impulse](https://doc.sccode.org/Classes/Impulse.html) unit generator.
Furthermore, let us try to trigger certain sounds at specific beats.
Listen to and experiment with the following code:

```isc
n = 16; // 1/16 beat
b = 60.0; // bpm

~clock = {Impulse.kr(n * b / 60.0)}

~trigger1 = {PulseDivider.kr(~clock, 4.0)}

~trigger2 = {PulseDivider.kr(~clock, 8.0)}

(
~env1 = {
    Linen.kr(
        gate: ~trigger1, 
        doneAction: Done.none, 
        releaseTime: 0.05);
};

~env2 = {
    Linen.kr(
        gate: ~trigger2, 
        doneAction: Done.none, 
        releaseTime: 0.05);
};
)

~bleep = {SinOsc.ar(TChoose.kr(~trigger1, [300, 600, 666, 900]))!2 * 0.5 * ~env1;}
~bleep.play;

~bass = {SinOsc.ar(TChoose.kr(~trigger2, [70, 65, 67]))!2 * 0.5 * ~env2;}
~bass.play;
```

It is not very musical and kind of boring but it demonstrate how we can route different node proxies together.
[PulseDivider](https://doc.sccode.org/Classes/PulseDivider.html) comes in handy because it outputs an impuls every time it receives a certain amount of impulses.
Thus we can divide pulses into fewer one per beat.
Also note that our ``doneAction`` of the envolved envelopes is set to ``Done.none`` because we do not want to free the synsth -- it is running all the time.
[TChoose](https://doc.sccode.org/Classes/TChoose.html) chooses randomly one of the values of the array whenever it is triggered.
Our clock ``~clock`` runs at 60 beats per minutes times 16 such that we divide each beat into 16 parts.

## Slots and Node Proxy Roles

Often we want to chain signals and effects in a series together such that signal $i$ can manipulate signal $i+1$.
For example, one might want to add a reverb effect to a percussive sawtooth signal.
By indexing the *environment variable*, i.e. our node proxy, we can use the slots of the proxy to chain singals together.

Assining multiple [UGens](sec-ugens) to multiple slots will add all these signals consecutively together.
We do not have to use consecutive slot numbers.
It is in fact a good practice to leave gaps between occupied slots such that we can bring in another effect between two already established synths.

These lines result in a sound produced of a sine and sawtooth wave added together.

```isc
~out[0] = {SinOsc.ar(\freq.kr(300)) * 0.25};
~out[10] = {LFTri.ar(\freq.kr(500)) * 0.25};
~out.play;
```

If we set the ``\freq`` argument for the node proxy it will be set for all its slots.

```isc
~out.set(\freq, 300) // changes \freq for all slots
```

The following will **not** work.

```isc
~out[10].set(\freq, 300) // error!
```

Adding signals together by using slots seems not very useful.
However, the story does not end here.
Slots become much more useful if we combine them with [NodeProxy roles](https://depts.washington.edu/dxscdoc/Help/Reference/NodeProxy_roles.html).

Similar to [adverbs](sec-array-adverbs), which I discuss as part of the [Array](sec-array) section, roles allow us to specify how a source, i.e. a synth, for a [NodeProxy](https://doc.sccode.org/Classes/NodeProxy.html) is being used.
A specific role is associated by a specific symbol and a new proxy source object.
For example, instead of adding signals together, the ``\filter`` and ``filterIn`` use the signal (coming from the slots with smaller indices) as input for a filter.
The filter can be any unit generator graph.
This sounds vague, so let's look at an example right away.

Listen to the following:

```isc
~out[0] = {SinOsc.ar(\freq.kr(300))};
~out[10] = \filter -> {arg in; in * SinOsc.ar(\freq.kr(1)) * 0.25};
~out.play;
```

The sine wave's amplitude is modulated by ``~out[10]``.
When we filter a signal, we get the so called *wet signal* while the original is the *dry* one.
If we go 100% wet, the dry signal disappears.
Let us try 50% wet:

```isc
~out.set(\wet10, 0.5);
```

We can clearly hear both signals.
To set the wet persentage of slot ``i``, you can use ``.set(\weti, value);`` on the proxy node.
In the folling I tried to recreate the sound of a firework:

```isc
~out.fadeTime = 2.0;
~out[0] = {Dust.ar([3, 2.5])};
~out[10] = \filter -> {arg in; Ringz.ar(in, freq: \freq.kr(300), decaytime: 0.1) * 0.55};
~out[20] = \filterIn -> {arg in; FreeVerb.ar(in, 0.6, 0.9, 0.8)};
~out[30] = \filterIn -> {arg in; LPF.ar(in: in, freq: \cutofffreq.kr(21000))};
~out.play;
```

[Dust](https://doc.sccode.org/Classes/Dust.html) generates random impulses such that the density of that impulses approximate its frequency arguement, i.e. 3 impulses per second for the left and 2.5 impulses for the right speaker.
[Ringz](https://doc.sccode.org/Classes/Ringz.html) models resonates at a frequency of ``300`` herz.
We add a reverb effect to give the sound some spacial depth.
The low pass filter has no effect since the cutoff frequency is very high.

Let us now introduce modulation for the resonance frequency and the cutoff filter to introduce even more spatial differences such that we get the feeling the firework happens around us in multiple streets.

```isc
~randFreq = {LFNoise1.kr(1).range(200, 300)};
~randcutoff = {LFNoise1.kr(0.3).range(10000, 4000)};

~out <<>.freq ~randFreq;
~out <<>.cutofffreq ~randcutoff;
```

The change in cutoff resonance and cutoff frequency happens continuously.

In combination, JITLib and the proxy space offer extreme versatility.
They make live coding easier and very flexible.
It gets more interesting when used with [pattern](sec-pattern), and one has multiple [Pbinds](https://doc.sccode.org/Classes/Pbinds.html) sounding together.

## SynthDefs and Pbinds

What if we want to use our carefully crafted [SynthDefs](sec-synths) in a live programming setup?
Well we can bind them to a node proxy.
Let us first create the most simple synth definition we get come up with.

```isc
(
SynthDef(\sine, {
    arg freq = 440, bus = 0, gate=1, amp=0.3;
    var env, sig;
    sig = SinOsc.ar(freq!2) * amp;
    Out.ar(bus, sig);
}).add;
)
```

We ``add`` the definition to the server.
Now bind the synth to a proxy node.

```isc
~test_beep = \sine; // plays the synth
~test_beep.set(\freq, 200);
```

The following does **not** work:

```isc
~test_beep = Synth(\sine);
~test_beep.set(\freq, 200);
```

Most of the time you will not use synths in this way but combine them with an [event player](sec-event-player), i.e., [Pbind](https://doc.sccode.org/Classes/Pbind.html).

Let us create a gated more useful synth definition.

```isc
(
SynthDef(\beep, {
    arg freq = 440, bus = 0, gate=1, amp=0.3;
    var env, sig;
    env = EnvGen.ar(
        Env(times: [0.01, 0.1], curve: [5, -5]), 
        gate: gate, 
        doneAction: Done.freeSelf);
    sig = SinOsc.ar(freq!2) * env * amp;
    Out.ar(bus, sig);
}).add;
)
```

Now we use a [Pbind](https://doc.sccode.org/Classes/Pbinds.html) to play a melody.

```isc
(
~test_beep = Pbind(
    \instrument, \beep, 
    \freq, Pseq([Pgeom(100, 2, 5), Pgeom(150, 2, 5)], inf),
    \dur, 0.2,
    \legato, 0.02);
)
```

Note that if you set an argument for the proxy node it will be used regardless of the argument with the same name of the [Pbind](https://doc.sccode.org/Classes/Pbinds.html).
You can not override it by re-evaluating the [Pbind](https://doc.sccode.org/Classes/Pbinds.html).

```isc
~test_beep.set(\freq, 200);
```

You can get rid of the 'parent' argument by setting it to ``nill``.

```isc
~test_beep.set(\freq, nil);
```

## Synchronization

In our second routing example we synchronzed our envelopes and [TChoose](https://doc.sccode.org/Classes/TChoose.html) unit generator by a global clock realized by an [Impulse](https://doc.sccode.org/Classes/Impulse.html) unit generator.
As you saw, this opens up jet another coding style.
A more straightforward way is to use [Pbinds](https://doc.sccode.org/Classes/Pbinds.html) synchronized by a [TempoClock](https://doc.sccode.org/Classes/TempoClock.html) which I describe in section [Clocks](sec-clocks).