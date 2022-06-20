# Phase & Frequency

If we speak of filters, we often refer to *low pass* or *high pass filters*. 
They filter frequencies above or below some *cutoff frequency*.
For example, the low pass filter ``LPF`` in ``sclang`` is a *2nd order Butterworth lowpass filter*.

```{figure} ../../../figs/sounddesign/filters/butterworth-filter.png
---
width: 600px
name: fig-butterworth-filter
---
Effect of a first-order Butterworth lowpass filter. By Alejo2083 - Own work, CC BY-SA 3.0, [link](https://commons.wikimedia.org/w/index.php?curid=735081).
```

The filter reduces the gain (amplitude) for frequencies above the cutoff frequency and shifts their phases.
Well, that is not entirely true because the cutoff frequency is also reduced by 6 [decibel (dB)](sec-intensity), so the reduction starts a little bit below the cutoff frequency.
Reducing the loudness by 6 dB means that the perceived level is reduced by a factor of 4.
The top plot of {numref}`Fig. {number} <fig-butterworth-filter>` shows the reduction in amplitude.

The second effect of the filter is a phase shift; compare the bottom plot of {numref}`Fig. {number} <fig-butterworth-filter>`.
This effect is crucial if we combine multiple filters because they interact!
In other words: we can not just combine a high pass and low pass filter to get the same result as a band pass filter!

The following code is an example of a band pass filter.
First, we use a low pass and high pass filter; then a band pass filter.
The results sound very similar but not identical.

```isc
({
    var sig = LFSaw.ar(500) ! 2 * 0.5;
    sig = HPF.ar(sig, 200);
    sig = LPF.ar(sig, 300);
    sig
}.play;)

({
    var sig = LFSaw.ar(500) ! 2 * 0.5;
    var bandwidth = 100;
    var cuttoffFeq = 200;
    sig = BPF.ar(sig, 250, rq: bandwidth / cuttoffFeq);
    sig
}.play;)
```

For completeness I also want to mention the inverse filter of a band pass filter: the band reject filter ``BRF``.
The following example rejects frequencies between 200 and 300 Hz, i.e., the inverse operation as before.

```isc
({
    var sig = LFSaw.ar(500) ! 2 * 0.5;
    var bandwidth = 100;
    var cuttoffFeq = 200;
    sig = BRF.ar(sig, 250, rq: bandwidth / cuttoffFeq);
    sig
}.play;)
```