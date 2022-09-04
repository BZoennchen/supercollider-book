(node-proxy-definitions)=
# Node Proxy Definition

[Ndef](https://doc.sccode.org/Classes/Ndef.html) is a node proxy definition.
It gives us a handy way to define a new node proxy.
``Ndef`` registers synths by key, i.e., all accesses to the registered synths go through the ``Ndef`` class via that key.

```isc
Ndef(\a).play;         // play to the hardware output
Ndef(\a).fadeTime = 2; // specify a 2 second fade time

// add the actual UGen graph to it and exchange it with another graph
Ndef(\a, { SinOsc.ar([350, 351.3], 0, 0.2) });
Ndef(\a, { Pulse.ar([350, 351.3] / 4, 0.4) * 0.2 });
```

Behind every ``Ndef`` there is one single instance of [ProxySpace](https://doc.sccode.org/Classes/ProxySpace.html) per server used (usually just the one for the default server).
This proxy space keeps default values for the proxies that can be set.

Combining ``Ndef`` with a [NdefGui](https://doc.sccode.org/Classes/NdefGui.html), a gui for a ``NodeProxy`` or ``Ndef``, provides us with a nice graphical interface to experiment with different arguments of, for example, a ``SynthDef``.
The gui generator automatically introduces a slide for each controllable argument.
We can even specify the range of the argument using a [Spec](https://doc.sccode.org/Classes/Spec.html).

```isc
(
Spec.add(\freq, [40, 4000]); // specify the range of the frequency argument
Spec.add(\amp, [0.0, 1.0]);  // specify the range of the apmlitude argument
Ndef(\sine, {SinOsc.ar(\freq.kr(300)) * \amp.kr(0.7) }).gui;
)
```

That is quite nice to experiment with!
Sometimes I will use node proxy definitions because of this ability to play around without writing tons of code.

## Examples

In this subsection I will give you the code that has the same effect as the code in section [Proxy Space](sec-proxy-space) without additional explanations.
For a detailed discussion please look at section [Proxy Space](sec-proxy-space).

```isc
Ndef(\sound).fadeTime = 4.0;
Ndef(\sound, {Resonz.ar(Pulse.ar(5), Array.exprand(4, 120, 2500), 0.005).sum!2});
Ndef(\sound).play;
```

```isc
Ndef(\sine, {SinOsc.ar(\freq.kr(333))*0.3!2});
Ndef(\sine).play;
Ndef(\sine).fadeTime = 2.0;
Ndef(\sine).xset(\freq, 190);
Ndef(\sine).set(\freq, 190);
Ndef(\sine).gui
```

```isc
Ndef(\sine).nodeMap.postln;
```

```isc
Ndef(\sine, {Ndef(\amp) * SinOsc.ar(350)*[1.0,1.003]});
Ndef(\sine).play;

Ndef(\amp, {SinOsc.kr(3)*0.25});

Ndef(\tri, {Ndef(\amp) * LFTri.ar(350)*[1.0,1.003]});
Ndef(\tri).play;
```

```isc
Ndef(\sine, {\amp.kr(0.25) * SinOsc.ar(350)*[1.0,1.003]});
Ndef(\tri, {\amp.kr(0.25) * LFTri.ar(350)*[1.0,1.003]});
Ndef(\sine).play;
Ndef(\tri).play;

Ndef(\amp, {SinOsc.kr(3)*0.25});

Ndef(\amp) <>>.amp Ndef(\sine);
Ndef(\tri) <<>.amp Ndef(\amp);
```

```isc
n = 16; // 1/16 beat
b = 60.0; // bpm

Ndef(\clock, {Impulse.kr(n * b / 60.0)});
Ndef(\trigger1, {PulseDivider.kr(~clock, 4.0)});
Ndef(\trigger2, {PulseDivider.kr(~clock, 8.0)});

(
Ndef(\env1, {
    Linen.kr(
        gate: ~trigger1, 
        doneAction: Done.none, 
        releaseTime: 0.05);
});

Ndef(\env2, {
    Linen.kr(
        gate: ~trigger2, 
        doneAction: Done.none, 
        releaseTime: 0.05);
});
)

Ndef(\beep, {SinOsc.ar(TChoose.kr(~trigger1, [300, 600, 666, 900]))!2 * 0.5 * ~env1});
Ndef(\beep).play;

Ndef(\bass, {SinOsc.ar(TChoose.kr(~trigger2, [70, 65, 67]))!2 * 0.5 * ~env2});
Ndef(\bass).play;
```

```isc
Ndef(\out)[0] = {SinOsc.ar(\freq.kr(300)) * 0.25};
Ndef(\out)[10] = {LFTri.ar(\freq.kr(500)) * 0.25};
Ndef(\out).sources.do(_.postln);
Ndef(\out).play;
```

```isc
Ndef(\out)[0] = {SinOsc.ar(\freq.kr(300))};
Ndef(\out)[10] = \filter -> {arg in; in * SinOsc.ar(\freq.kr(1)) * 0.25};
Ndef(\out).play;

Ndef(\out).set(\wet10, 0.5);
```

```isc
Ndef(\out).fadeTime = 2.0;
Ndef(\out)[0] = {Dust.ar([3, 2.5])};
Ndef(\out)[10] = \filter -> {arg in; Ringz.ar(in, freq: \freq.kr(300), decaytime: 0.1) * 0.55};
Ndef(\out)[20] = \filterIn -> {arg in; FreeVerb.ar(in, 0.6, 0.9, 0.8)};
Ndef(\out)[30] = \filterIn -> {arg in; LPF.ar(in: in, freq: \cutofffreq.kr(21000))};
Ndef(\out).play;

Ndef(\randFreq, {LFNoise1.kr(1).range(200, 300)});
Ndef(\randcutoff, {LFNoise1.kr(0.3).range(10000, 4000)});

Ndef(\out) <<>.freq Ndef(\randFreq);
Ndef(\out) <<>.cutofffreq Ndef(\randcutoff);
```

```isc

(
SynthDef(\beep, {
    arg freq = 440, bus = 0, gate=1, amp=0.3;
    var env, sig;
    env = EnvGen.ar(Env(times: [0.01, 0.1], curve: [5, -5]), gate: gate, doneAction: Done.freeSelf);
    sig = SinOsc.ar(freq!2) * env * amp;
    Out.ar(bus, sig);
}).add;
)

Ndef(\test_beep, Synth(\beep));
Ndef(\test_beep, \beep);

(
Ndef(\test_beep, 
    Pbind(
        \instrument, \beep, 
        \freq, Pseq([Pgeom(100, 2, 5), Pgeom(150, 2, 5)], inf),
        \dur, 0.2,
        \legato, 0.02));
)
```