# Control Filters

Control filters are UGens that process control rate signals. They can perform various functions, such as smoothing a control signal, downsampling an audio signal to a control signal, or performing mathematical operations on control signals.

To use a control filter, you need to create an instance of the control filter [UGen](http://doc.sccode.org/Classes/UGen.htm), connect a control signal to its input, and then connect the output of the control filter to the parameter you want to control. 
The control filter will process the control signal and the resulting signal will control the parameter.

(sec-lag)=
## Lag

The [Lag](http://doc.sccode.org/Classes/Lag.html) unit generator is a simple control filter that's very useful for smoothing rapid changes in a control signal. This is often used to avoid clicks or pops that might occur when a parameter changes suddenly.

It is similar to [OnePole](http://doc.sccode.org/Classes/OnePole.html) but it has a more meaningful parameter, called ``lagTime`` which is the time it takes for the output value to reach 63.2% of the way towards the target value after the input changes.
The higher the ``lagTime``, the slower the output will respond to changes in the input, and the smoother the transition will be.

The following code plots a the signal of a noise generator which generates a random value every ``1/freq`` seconds.
We smoothen the noise by a [OnePole](http://doc.sccode.org/Classes/OnePole.html) and by [Lag](http://doc.sccode.org/Classes/Lag.html).
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
A filtered random signal. First we apply [OnePole](http://doc.sccode.org/Classes/OnePole.html) and [Lag](http://doc.sccode.org/Classes/Lag.html) which gives us roughly the same result.
```

Since [Lag](http://doc.sccode.org/Classes/Lag.html) is often used to smoothen changing parameters, for example in a performance, SuperCollider offers us a syntactical shorthand:

```isc
LFNoise0.ar(freq).lag(0.1);
```

Let us try to lag a signal consisting of 440 and 40 Hz.
As we increase the ``lagTime`` we have to boost the amplitude of the signal.

```isc
{SinOsc.ar(440)+SinOsc.ar(40) * 0.25;}.plot(2/40);

({
3.8 * Lag.ar(
    SinOsc.ar(440)+SinOsc.ar(40), 
    lagTime: 300/440
) * 0.25;
}.plot(2/40);
)
```

```{figure} ../../../figs/sounddesign/filters/lag-filtering.png
---
width: 800px
name: fig-lag-filtering
---
A signal consisting of 440 HZ and 40 Hz partial (left) filtered by [Lag](http://doc.sccode.org/Classes/Lag.html) (right).
```

(sec-varlag)=
## VarLag

[VarLag](http://doc.sccode.org/Classes/VarLag.html) is similar to [Lag](http://doc.sccode.org/Classes/Lag.html) but with other curve shapes than exponential.
However [VarLag](http://doc.sccode.org/Classes/VarLag.html) only works at control rate ``kr``!
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
A filtered random signal. First we apply no filter at all, then [VarLag](http://doc.sccode.org/Classes/VarLag.html) with different curve shapes.
```