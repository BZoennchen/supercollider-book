# Example

Let us first recreate the [sawtooth wave](sec-square-wave) without ``LFSaw``.
Instead we use a bunch of ``SinOsc`` oscillators.
The following code generates the sound of the Fourier series approximation.
I implemented Eq. {eq}`eq:saw:fourier:n`.
You can change ``n`` to increase the number of harmonics.

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n;
    amp = 0.5;
    n = 10;
    sig = 0;

    n.do({
        arg index;
        var k = index+1;
        sig = sig + ((-1).pow(k%2) * SinOsc.ar(\freq.kr(220)*k) / k);
    });

    sig = (1/2) - ((1/pi) * sig);
    sig = sig!2 * amp;
}).play;
)
```

```{admonition} SCLang and the Server
:name: attention-invalid-synthdef-arguments
:class: attention
We are tempted to convert the variable ``n`` into an argument that we can change while the synth is playing!
Here we enter the limits of a synth or in other words the difference between ``sclang`` and the code that is actually running on the audio server.

``sclang`` is executed on the client.
Therefore, the ``do``-construct is executed on the client before the synth is sent to the server.
In some sense, the synth is compiled and ``n`` is a variable which is fixed at run time.
Consequently, changing ``n`` while the synth is playing will not change anything.
```

My machine has no problem of running over hundred oscillators (``n=100``).
The CPU workload is at about 8-9 percent.
If we only use the first ten harmonics, the sound is clearly much more doll and it becomes crispier by adding more and more harmonics.
However, for me at least, at some point it is hard to perceive any difference if I add even more harmonics.

Ok, so far so good.
Of course, it makes no real sense to recreate the 'pure' [sawtooth wave](sec-square-wave) by multiple oscillators because it is much more computational expensive.
But if we introduce modulation we can create many different sounds that can not be produced by only one [sawtooth wave](sec-square-wave).
Even with filters this can be quite challenging or impossible.

For example, a string of a 'perfect' violin makes a sound that can be described by a [sawtooth wave](sec-square-wave) -- each harmonic of the fundamental is present.
However, there is no globally determining envelope.
Instead each frequency changes its power over time independently.
Therefore, a real violin sounds completely different than a [sawtooth wave](sec-square-wave) combined with an [envelope](sec-envelope).
Furthermore, the world is imperfect and so is the violin -- there is always some distortion, also within the frequencies.
Fortunately, our ears like this slight imperfection.
By introducing imperfections the sound becomes more gentle.
It is a balance between order and chaos.
In summary, for a real violin

1. the amplitudes of the harmonics deviate from Eq. {eq}`eq:saw:fourier:n`,
2. they slightly deviate over time -- each in a different way,
3. and their power (amplitude) is a unique function of time.

## Global Envelope

Let is first try a percussive envelope:

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n=20, env;
    amp = 0.5;
    sig = 0;

    env = EnvGen.ar(Env.perc(
        attackTime: \attk.kr(0.1),
        releaseTime: \rel.kr(1.0),
        curve: \curve.kr(-4)),
    doneAction: Done.freeSelf
    );

    n.do({
        arg index;
        var k = index+1;
        sig = sig + ((-1).pow(k%2) * SinOsc.ar(\freq.kr(220)*k) / k);
    });

    sig = (1/2) - ((1/pi) * sig);
    sig = sig!2 * amp * env;
}).play;
)
```

The sound is quite boring because nothing changes over time.
There is no dynamic thus we lose interest immediately.
Let us introduce some change over time.

## Noisy De-tuning of Partials Over Time

