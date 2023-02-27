# Building Sounds

## Frequency and Midinotes

Let $f$ be our frequency.
$f$ determines the pitch of a sound.
The pitch increases by one octave if we double the frequency $f$.
There are 12 keys on a pianos keyboard within one octave, this means that if we go up one note we increase $f$ by

$$
2^{1/12} \approx 1.059446
$$

which is approximately the value of

```isc
1.0.midiratio
```

We can also transform a midinote to frequency (cycles per seconds, i.e., cps) and vise versa by

```isc
75.midicps                                             // 622.25396744416
abs(76.midicps - (75.midicps * 2.pow(1/12))) < 0.0001; // true
76.midicps.cpsmidi                                     // 76
```

## Noise generation

Let us imagine we have a very basic sound of a simple sinewave.

```isc
(
SynthDef.new(\melo,{
    arg freq = 200;
    var sig;
    sig = SinOsc.ar(freq)!2 * 0.4;
    Out.ar(0, sig);
}).add;
)
Synth(\melo);
```

This is a quite boring sound.
A way to enrich it, is to add slightly detuned copies of the sinewave which change their frequency over time.
The noise oscillators ``LFNoiseX.ar(freq: freq)`` generate a juggeling signal which changes its amplitude inbetween the $[-1;1]$ uniformly distributed.
Between the changes, the amplitude stays constant (0), is interpolated linearly (1) or quadratically (2), compare {numref}`Figure {number} <fig-plot-LFNoiseX>`.

```isc
(
{[
    LFNoise0.ar(10),
    LFNoise1.ar(10),
    LFNoise2.ar(10)
]}.plot(4, bounds: Rect(100, 100, 1000, 600))
)
```

```{figure} ../../figs/plot-LFNoiseX.png
---
width: 800px
name: fig-plot-LFNoiseX
---
Plot of ``LFNoise0``, ``LFNoise1`` and ``LFNoise2`` over 4 seconds and a frequency of 10 Hz.
```

So let us create $n$ number of detuned sinewaves and adding them to the fundamental:

```isc
(
SynthDef.new(\melo,{
    arg freq = 300, detune = 0.5;
    var sig, n = 10, freqsL, freqsR;
	freqsL = freq * LFNoise2.ar({Rand(0.08, 0.11)}!n).bipolar(detune).midiratio;
	freqsR = freq * LFNoise2.ar({Rand(0.08, 0.11)}!n).bipolar(detune).midiratio;
	freqsR.postln;
	sig = (SinOsc.ar(freq)!2) + [SinOsc.ar(freqsL).sum, SinOsc.ar(freqsR).sum];
	Out.ar(0, sig * 1.0/(n+1));
}).add;
)
Synth(\melo);
```

``{Rand(lo, hi)}!n`` is a array containing ``n`` functions ``{Rand(lo, hi)}`` which are evaluated each time we execute the synth ``\melo``.
Is a ``UGen`` that ``Rand(lo, hi)`` generates a single random ``float`` value in uniform distribution from ``lo`` to ``hi``, see [Random distributions](sec-utility-distributions).

The function ``bipolar(x)`` ensures that each value is inbetween the interval [``-x``, ``x``].
In this case we could also just multiply the noise by ``detune``, since it is between [``-1``, ``1``].

To enrich a sound a good technique is to add detuned 


```isc
(
Array.new();
SynthDef.new(\melo,{
	arg freq = 200, atk = 0.002, sus = 0, rel = 1, detune = 0.015;
	var sig, env, sines, freqs;
	env = EnvGen.ar(Env(levels: [0,1,1,0], times: [atk,sus,rel], curve: [1,0,-6]), doneAction: Done.freeSelf);

	freqs = freq * LFNoise2.kr({Rand(0.08, 0.11)}!6).bipolar(detune).midiratio;
	sig = SinOsc.ar(freq: freq, mul: 0.4)!2;

	sines = freqs.collect({
		arg n;
		var tmp;
		tmp = SinOsc.ar(n);
		tmp = Pan2.ar(tmp, Rand(-0.9, 0.9));
		tmp = tmp.tanh;
		tmp;
	}).sum;

	sig = sig + sines;
	sig = sig * env;
	Out.ar(0, sig * 0.03);
}).add;
)
```


```isc
(
{
	var noise0 = LFNoise0.kr(1/3) * 4;
	var saw = Saw.ar([32,33]) * 0.2;
	var in = LocalIn.ar(2) * 7.5;
	var center = 2**noise0*300;
	//var center = 120;
	var bpf = BPF.ar(in+saw, center, rq: 0.1).distort;
	
	LocalOut.ar(a=CombN.ar(bpf,2,2,40));
	a;
}.play
)
```


```{admonition} Intervals and Pitches 
:name: remark-interval-vs-pitches
:class: remark
The actual pitches within a scale are less important than their relation, i.e. the *interval* between pitches/frequencies.
```

```{figure} ../../../figs/composing/piano-keys.png
---
width: 500px
name: fig-piano-keys
---
The notes of an octave mapped onto piano keys.
Each consecutive key is a multiple of $\sqrt[12]{2}$ apart.
The white keys give us the C major scale ([diatonic scale](sec-diatonic-scale)).
Above, one can see the number of semitones of each interval of the major scale.
```