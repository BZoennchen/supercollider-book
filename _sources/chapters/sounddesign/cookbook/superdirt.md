---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
```

# SuperDirt Synths

These synths are from the [SuperDirt](https://github.com/musikinformatik/SuperDirt/tree/develop) sampler designed for [TidalCycles](https://github.com/tidalcycles/tidal).
They cover a lot of what I would call basic sounds thus it is a good idea to study what basic unit generators they rely on.
Note that I simplified them a bit such that no ``SuperDirt`` specific classes are required, e.g. I removed the ``DirtFreqScale`` unit generator which manipulates the fundamental frequency based on ``\speed``, ``\accelerate``, and ``\sustain``.

```isc
/*
Frequency scaler with speed like samples have it
Switch on by settig speedFreq > 0
Intermediate values scale proportionally
*/

DirtFreqScale : UGen {
    *kr { |speed = 1, accelerate = 0, sustain = 1, speedFreq|
        var speedTerm;
        speed = speed.abs;
        speedFreq = speedFreq ?? { \speedFreq.ir(1) };
        speedTerm = Line.kr(speed, speed * (accelerate + 1), sustain);

        // linear interpolation between a factor of 1 (speedFreq = 0)
        // and of speedTerm (speedFreq = 1)
        ^speedFreq * (speedTerm - 1) + 1
    }
}
```

In addition, I only list those synths that do not require any extensions.
You can find the unchanged source code [here](https://github.com/musikinformatik/SuperDirt/blob/develop/library/default-synths-extra.scd).

## supergong

`\supergong` is a sum of a fundamental frequency and 14 inharmonic frequencies, consisting of 15 simple sine waves in total.
The higher the frequency of a partial, the shorter its duration and the faster its amplitude decreases.  
This is achieved by the `tscale`, an array of floating-point numbers.
The implemented formula is:

$$\frac{f}{100} \cdot h_i^{-2+\text{clip}(d, 0, 2)}$$

where $f$ is the fundamental frequency `\freq`, $d$ is the `\decay`, and $h_i$ is the $i$-th harmonic.
Clipping serves as a safeguard to keep values within a reasonable range.
The value decreases quadratically with $h_i$, meaning that for higher frequencies, the duration defined by `tscale` is shorter.
This models the natural phenomenon that high frequencies decay faster than low frequencies.
Similarly, the loudness increases with the frequency of the partials, as represented by `ascale`.

A percussive envelope is used.
`clip` ensures that `\decay` remains in the range [0, 2] and `\voice` in the range [0, 4].
The larger the `\decay`, the longer the attack and release times.
Similarly, the larger the `\voice`, the greater the magnitude of the sine waves, i.e., the loudness increases.
Both relationships are exponential because the human ear perceives loudness and frequency on a logarithmic scale.

Effectively, this generates a metallic, inharmonic sound.

```isc
(
SynthDef(\supergong, {
    // lowest modes for clamped circular plate
    var harmonics = [
        1.000,  2.081,  3.414,  3.893,  4.995,  
        5.954,  6.819,  8.280,  8.722,  8.882, 
        10.868, 11.180, 11.754, 13.710, 13.715
    ];

    var tscale = 100.0 / \freq.kr(440) / (harmonics**(2-clip(\decay.kr(1), 0, 2)));
    var ascale = harmonics**clip(\voice.kr(0),0,4);
    var sound = Mix.arFill(15, {arg i;
        var env = EnvGen.ar(
            Env.perc(
                attackTime: 0.01*tscale[i], 
                releaseTime: 0.5*tscale[i], 
                level: 0.2*ascale[i]), 
            timeScale: \sustain.kr(1)*5);
        
        var sig = SinOsc.ar(\freq.kr(440) * harmonics[i]);
        env * sig
    });
    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0)));
}).add
);
```

```isc
(
Pbind(
    \instrument, \supergong,
    \scale, Scale.majorPentatonic,
    \degree, Pseq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    \amp, 0.5,
    \dur, 0.5,
    \sustain, 1.0
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/supergong.mp3'
ipd.Audio(audio_path)
```

## super888

``\super888`` is a vaguely 808-ish kick drum based on a [SinOscFB](https://doc.sccode.org/Classes/SinOscFB.html), that is, a sine oscillator that has phase modulation feedback; its output plugs back into the phase input where the ``feedback`` argument controls the amplitude of phase feedback in radians.
As usual, ``\sustain`` controls the overall duration.
[LPF](https://doc.sccode.org/Classes/LPF.html) filters very high frequencies to reduce the glitchiness of the sound.
The frequency is modulated using [XLine](https://doc.sccode.org/Classes/XLine.html) which generates an exponential curve from the start value to the end value.
The start frequency is exponentially mapped from [10;2000] to [1000;8000] but it ends always at the fundamental frequency.
``\rate`` controls the duration of the frequency sweep.

```isc
(
SynthDef(\super808, {
    var env, sound, freq, mod;
    env = EnvGen.ar(Env.linen(
        attackTime: 0.01, 
        sustainTime: 0, 
        releaseTime: 1, 
        level: 0.3,
        curve: -3),
    timeScale: \sustain.kr(1), doneAction: 2);
    env = env * \amp.kr(1.0);

    mod = XLine.ar(
        start: \freq.kr(440).expexp(10, 2000, 1000, 8000), 
        end: \freq.kr(440), 
        dur: 0.025/\rate.kr(1));
    sound = LPF.ar(in: SinOscFB.ar(freq: mod, feedback: \voice.kr(0)), freq: 9000);
    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0), env));
}).add
);
```

```isc
(
Pbind(
    \instrument, \super808,
    \freq, Pshuf(Array.series(80, 40, 1)).midicps,
    \dur, 0.125,
    \sustain, 0.25,
    \voice, Pwhite(0.0, 1.0, inf),
    \amp, 0.5
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/super888.mp3'
ipd.Audio(audio_path)
```

## supersiren

The ``\supersiren`` [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) creates a dynamic siren sound by

+ Using a variable-width sawtooth wave ([VarSaw](https://doc.sccode.org/Classes/VarSaw.html)) as the sound source.
+ Modulating the amplitude with an envelope that defines the overall shape and duration of the sound.
+ Modulating the frequency with another envelope to create a rising and falling pitch effect.
+ Adjusting the width of the sawtooth wave over time to add variation to the sound.


```isc
(
SynthDef(\supersiren, {
    var env, sound, freqmod;
    env = EnvGen.ar(
        Env.linen(0.05, 0.9, 0.05, 1, -2), 
        timeScale: \sustain.kr(1), 
        doneAction:2
    );
    env = env * \amp.kr(0);

    freqmod = EnvGen.kr(
        Env.linen(0.25, 0.5, 0.25, 3, 0),
        timeScale: \sustain.kr(1), 
        doneAction:2
    );

    sound = VarSaw.ar(
        freq: \freq.kr(440) * (1.0 + freqmod),
        width: Line.kr(0.05, 1, \sustain.kr(1))
    );

    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0), env));
}).add
);
```

```isc
(
Pbind(
    \instrument, \supersiren,
    \freq, Pseq([60, 62, 65, 60, 55], 3).midicps,
    \dur, 0.25,
    \sustain, 0.15,
    \amp, 0.3
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/supersiren.mp3'
ipd.Audio(audio_path)
```

## superkick

The `\superkick` is based on [Rumble-San's implementation](https://blog.rumblesan.com/post/53271713518/drum-sounds-in-supercollider-part-1) as a starting point.
The [SinOsc](https://doc.sccode.org/Classes/SinOsc.html) generates the bass, and the [WhiteNoise](https://doc.sccode.org/Classes/WhiteNoise.html) combined with a [Line](https://doc.sccode.org/Classes/Line.html) envelopes the percussive click.
`\n` controls the kick frequency in a nonstandard way, subtracting 25.5 from the MIDI note `\n`.
Note that in Tidal, `\n` usually controls the pitch and is assumed to be a MIDI note.
`\sustain` affects the overall envelope's duration.
`\pitch1` affects the click frequency by letting higher frequencies through the filter, and `\decay` changes the click duration relative to the overall timescale.

```isc
(
SynthDef(\superkick, {
    var env, sound, dur, clickdur, envFilter;
    env = EnvGen.ar(
        Env.linen(
            attackTime: 0.01, 
            sustainTime: 0, 
            releaseTime: 0.5, 
            level: 1, 
            curve: -3), 
        timeScale: \sustain.kr(1), doneAction:2);

    sound = SinOsc.ar((\n.kr(60) - 25.5).midicps);
    clickdur = 0.02 * \sustain.kr(1) * \decay.kr(1);
    envFilter = Line.ar(start: 1, end: 0, dur: clickdur);
    sound = sound + (LPF.ar(
        in: WhiteNoise.ar(1), 
        freq: 1500*\pitch1.kr(1)) * envFilter);

    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0), env));
}).add
);

