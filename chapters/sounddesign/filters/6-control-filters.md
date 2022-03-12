# Control Filters


(sec-lag)=
## Lag

The ``Lag``-``UGen`` is similar to ``OnePole`` but it has a more meaningful parameter, called ``lagTime``.
I do not yet fully understand what it means but basically it is the time frame for which the signal should be smoothen.

The following code plots a the signal of a noise generator which generates a random value every ``1/freq`` seconds.
We smoothen the noise by a ``OnePole`` and by ``Lag``.
Our frequency is 10 Hz and our ``lagTime`` is 0.1 seconds.

```isc
({
    var freq = 10;
    var noise = LFNoise0.ar(freq);
    [noise, OnePole.ar(noise, coef: 0.999), Lag.ar(noise, lagTime: freq.reciprocal)];
}.plot(2.0))
```

This gives us the following plot.

```{figure} ../../../figs/sounddesign/filters/lag-and-onepole.png
---
width: 800px
name: fig-lag-and-onepole
---
A filtered random signal. First we apply ``OnePole`` and ``Lag`` which gives us roughly the same result.
```

Since ``Lag`` is often used to smoothen changing parameters, for example in a performance, SC supports a syntactical shorthand:

```isc
LFNoise0.ar(freq).lag(0.1);
```

Let us try to the 440 Hz part of a signal consisting of 440 and 40 Hz.

```isc
{SinOsc.ar(440)+SinOsc.ar(40) * 0.25;}.plot(2/40)
{3.8*Lag.ar(SinOsc.ar(440)+SinOsc.ar(40), lagTime: 300/440) * 0.25;}.plot(2/40)
```

```{figure} ../../../figs/sounddesign/filters/lag-filtering.png
---
width: 800px
name: fig-lag-filtering
---
A signal consisting of 440 HZ and 40 Hz partial (left) filtered by ``Lag`` (right).
```

As we increase the ``lagTime`` we have to boost the amplitude of the signal.

(sec-varlag)=
## VarLag

``VarLag`` is similar to ``Lag`` but with other curve shapes than exponential but it works only on control rate signals ``kr``!
Compare the different shapes of the lag:

```isc
({
    var freq = 10;
    var noise = LFNoise0.kr(freq);
    [
        noise, 
        VarLag.kr(noise, time: freq.reciprocal, warp: \sine), 
        VarLag.kr(noise, time: freq.reciprocal, warp: \linear), 
        Lag.kr(noise, lagTime: freq.reciprocal)
    ];
}.plot(2.0))
```

```{figure} ../../../figs/sounddesign/filters/var-lag.png
---
width: 800px
name: fig-var-lag
---
A filtered random signal. First we apply ``OnePole`` and ``Lag`` which gives us roughly the same result.
```