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

# Minimalism

As stated by Nathan, [patterns](sec-pattern) are not for everyone.
You have to learn a bunch of new syntax and keep it in your head.
Sometimes it is easier to just rely on plain [routines](sec-routines-tasks) and [synth](sec-synths).
In the following example, I had a hard time realizing what I wanted using pattern.
Therefore, I choose routines, but I still choose to use events to use parts of the pattern library, in my case, scales and events.
Since I am not musically educated, using scales and degrees instead of plain midi notes or even frequencies makes my life easy (at least for now) when it comes to creating melodies.

I want to construct something similar to the piece [In C](https://web.archive.org/web/20150319002917/http://www.flagmusic.com/content/clips/inc.pdf) by *Terry Riley*.
The piece consists of 53 *melodic fragments*.
Each fragment can be played multiple times before playing the next fragment.
Each musician can play each fragment a different amount of times.
The only suggestion is that musicians should not be separated by too many fragments during the performance. 
This is perfectly suitable to be performed algorithmically, either in an online or offline setting.
Online might be more desirable since Riley notes:

>It is very important that performers listen very carefully to one another and this
means occasionally to drop out and listen. As an ensemble, it is very desirable to
play very softly as well as very loudly and to try to diminuendo and crescendo
together. [...] As the performance progresses, performers should stay within 2 or 3 patterns of each other. It is important not to race too far ahead or to lag too far behind. [...] It is important to think of patterns periodically so that when you are resting you are conscious of the larger periodic composite accents that are sounding, and when you re-enter you are aware of what effect your entrance will have on the music’s flow. -- Terry Riley

Therefore, it would be great to control the process semi-automatically in a live-programming setting with multiple performers.

For the purpose of this book, we try a fully-automated version even if it is not in the spirit of the piece.
I use the following *Glockenspiel*-synth for this example.

```isc
(
SynthDef(\glockenspiel, {
    var sig, env, env2, fundamental, partials;

    env = EnvGen.ar(Env(
        levels: [0, 1, 0.4, 0],
        times: [\atk.kr(0.01), \dec.kr(0.5), \rel.kr(1.5)],
        curve: -4), doneAction: Done.freeSelf);
    env2 = EnvGen.ar(Env(
        levels: [0, 0.25, 0.125, 0],
        times: [\atk.kr(0.01), \dec.kr(0.5)*0.25, \rel.kr(1.5)*0.4],
        curve: -6));

    fundamental = SinOsc.ar(\freq.kr(440)!2);
    partials = Saw.ar(([12, 24]).midiratio * \freq.kr(440));
    sig = fundamental * env;
    sig = sig + (partials * env2);
    sig = sig * 0.1 * \amp.kr(1.0);
    sig = Splay.ar(sig);
    sig = Balance2.ar(sig[0], sig[0], \pan.kr(0));
    Out.ar(\out.kr(0), sig);
}).add;
)
```

My first idea was to use tow pattern (one for duration and for degree) for each melodic fragment and one ``Pbind`` for each musician/instrument.
To make sure all ``Pbinds`` are in sync we can schedule them on a [clock](sec-clocks).
Something like this:

```isc
var degrees = Pseq([
    Pseq([0, 2, 3, 0]),
    Pseq([0, 4]),
    Pseq([6, 6, 7, 7]),
    Pseq([0, -4, -6]),
]);

var durs = Pseq([
    Pseq([0.25, 0.25, 0.5, 0.5]),
    Pseq([0.5, 0.5]),
    Pseq(0.25!4),
    Pseq([0.25, 0.25, 0.5]),
]);
```

Then we might wanna use 3 instruments, i.e. 3 ``Pbinds``:

```isc
var tempo = TempoClock(1); 
3.do {
    Pbind(
    \instrument, \glockenspiel,
    \degree, degrees,
    \dur, durs,
    \amp, 1.0,
).play(tempo, quant: 1);
};
```

However, this just plays the exact same patterns 3 times in parallel and each *melodic fragment* is played exactly once.
We want to play each fragment multiple times but also different amount of times for each intrument.
But how do we do that?
We could introduce random repeats like this:

```isc
var degrees = Pseq([
    Pseq([0, 2, 3, 0], repeats: {rrand(1, 4)}),
    Pseq([0, 4], repeats: {rrand(1, 4)}),
    Pseq([6, 6, 7, 7], repeats: {rrand(1, 4)}),
    Pseq([0, -4, -6], repeats: {rrand(1, 4)}),
]);
```

Note that we need the curly brackets to ensure different values for ``repeats`` each time the pattern gets used, i.e. evaluated.
Compare the following example where repeat is the same for each of the ``Pn``-repeats

```isc
(
Pbind(
    \instrument, \glockenspiel,
    \degree, Pn(Pser([1,2,3,4], repeats: {rrand(1, 4)}), 4),
    \dur, 0.25,
    \amp, 1.0,
).play;
)
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/minimalism-rrand-func.mp3'
ipd.Audio(audio_path)
```

and 

```isc
(
Pbind(
    \instrument, \glockenspiel,
    \degree, Pn(Pser([1,2,3,4], repeats: {rrand(1, 4)}), 4),
    \dur, 0.25,
    \amp, 1.0,
).play;
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/minimalism-rrand.mp3'
ipd.Audio(audio_path)
```

Ok, using ``repeats: {rrand(1, 4)}`` to simulate the musician's choice of repetition seem to work.
However, now we run into another problem: we need the exact same amount of repeats for the duration part of the melodig fragment!
At this point I stoped trying to use pattern for this example because the code is already quiete complicated for something that should be rather easy.

Let us switch gears.
Let us try to use routines instead.
I came up with the following code:

```isc
(
var tempo = TempoClock(1);                  // our tempo
var n = 5;                                  // number of "instruments"
var n_bars = 6;                             // number of bars
var bars = Array.fill(n, 0);                // current bar of instruments
var degrees = Array.fill(n_bars, nil);      // bars (melody pitch parts)
var durs = Array.fill(degrees.size, nil);   // bars (melody duration parts)
var octaves = Array.rand(n, 5, 7);          // octave of instrument

// define the melody parts
degrees[0] = [2, 2, 2, 2];
durs[0] = [0.25, 0.25, 0.5, 0.5];

degrees[1] = [0, 0];
durs[1] = [0.5, 0.5];

degrees[2] = [6, 6, 7, 7];
durs[2] = 0.25!4;

degrees[3] = [-6, -4, -6];
durs[3] = [0.25, 0.25, 0.5];

degrees[4] = [3];
durs[4] = [1.0];

degrees[5] = [1];
durs[5] = [1.0];

fork {
n.do { |j|
    {
        var i = 0;
            120.do {
            var mel = bars[j];
            (
                instrument: \glockenspiel,
                scale: Scale.minor,
                octave: octaves[j],
                pan: {rrand(-0.5, 0.5)},
                degree: degrees.wrapAt(mel).wrapAt(i),
                amp: {rrand(0.3, 0.7)},
            ).play;

            durs.wrapAt(mel).wrapAt(i).wait;
            i = i + 1;

            if(rand(1.0) > 0.85, {
                bars[j] = bars[j] + 1;
            });
        };
    }.fork(tempo, quant: 0.25);
    rrand(2.0, 8.0).wait;
};
};
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/minimalism.mp3'
ipd.Audio(audio_path)
```

Musically this could be better.
We can notice clashes of notes that lead to strong dissonance, but the concept is established, and it is interesting how a bunch of simple fragments can lead to a complex musical texture.
You can easily introduce more fragments, constrains, instruments, and musicians and redefine fragments or play around with probabilities.

Let me explain the code above:
Instead of using the sequence pattern for the pitches (in degree) and durations, I use two-dimensional [arrays](sec-array), ``degrees`` and ``durs`` respectively, where the first dimension is the melodic fragment and the second dimension is the pitch or duration of a specific element within the fragment.
``bars[k]`` indicate the index of the fragment of the musician ``k``.
``n_bars`` is the overall number of melodic fragments.

I ``fork`` ``n=5`` threads scheduled on the same clock.
Each thread represents one musician.
I ``loop`` indefinitely and increase the index of the melodic fragment by one with a certain probability which is independent for each musician/thread.
I make use of ``wrapAt`` such that arrays work like ring buffer (when the index becomes too large, we start all over again).

Instead of playing the ``Synth``, I use events such that I can still use scales, degrees, and so on.
In this example, I only use 4 instead of 53 fragments, and I have no constraints to limit the distance between parallel played fragments.
However, with this design, it is easy to add more fragments and to introduce a more sophisticated index control for selecting fragments.

Patterns are great, but they force you into a certain mindset where some things are more straightforward, and others are harder.
However, the same is true for plain routines.
Often you can achieve more in fewer lines of code using patterns.
But you have to get used to them, and you have to know a lot of patterns.
If you are used to *imperative* programming, routines can be picked but easily, even if you have to write more code which often looks not that beautiful.
I don't know what the best way here is.
It depends on your taste, experience, and background.
For this example, plain routines worked better for me.