```

```isc
(
Pbind(
    \instrument, \superkick,
    \n, Pshuf(Array.series(80, 40, 0.5)),
    \dur, 0.125,
    \sustain, 0.25,
    \pitch1, Pwhite(0.5, 3.0, inf),
    \decay, Pwhite(0.5, 1.5, inf),
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/superkick.mp3'
ipd.Audio(audio_path)
```

## superclap

The ``superclap`` represents a clap sound which is created by layering multiple instances of the filtered noise with slight delays to simulate the sound of multiple fingers clapping.
We mix 4 copies of the enclosed sound within ``Mix``.
Each envelope within the sum has an initial delay ``spr*(i**(\n.kr(0).clip(0,5)+1))``, instantaneous attack, brief sustain, and quick release for each copy.
``sqr`` determines the base delay time, calculated as ``0.005 * \delay.kr(1)``.
``i**(\n.kr(0).clip(0,5)+1)`` scales the delay for each instance using the ``\n`` argument, which is clipped between 0 and 5 to ensure a reasonable range.

```isc
(
SynthDef(\superclap, {
    var env, sound;
    var spr = 0.005 * \delay.kr(1);
    env = EnvGen.ar(Env.linen(0.01, 0, 0.6, 1, -3), 
        timeScale: \sustain.kr(1), 
        doneAction:2
    );

    sound = BPF.ar(
        LPF.ar(
            in: WhiteNoise.ar, 
            freq: 7500 * \pitch1.kr(1)
        ),
        freq: 1500 * \pitch1.kr(1));

    sound = Mix.arFill(4, { arg i; 
        sound * 0.5 * EnvGen.ar(
            Env(
                levels:[0, 0, 1, 0],
                times: [spr*(i**(\n.kr(0).clip(0,5)+1)), 0, 0.04 / \rate.kr(1)]
            )
        );
    });
    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0), env));
}).add
);

