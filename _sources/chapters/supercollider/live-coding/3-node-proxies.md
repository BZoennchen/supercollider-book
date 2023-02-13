(sec-node-proxies)=
# Node Proxies

[NodeProxy](https://doc.sccode.org/Classes/NodeProxy.html) objects (usually synth or event streams) can be replaced with other synths and event streams while they are played.
This replacement can be crossfaded automatically by setting up a ``fadeTime``.
Furthermore, the replacement time can be quantized.

```{admonition} Node Proxy
:name: def-node-proxy
:class: definition
A node proxy is a placeholder for something **playing on a server** that writes to a limited number of busses (e.g., a synth or an event stream).
```
After booting the server via ``s.boot``, we can create a new [NodeProxy](https://doc.sccode.org/Classes/NodeProxy.html) object and ``play`` it.

```isc
a = NodeProxy(); // define a node proxy
a.play();        // and play it to the hardware output
a.fadeTime = 2.0 // specify a 2 second fade time

// add the actual UGen graph to it and exchange it with another graph
a.source = { SinOsc.ar([350, 351.3], 0, 0.2) };
a.source = { Pulse.ar([350, 351.3] / 4, 0.4) * 0.2 }; // replace the synth
```

## Examples

In this subsection I will give you the code that has the same effect as the code in section [Proxy Space](sec-proxy-space) without additional explanations.
For a detailed discussion please look at section [Proxy Space](sec-proxy-space).

```isc
~sound = NodeProxy();
~sound.fadeTime = 4.0;
~sound.source = {Resonz.ar(Pulse.ar(5), Array.exprand(4, 120, 2500), 0.005).sum!2};
~sound.play;
```

```isc
~sine = NodeProxy();
~sine.source = {SinOsc.ar(\freq.kr(333))*0.3!2};
~sine.play;
~sine.fadeTime = 2.0;
~sine.xset(\freq, 190);
~sine.set(\freq, 100);
~sine.gui; // we can make use of the same gui
```

```isc
~sine.nodeMap.postln;
```

```isc
~sine = NodeProxy();
~amp = NodeProxy();
~tri = NodeProxy();

~sine.source = {~amp * SinOsc.ar(350)*[1.0,1.003]};
~sine.play;

~amp.source = {SinOsc.kr(3)*0.25};

~tri.source = {~amp * LFTri.ar(350)*[1.0,1.003]};
~tri.play;
```

```isc
~sine = NodeProxy();
~amp = NodeProxy();
~tri = NodeProxy();

~sine.source = {\amp.kr(0.25) * SinOsc.ar(350)*[1.0,1.003]};
~tri.source = {\amp.kr(0.25) * LFTri.ar(350)*[1.0,1.003]};
~sine.play;
~tri.play;

~amp.source = {SinOsc.kr(3)*0.25};

~amp <>>.amp ~sine; // shorthand for ~sine.set(\amp, ~amp);
~tri <<>.amp ~amp;  // shorthand for ~tri.set(\amp, ~amp);
```

```isc
n = 16; // 1/16 beat
b = 60.0; // bpm

~clock = NodeProxy();
~trigger1 = NodeProxy();
~trigger2 = NodeProxy();
~env1 = NodeProxy();
~env2 = NodeProxy();
~bleep = NodeProxy();
~bass = NodeProxy();

~clock.source = {Impulse.kr(n * b / 60.0)}

~trigger1.source = {PulseDivider.kr(~clock, 4.0)}

~trigger2.source = {PulseDivider.kr(~clock, 8.0)}

(
~env1.source = {
    Linen.kr(
        gate: ~trigger1, 
        doneAction: Done.none, 
        releaseTime: 0.05);
};

~env2.source = {
    Linen.kr(
        gate: ~trigger2, 
        doneAction: Done.none, 
        releaseTime: 0.05);
};
)

~bleep.source = {SinOsc.ar(TChoose.kr(~trigger1, [300, 600, 666, 900]))!2 * 0.5 * ~env1;}
~bleep.play;

~bass.source = {SinOsc.ar(TChoose.kr(~trigger2, [70, 65, 67]))!2 * 0.5 * ~env2;}
~bass.play;
```

```isc
~out = NodeProxy();
~out[0] = {SinOsc.ar(\freq.kr(300)) * 0.25};
~out[10] = {LFTri.ar(\freq.kr(500)) * 0.25};
~out.sources.do(_.postln)
~out.play;
```

```isc
~out = NodeProxy();
~out[0] = {SinOsc.ar(\freq.kr(300))};
~out[10] = \filter -> {arg in; in * SinOsc.ar(\freq.kr(1)) * 0.25};
~out.play;

~out.set(\wet10, 0.5);
```

```isc
~out = NodeProxy();
~out.fadeTime = 2.0;
~out[0] = {Dust.ar([3, 2.5])};
~out[10] = \filter -> {arg in; Ringz.ar(in, freq: \freq.kr(300), decaytime: 0.1) * 0.55};
~out[20] = \filterIn -> {arg in; FreeVerb.ar(in, 0.6, 0.9, 0.8)};
~out[30] = \filterIn -> {arg in; LPF.ar(in: in, freq: \cutofffreq.kr(21000))};
~out.play;

~randFreq = NodeProxy();
~randFreq.source = {LFNoise1.kr(1).range(200, 300)};

~randcutoff = NodeProxy();
~randcutoff.source = {LFNoise1.kr(0.3).range(10000, 4000)};

~out <<>.freq ~randFreq;
~out <<>.cutofffreq ~randcutoff;
```

```isc
~test_beep = NodeProxy();

~test_beep.source = Synth(\beep);

(
~test_beep.source = Pbind(
    \instrument, \beep, 
    \freq, Pseq([Pgeom(100, 2, 5), Pgeom(150, 2, 5)], inf),
    \dur, 0.2,
    \legato, 0.02);
)
```