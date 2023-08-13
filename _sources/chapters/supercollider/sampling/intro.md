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

# Music Concrète

The most common definition for concrète music, what you will hear in an electro-acoustic music course, is compostion using recordings of real sounds as raw material.
This definition takes its meaning partly as a distinction from analog electronic sounds which are purely electronic.
The attraction is the richness and complexity of the source.
The sounds can have a depth that is difficult to reproduce with pure electronics.

Today we call the use of such raw material, i.e. recordings, *sampling*.
It is concrète because it never changes at least if we do not modulate it.
The process of using raw material as a basis and built on top of it we may call *sound file manipulation*.
In that sense, the title of this chapter is kind of ironic.

## Buffers

Before processing audio it needs to be loaded into a memory [Buffer](https://doc.sccode.org/Classes/Buffer.html) on the server.
After audio is loaded into a buffer, either from a sound file on disk or from an input source, it is then available for processing, quotation, or precise playback manipulation.

I recorded the sound of a waterboiler since I thought that might be interesting to work with.
To load the file into a buffer on the server, the following line suffice.
I suggest you pick an audio file that you can play with.
Here, I use the [global variable](sec-variables) ``b`` as the reference to the server buffer.

```isc
b = Buffer.read(s, "../samples/experimental/waterboiler.WAV".resolveRelative);
```

I use a relative path, relative from the ``scd``-file, to the file ``waterboiler.WAV``.
We can directly play the buffer ``b``:

```isc
b.play;
```

To get some information about the buffer you can call.

```isc
b.query;
```

In my case it prints:

```
bufnum: 2718
numFrames: 8645952
numChannels: 2
sampleRate: 48000.0
```

Since there are ``8645952`` frames and the sample rate is 48.0 kHz the sample is ``8645952 / 48000.0 = 180.124`` seconds long.

## Playing Buffers

As mentioned we can use ``b.play`` to play the buffer ``b`` but this gives us no control over how we play it.
The power of using rich raw audio material is to manipulate the playback, e.g. speed it up to increase the pitch or to play only a little part as small as some milliseconds, etc.

A [unit generator](sec-ugens) that makes this possible is [PlayBuf](https://doc.sccode.org/Classes/PlayBuf.html).
We have to define the number of channels and the number of the buffer.
Let's define a minimal [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) to play the buffer.

```isc
(
SynthDef(\playbuff, {
    var sig, env;

    sig = PlayBuf.ar(
        numChannels: 2, // my recording is in stereo
        bufnum: \buf.kr(0),
        rate: BufRateScale.kr(\buf.kr(0)) * \rate.kr(1.0),
        startPos: \pos.kr(0.0)
    );

    env = EnvGen.kr(
        Env([0, 1, 0], [\atk.ir(0.02), \rel.ir(3)], [-2, -4]), 
        doneAction: Done.freeSelf
    );

    sig = sig * env;
    sig = sig * \amp.kr(1);

    Out.ar(\out.kr(0), sig);
}).add;
)
```

The unit generator [BufRateScale](https://doc.sccode.org/Classes/BufRateScale.html) computes and returns a ratio by which the playback of a soundfile is to be scaled.
This can be important if the sampling rate of the file differ from the sampling rate of the audio server scsynth.
If the sampling rate of the server is greater, the file would be played back faster resulting in an increased pitch.
Via ``rate`` we can control the actual playback rate, i.e. the pitch.
Note that a negative rate plays the sample backwards as expected.
I use a very simple envelope that realizes only an attack and release.

Let's use our synth definition.
I choose to start the sample 160 seconds in, that is, at position ``b.sampleRate * 160``:

```isc
Synth(\playbuff, [
    buf: b.bufnum, 
    rate: 1, 
    pos: b.sampleRate * 160, 
    atk: 1.0, 
    rel: 1.0]
);
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/sampling1.mp3'
ipd.Audio(audio_path)
```

Let's increase the playback rate to ``rate: 4``.

```isc
Synth(\playbuff, [
    buf: b.bufnum, 
    rate: 4, 
    pos: b.sampleRate * 160, 
    atk: 1.0, 
    rel: 1.0]
);
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/sampling2.mp3'
ipd.Audio(audio_path)
```

If we use a very short attack and release we get closer what one calls *granular synthesis*, i.e., a sound synthesis method that operates on the *microsound* time scale.
The samples are split into small pieces of around 1 to 100 milliseconds in duration.
These small pieces are called *grains*.
Multiple *grains* may be layered on top of each other, and may play at different speeds, phases, volume, and frequency, among other parameters.
Greek composer Iannis Xenakis is known as the inventor of the granular synthesis technique.

>All sound, even continuous musical variation, is conceived as an assemblage of a large number of elementary sounds adequately disposed in time.
>In the attack, body, and decline of a complex sound, thousands of pure sounds appear in a more or less short interval of time.

In the following example each grain is 0.01 + 0.05 = 0.06 that is 60 milliseconds long.

```isc
(
fork {
    300.do {
        var rates = [1, 3, 4, 6, 10], durs = [1/4, 1/8, 1/8, 1/2, 1] / 16;
        Synth(\playbuff, [
            buf: b.bufnum,
            rate: rates.choose,
            pos: b.sampleRate * rrand(140, 160),
            atk: 0.01,
            rel: 0.05]
        );
        durs.choose.wait;
    }
};
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/sampling3.mp3'
ipd.Audio(audio_path)
```

We play in roughly seven seconds 300 *grains*.

Another unit generator useful to play buffers is [BufRd](https://doc.sccode.org/Classes/BufRd.html).
Instead of playing the buffer with a specific rate (that can be modulated), we give the ``phase`` (index of the frame) directly via anohter unit generator.
For instance, we can use the x-coordinate of the mouse using [MouseX](https://doc.sccode.org/Classes/MouseX.html) to sweep through the buffer.

```isc
{BufRd.ar(1, b.bufnum, K2A.ar(MouseX.kr(0, 40*48000.0)))}.play
```

[K2A](https://doc.sccode.org/Classes/K2A.html) transform a signal from *control* to *audio rate*.
Other helpful unit generators are [BufFrames](https://doc.sccode.org/Classes/BufFrames.html) which returns the numbers of frames (in my case 8645952) and [BufDur](https://doc.sccode.org/Classes/BufDur.html) which gives you the duration of the sound file

The following code plays the buffer as if we would call ``b.play``.

```isc
(
{
BufRd.ar(
    numChannels: 2,
    bufnum: b,
    phase: LFSaw.ar(BufDur.ir(b).reciprocal, iphase: 1).range(0, BufFrames.ir(b))
)
}.play
)
```

Whenever the buffer number is required you can also just use ``b`` instead of ``b.bufnum``.
In the following example, I play my sample starting at 5 seconds for 10/4 seconds but with a rate of 4.
For each cycle of the saw wave this is repeated. 

```isc
(
{
var len = 10, start = 5, rate = 4;
BufRd.ar(
    numChannels: 2,
    bufnum: b,
    phase: LFSaw.ar(len.reciprocal*rate, iphase: 1).range(
        b.sampleRate * start, 
        b.sampleRate * (start+len)
    );
)
}.play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/sampling4.mp3'
ipd.Audio(audio_path)
```

To avoid clicks you can use en envelope with a trigger.

```isc
(
{
var len = 10, start = 5, rate = 4, srate = b.sampleRate, dur = len/rate;
BufRd.ar(
    numChannels: 2,
    bufnum: b,
    phase: LFSaw.ar(1/dur, iphase: 1).range(start, start+len) * srate
) * EnvGen.kr(
    Env.linen(0.01, 0.98, 0.01),
    timeScale: dur, gate: 
    Impulse.kr(1/dur));
}.play
)
```

Since we can use **any** unit generator to swipe through the sample, we can achieve interesting results.

```isc
(
{
var len = 4, start = 30, rate = 0.5, srate = b.sampleRate, dur = len/rate, env;
env = EnvGen.kr(
    Env.linen(0.01, 0.98, 0.01), 
    timeScale: dur, 
    gate: Impulse.kr(1/dur)
);
BufRd.ar(
    numChannels: 2,
    bufnum: b,
    phase: SinOsc.ar(1/dur).range(start, start+len) * srate
) * env;
}.play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/sampling5.mp3'
ipd.Audio(audio_path)
```

## Recording

Recording can be done via the graphical user interface of the SuperCollider IDE.
However, by utilizing the [RecordBuf](https://doc.sccode.org/Classes/RecordBuf.html) [unit generator](sec-ugens) you can record into a [Buffer](https://doc.sccode.org/Classes/Buffer.html) (in my case 180.124).

```isc
// a four second 1 channel Buffer
d = Buffer.alloc(s, 44100 * 4.0, 1); 

{RecordBuf.ar(In.ar(2), d.bufnum, loop: 0)}.play;

{PlayBuf.ar(1, d.bufnum)}.play(s);
```

It might look strange to call ``play`` to start recording but this is exaclty what is happening.
Note also that we can record into a full buffer and control the mixing by ``recLevel`` (amplitude of the buffer content) and ``preLevel`` (amplitude of what is recorded).

This can be interesting to create even more complex audio files.
We can combine purely synthesized signal with multiple audio files played back very differently.
The *space of possibilities* is almost limitless.

[PlayBuf](https://doc.sccode.org/Classes/PlayBuf.html) and [RecordBuf](https://doc.sccode.org/Classes/RecordBuf.html) have a ``loop`` argument, set to 0 (no loop) by default. 
To loop playback, set this value to 1. 
In the case of RecordBuf a loop is applied to playback and record.
If ``loop`` is equal 1 and ``preLevel`` is set to 0.5 and we continue to keep recording than the existing loop (pre-recorded material) will slowly fade away.
[BufRd](https://doc.sccode.org/Classes/BufRd.html)