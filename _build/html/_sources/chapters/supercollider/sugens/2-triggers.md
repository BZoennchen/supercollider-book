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

(sec-demand-ugens)=
# Demand Unit Generators

In this section, I wish to discuss the ability to modify (discrete) arguments directly on the **audio server**.

We've learned about instantiating [Synths](https://doc.sccode.org/Classes/Synth.html) using either (1) [patterns](sec-playing-pattern) iin conjunction with [Pbind](https://doc.sccode.org/Classes/Pbind.html) or [Pbindef](https://doc.sccode.org/Classes/Pbindef.html), or (2) other [scheduling techniques](sec-scheduling) like [Routine](https://doc.sccode.org/Classes/Routine.html) while communicating with the audio server, for example:

```isc
x = Synth(\default, [\freq: 64.midicps]);
...
x.set(\gate, 0);
...
x = Synth(\default, [\freq: 80.midicps]);
```

However, if we don't need control over the changes via the client-side  ``sclang`` -- meaning, if all required algorithms can be implemented through server-side code -- we can utilize *triggers* and *demand unit generators* to make discrete changes, such as altering the frequency of a running synth.
Many may find this method of programming less than desirable, and as far as I know, there's nothing you can't do without this method.
However, this largely boils down to personal aesthetic preference.
Moreover, if you stumble across code that utilizes *demand unit generators*, you might want to understand what is going on.

In principle, we can actually employ "server-side pattern" such as [Dseq](https://doc.sccode.org/Classes/Dxrand.html), [Dxrand](https://doc.sccode.org/Classes/Dxrand.html), and so on.
For many pattern ``Pname``, there is a server-side version called ``Dname``.

Let's consider an example:

```isc
(
{
    var trig, sig, freqs = [500, 400, 300, 200];
    trig = Impulse.kr(10);
    SinOsc.ar(Demand.kr(
        trig: trig, 
        reset: 0, 
        demandUGens: Dxrand(freqs, inf))
    ) * 0.5!2;
}.play;
)
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/demand-dxrand.mp3'
ipd.Audio(audio_path)
```

In this case, I use [Dxrand](https://doc.sccode.org/Classes/Dxrand.html) to select from four different frequencies, with the guarantee that two consecutive chosen frequencies will be different. 
Whenever the trigger changes its value from zero or lower to a positive value, [Demand](https://doc.sccode.org/Classes/Demand.html) gets activated. 
It asks its *demand unit generators* for the next value and then outputs it.

Instead of using a trigger, we can use durations in combination of the [Duty](https://doc.sccode.org/Classes/Duty.html) unit generator.
The following code leads to the same result.

```isc
(
{
    var sig, freqs = [500, 400, 300, 200];
    SinOsc.ar(Duty.kr(
        dur: 10.reciprocal, 
        reset: 0, 
        level: Dxrand(freqs, inf)).poll
    ) * 0.5!2;
}.play;
)
```

[TDuty](https://doc.sccode.org/Classes/Duty.html) lets you introduce a delay before the first ``level`` value gets polled.
You can use ``Duty(...).poll`` to see the values that are generated.

The following code achieves almost the same except that consecutive frequencies might be equal.
Here I use the [Select](https://doc.sccode.org/Classes/Select.html) *unit generator*.
[TIRand](https://doc.sccode.org/Classes/TIRand.html) picks an integer from $\{0,1,2,3\}$ at random whenever ``trig`` gets activated.
This number acts as an *index* ``i`` used by [Select](https://doc.sccode.org/Classes/Select.html) to pick ``freqs[i]``.

```isc
(
{
    var trig, sig, freqs = [500, 400, 300, 200];
    trig = Impulse.kr(10);
    SinOsc.ar(Duty.kr(
        dur: 10.reciprocal, 
        reset: 0, 
        level: Select.kr(TIRand.kr(0, 3, trig), freqs)).poll
    ) * 0.5!2;
}.play;
)
```

There are many more *demand unit generators* to explore. 
Given that these are quite similar to existing client-side control structures and patterns, I won't delve into further details here.