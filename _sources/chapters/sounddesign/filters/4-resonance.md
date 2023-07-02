(sec-resonance)=
# Responses and Resonance

To introduce dynamism into the sound through a filter, we can take the most straightforward approach: altering the cutoff frequency over time! 
Let's try this with a low-pass filter:

```isc
(
Spec.add(\modfreq, [0, 1000]);
Spec.add(\freq, [0, 1000]);
Spec.add(\mincutoff, [5, 1000]);
Spec.add(\maxcutoff, [5, 1000]);

Ndef(\filtering, {
    var sig = Saw.ar(\freq.kr(400)) ! 2 * 0.5;
    var cuttoff = SinOsc.ar(\modfreq.kr(10)).range(
            \mincutoff.kr(100), 
            \maxcutoff.kr(1000)
        );
    sig = LPF.ar(sig, cuttoff);
}).play;
)

Ndef(\filtering).gui;
```

Almost all physical objects possess the capacity to resonate. In other words, nearly every object will naturally vibrate at specific frequencies. 
Imagine a musical object, such as a string, that is not being actively played or plucked, yet exists within an environment where sound is being generated.
How does such an object interact with the vibrations of other objects?

What we observe in such a case is **resonance**!
If the musical object is exposed to frequencies that match its natural resonant frequencies, it will vibrate in harmony with the source of the vibrations. Conversely, if the frequencies don't match, it will largely remain static.
The way a musical instrument resonates significantly impacts the color of its sound, or its ([timbre](sec-timbre)).

Resonance filters intensify certain frequencies, amplifying the harmonics at those frequencies beyond their levels in the input signal.
This effect emulates resonance, hence these filters are known as resonance filters.

Which frequencies are amplified? 
Typically, in most resonance filters, the frequencies near the cutoff point are the ones that are boosted.
In ``sclang`` the [UGens](def-ugen) that implement a resonance filter begin with an ``R``.
For instance, [RLPF](https://doc.sccode.org/Classes/RLPF.html) stands for *resonant low pass filter*.

```isc
(
Spec.add(\modfreq, [0, 1000]);
Spec.add(\freq, [0, 1000]);
Spec.add(\mincutoff, [5, 1000]);
Spec.add(\maxcutoff, [5, 1000]);
Spec.add(\bandwidth, [5, 100]);

Ndef(\filtering, {
    var sig = Saw.ar(\freq.kr(400)) ! 2 * 0.5;
    var cuttoff = SinOsc.ar(\modfreq.kr(10)).range(
            \mincutoff.kr(100),
            \maxcutoff.kr(1000)
        );
    sig = RLPF.ar(sig, cuttoff, rq: \bandwidth.kr(100) / cuttoff);
}).play;
)
Ndef(\filtering).gui;
```

Try different values especially for the bandwidth.
A small bandwidth will result in a strong effect.
In fact, if the bandwidth is very small, the effect becomes so pronounced that the high and low frequencies disappear from the signal and another effect occurs: the filter begins to oscillate at its cutoff frequency.
The result is a powerful unnatural sound unique to the electronic synthesizer.