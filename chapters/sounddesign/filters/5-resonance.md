(sec-resonance)=
# Responses and Resonance

To bring dynamic into the sound by a filter, we can do the obvious: change the cuttoff frequency over time!
Let us try this with a low pass filter:

```isc
(
Spec.add(\modfreq, [0, 1000]);
Spec.add(\freq, [0, 1000]);
Spec.add(\mincutoff, [5, 1000]);
Spec.add(\maxcutoff, [5, 1000]);

Ndef(\filtering, {
    var sig = Saw.ar(\freq.kr(400)) ! 2 * 0.5;
    var cuttoff = SinOsc.ar(\modfreq.kr(10)).range(\mincutoff.kr(100), \maxcutoff.kr(1000));
    sig = LPF.ar(sig, cuttoff);
}).play;
)

Ndef(\filtering).gui;
```

Almost all physical objects resonate.
Or, to put it another way, almost all objects will vibrate naturally at certain frequencies.
What happens to musical objects such as a string when we do not play/pluck them but they are in an environment where sound is generated.
In other words: how does such an object interact with vibrations of other objects?

What we observe in that case is **resonance**!
If the musical object is excited by frequencies that coincide with its natural resonant frequencies, then it will vibrate in sympathy with the source oscillator.
Otherwise it will approximately stand still. 
How a musical instrument resonate has a great effect on the color of its sound ([timbre](sec-timbre)).

Resonance filters boost certain frequencies, making the harmonics at those frequencies louder than they were in the input signal.
The effect sounds like resonance. 
Therefore, resonance filters emulate resonance.

Which frequencies are boosted?
For most resonance filters, the frequencies near the cutoff frequency are boosted.
In ``sclang`` the [UGens](def-ugen) realizing a resonance filter start with an ``R``, for example, ``RLPF`` is the *resonance low pass filter*.

```isc
(
Spec.add(\modfreq, [0, 1000]);
Spec.add(\freq, [0, 1000]);
Spec.add(\mincutoff, [5, 1000]);
Spec.add(\maxcutoff, [5, 1000]);
Spec.add(\bandwidth, [5, 100]);

Ndef(\filtering, {
    var sig = Saw.ar(\freq.kr(400)) ! 2 * 0.5;
    var cuttoff = SinOsc.ar(\modfreq.kr(10)).range(\mincutoff.kr(100), \maxcutoff.kr(1000));
    sig = RLPF.ar(sig, cuttoff, rq: \bandwidth.kr(100) / cuttoff);
}).play;
)
Ndef(\filtering).gui;
```

Try different values especially for the bandwidth.
A small bandwidth will result in a strong effect.

In fact, if the bandwidth is very small, the effect becomes so pronounced that the high and low frequencies disappear from the signal and another effect occurs: the filter begins to oscillate at its cutoff frequency.
The result is a powerful unnatural sound unique to the electronic synthesizer.