```

```isc
(
Pbind(
    \instrument, \superclap,
    \n, Pdup(5, Pshuf([0,1,2,3,4])),
    \dur, 0.25,
    \sustain, 0.15,
    \pitch1, Pwhite(0.1, 3.0, inf),
    \decay, Pwhite(0.9, 1.5, inf),
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/superclap.mp3'
ipd.Audio(audio_path)
```

## superhat

``\superhat`` is a hi-hat using [Rumble-San's implementation](https://blog.rumblesan.com/post/53271713518/drum-sounds-in-supercollider-part-1) as a starting point.
``(\n/5 + 1).wrap(0.5,2)`` makes sure that the result is in [0.5;2].
As stated in the source code: using ``\n`` in a weird way to provide some variation on the frequency.
I am not sure what ``\n`` stands for but looking to the formula it is clear that ``freq`` is in [1000;4000].
And the [WhiteNoise](https://doc.sccode.org/Classes/WhiteNoise.html) is filtered by a low- and highpass filter where the cutoff frequency depends on ``freq``.
The envelope has a short attack, no sustain and a ``releaseTime`` of ``0.3``.
It is basically a percussive envelope and equal to ``Env.perc(0.01, 0.3, 1, -3)``.

```isc
(
SynthDef(\superhat, {
    var env, sound, freq;
    env = EnvGen.ar(
        Env.linen(
            attackTime: 0.01, 
            sustainTime: 0, 
            releaseTime: 0.3, 
            level: 1, 
            curve: -3), 
        timeScale: \sustain.kr(1), doneAction:2);
    freq = 2000 * (\n.kr(10)/5 + 1).wrap(0.5,2);
    sound = HPF.ar(LPF.ar(WhiteNoise.ar(1), 3*freq), freq);
    sound = sound * \amp.kr(1);
    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0), env));
}).add
);
```

```isc
(
Pbind(
    \instrument, \superhat,
    \n, Pwhite(1.0, 4.0, length: 50),
    \dur, 0.25,
    \sustain, Pwhite(0.1, 1.0),
    \amp, 1.0
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/superhat.mp3'
ipd.Audio(audio_path)
```

## supersnare

The ``\supersnare`` is quite similar to the ``\superhat`` but also quite different.
The sound is the sum of two parts: One filtered [Pulse](https://doc.sccode.org/Classes/Pulse.html) where the cutoff frequency of the [LPF](https://doc.sccode.org/Classes/LPF.html) and a filtered [WhiteNoise](https://doc.sccode.org/Classes/LPF.html) with a center frequency of 1500 Hz and a cutoff >500 Hz.

In addition, the amplitude of the second part, i.e. the noise, drops dependend on ``\decay`` where the filter cutoff of the first part decreases from 1030 to 30 Hz in ``0.2* \sustain`` seconds.
Thus, the pulse frequency decreases over time.
Again, ``\n`` brings in some variations and is bound to [0.5;2].
The ``releaseTime`` is doubled compared to ``\superhat``.

```isc
(
SynthDef(\supersnare, {
    var env = EnvGen.ar(
        Env.linen(
            attackTime: 0.01, 
            sustainTime: 0, 
            releaseTime: 0.6, 
            level: 1, 
            curve: -3), 
        timeScale: \sustain.kr(1), doneAction:2);
    var freq = 100 * (\n.kr(5)/5+1).wrap(0.5,2);
    var mod = Line.ar(start: 1030, end: 30, dur: 0.2*\sustain.kr(1));
    var env2 = Line.ar(start: 1, end: 0, dur: 0.2 *\decay.kr(1));
    var sound1 = LPF.ar(in: Pulse.ar(freq), freq: mod);
    var sound2 = BPF.ar(in: HPF.ar(
        in: WhiteNoise.ar(1), 
        freq: 500), freq: 1500) * env2;
    var sound = sound1 + sound2;
    sound = sound * \amp.kr(1);
    Out.ar(\out.kr(0), Pan2.ar(sound, \pan.kr(0), env));
}).add
);
````

```isc
(
Pbind(
    \instrument, \supersnare,
    \n, Pwhite(1.0, 4.0, length: 50),
    \dur, 0.25,
    \sustain, Pwhite(0.1, 1.0),
    \amp, 1.0,
    \decay, Pwhite(0.1, 1.0)
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/supersnare.mp3'
ipd.Audio(audio_path)
```

TODO