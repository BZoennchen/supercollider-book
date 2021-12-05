# Drones

In this section we try to create an ambient drone sound.
Our basic wave front will be a [sawtooth wave](sec-sawtooth-wave).
The drone has a long attack and decay.
In fact, we start without an envelope.
This time we will use the ``SynthDef`` to define our drone synth.

```isc
(
SynthDef(\drone, {
    var sig, amp;
	amp = 0.5;
	sig = Saw.ar(\freq.kr(150)) * amp;
    Out.ar(0, sig);
}).play;
)
```

That's our basic [sawtooth wave](sec-sawtooth-wave) which does not sound very drone-like.
A drone has a lot of movement.
Our first step is to change the frequency of the drone over time but not too much.
Since we want this sine like wobble effect, we use a sine wave for the frequency modulation.
But to add additional movement, we modulate the frequency of the frequency modulation randomly:

```isc
(
SynthDef(\drone, {
    var sig, amp, freqmod;
	amp = 0.5;
	freqmod = SinOsc.kr(LFNoise0.kr(1)).range(1-\detune.kr(0.01), 1+\detune.kr(0.01));
	sig = Saw.ar(\freq.kr(150) * freqmod) * amp;
	Out.ar(0, sig);
}).play;
)
```

We can reduce the harshness by using a ``VarSaw`` instead of ``Saw``.
``VarSaw`` let's us modulate its ``width`` by which we can control how much it is shaped like a [triangle wave](sec-triangle-wave).

```isc
(
SynthDef(\drone, {
    var sig, amp, freqmod, widthmod;
	amp = 0.85;
	freqmod = SinOsc.kr(LFNoise0.kr(1)).range(1-\detune.kr(0.01), 1+\detune.kr(0.01));
	widthmod = SinOsc.kr(LFNoise0.kr(1)).range(0.35, 0.65);
	sig = VarSaw.ar(\freq.kr(150) * freqmod) * amp;
	Out.ar(0, sig);
}).play;
)
```

Let's duplicate to create some sort of unison:

```isc
(
SynthDef(\drone, {
    var sig, amp, freqmod, widthmod, n = 3;
	amp = 0.85;

	sig = Array.fill(n, {
		arg i;
		freqmod = SinOsc.kr(LFNoise0.kr(1)).range(1-\detune.kr(0.01), 1+\detune.kr(0.01));
		widthmod = SinOsc.kr(LFNoise0.kr(1)).range(0.35, 0.65);
		sig = VarSaw.ar((i+1)*\freq.kr(150) * freqmod) * (i+1).reciprocal;
	}) * amp;

	sig = Splay.ar(sig);
	sig = Balance2.ar(sig[0], sig[1], SinOsc.kr(LFNoise0.kr(0.1).range(0.05,0.2))*0.1);
    //sig;
	Out.ar(0, sig);
}).play;
)
```

TODO