My starting point is the introduction of detune but a detune that changes over time!
I introduce a variable ``vibrato`` that lies in between $[1-\epsilon; 1+\epsilon]$.
$\epsilon$ is the percentage of maximal detune, that is, a harmonic with a frequency of $f$ will have an actual frequency within $[f(1-\epsilon); f(1+\epsilon()]$.
In the code below, I call $\epsilon$ ``detune``.
The detune changes over time.

I make use of ``LFNoise1`` which chooses a value between 1 and -1 every $1/f$ seconds where $f$ is its frequency.
In between of these times, values are linearly interpolated.
Note that for each speaker the noises are different!
It is hard to explain what exactly happens with our ``vibrato`` over time so let us plot an example

```isc
{LFNoise1.ar(100!2).range(1-0.015, 1+0.015)}.plot(1.01)
```

gives us the following plot:

```{figure} ../../../figs/sounddesign/add-synth-single-noise.png
---
width: 800px
name: fig-add-synth-single-noise
---
```

The updated version of ``\sine_sum`` looks like the following:

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n=20, env;
    var detuneFreq = 100;
    var detune = 0.015;

    amp = 0.5;
    sig = 0;

    env = EnvGen.ar(Env.perc(
        attackTime: \attk.kr(0.01),
        releaseTime: \rel.kr(1.0),
        curve: \curve.kr(-4)),
    doneAction: Done.freeSelf
    );

    n.do({
        arg index;
        var k = index+1;
        var vibrato = LFNoise1.ar(detuneFreq!2).range(1-detune, 1+detune);
        var harmonicFreq = \freq.kr(220) * vibrato * k;
        var harmonic = ((-1).pow(k%2) * SinOsc.ar(harmonicFreq) / k);
        sig = sig + harmonic;
    });

    sig = (1/2) - ((1/pi) * sig);
    sig = sig * amp * env;
}).play;
)
```

In my opinion, this already sounds much more interesting.
Of course, we went beyond *additive synthesis* and used *frequency modulation* but those go hand in hand, especially if the modulation frequency is low.

## Separated Partial Envelopes

What can we do in addition?
Well, at the moment we have one global envelope for all frequencies.
What about ``n`` independent envelopes?
We could, for example, imitate nature and decrease the amplitudes of high frequencies faster than those of low frequencies.
We could introduce randomness such that only the *expected decrease in amplitude* behaves like that.

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n=20;
    var detuneFreq = 100;
    var detune = 0.015;

    amp = 0.5;
    sig = 0;

    n.do({
        arg index;
        var k = index+1;

        var env = EnvGen.ar(Env.perc(
            attackTime: \attk.kr(0.01) * Rand(0.8,1.2),
            releaseTime: \rel.kr(5.0) * Rand(0.9,1.1),
            curve: \curve.kr(-4))
        );

        var vibrato = LFNoise1.ar(detuneFreq!2).range(1-detune, 1+detune);
        var harmonicFreq = \freq.kr(220) * vibrato * k;
        var harmonic = ((1/2) - ((1/pi) * ((-1).pow(k%2) * SinOsc.ar(harmonicFreq) / k))) * env.pow(1+((k-1)/3));
        sig = sig + harmonic;
    });

    sig = sig * amp;
    DetectSilence.ar(sig, doneAction: Done.freeSelf);
    sig;
}).play;
)
```

Ok, this looks complicated.
However, I did not change too much.
First, I have rewritten the series such that the sum is the most outer operation.
Secondly, I generate for each frequency one independent envelope with a random attack and release.
Thirdly, I take the power to decrease the envelope for high frequencies faster:

```{math}
:label: eq:env:amplified
    x \leftarrow x^{1 + \frac{k-1}{3}}
```

where $x$ is a value of the envelope (a series of numbers) of the $k^\text{th}$-harmonic.
Compare the following two plots.

```{figure} ../../../figs/sounddesign/add-synth-env_2.png
---
width: 400px
name: fig-add-synth-env_2
---
The effect of Eq. {eq}`eq:env:amplified` for $k = 2$.
```

```{figure} ../../../figs/sounddesign/add-synth-env_10.png
---
width: 400px
name: fig-add-synth-env_10
---
The effect of Eq. {eq}`eq:env:amplified` for $k = 10$.
```

Fourthly, I remove the ``doneAction: Done.freeSelf`` from the envelopes because this would shut down the synth as soon as the first envelope reaches its end.
The sound would abruptly end too early.
To clean up the audio server, I instead use ``DetectSilence``-[UGen](sec-ugens).
It executes the cleanup, that is, the action ``freeSelf`` if the signal ``sig`` indicates silence for a small period of time, which is very handy.