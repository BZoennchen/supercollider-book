#!/usr/bin/env python
# coding: utf-8

# # Drones
# 
# In this section, we try to create an ambient drone sound.
# Drones are great building blocks.
# They can stand on their own or be part of the background texture of our sound.
# They can be stale or slowly moving using modulation at control rate.
# Due to multichannel expansion and *unit generator argument modulation* SuperCollider is a powerful tool for creating all kinds of drones.
# I find it much more challenging to create an exciting melody than to construct interesting drones.
# 
# A fundamental building block of drones is the *beating effect*.
# If we combine two *waveforms* of slightly detuned frequency, we can clearly hear the difference in frequency.
# The result is a *beating effect*.
# Take, for example, two slightly detune [sine waves](sec-sine-wave):
# 
# ```isc
# {SinOsc.ar(90 * [1, 1.01]) * 0.8}.play;
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/sine-low-freq.mp3'
ipd.Audio(audio_path)


# The frequency difference is 1%.
# We hear a *beating* of frequency $0.9$ Hz.
# 
# Ok, this drone becomes boring pretty fast, but it is still astonishing how easy it is to create a basic drone.
# Let's try multiple detuned harmonics using a combination of [sawtooth waves](sec-sawtooth-wave).
# A *resonance low pass filter* is used to filter out high frequencies.
# Moreover, we add additional movement to the sound using low frequency noise, distortion, and panning.
# [Balance2](https://doc.sccode.org/Classes/Balance2.html) is similar to a panning ([Pan2](https://doc.sccode.org/Classes/Pan2.html)) but for a *stereo signal*.
# We let the stereo signal move from left to right.
# 
# ```isc
# (
# SynthDef(\drone_saws, {
# 	arg freq = 75;
# 	var sig, detuner, env;
# 	sig = Array.fill(8, {arg i;
# 		var freqNoise = LFNoise1.kr(Rand(0.05, 0.2)).bipolar(1.0).midiratio;
# 		RLPF.ar(
# 			in: Saw.ar(freq * (i+1).reciprocal * freqNoise * [1.0, 1.01]).distort,
# 			freq: freq*(i+1),
# 			rq: SinOsc.kr(Rand(0.05, 0.2)).range(0.4, 1.0),
# 			mul: SinOsc.kr(0.11).range(0.5, 0.9) * (i+1).reciprocal
# 		);
# 	}).sum;
# 
# 	env = EnvGen.kr(Env(
# 		levels: [0, 1, 1, 0],
# 		times: [\atk.kr(6.0), \sus.kr(4.0), \rel.kr(6.0)]), doneAction: Done.freeSelf);
# 
# 	sig = Balance2.ar(sig[0], sig[1], pos: LFNoise1.kr(0.1).bipolar(0.85));
# 	sig = sig * env * \amp.kr(1.0);
# 	Out.ar(0, sig);
# }).add;
# )
# Synth(\drone_saws, [\freq, 200, \amp: 1.2]);
# ```
# 
# TODO!

# In[2]:


audio_path = '../../../sounds/saw-drone.mp3'
ipd.Audio(audio_path)


# Our basic waveform is a [sawtooth wave](sec-sawtooth-wave).
# The drone has a long attack and decay.
# In fact, we start without an envelope.
# This time we will use the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) to define our drone synth.
# 
# ```isc
# (
# SynthDef(\drone, {
#     var sig, amp;
# 	amp = 0.5;
# 	sig = Saw.ar(\freq.kr(150)) * amp;
#     Out.ar(0, sig);
# }).play;
# )
# ```
# 
# That's our basic [sawtooth wave](sec-sawtooth-wave) which does not sound very drone-like.
# A drone has a lot of movement.
# Our first step is to change the frequency of the drone over time but not too much.
# Since we want this sine like wobble effect, we use a sine wave for the frequency modulation.
# But to add additional movement, we modulate the frequency of the frequency modulation randomly:
# 
# ```isc
# (
# SynthDef(\drone, {
#     var sig, amp, freqmod;
# 	amp = 0.5;
# 	freqmod = SinOsc.kr(LFNoise0.kr(1)).range(1-\detune.kr(0.01), 1+\detune.kr(0.01));
# 	sig = Saw.ar(\freq.kr(150) * freqmod) * amp;
# 	Out.ar(0, sig);
# }).play;
# )
# ```
# 
# We can reduce the harshness by using a ``VarSaw`` instead of ``Saw``.
# ``VarSaw`` let's us modulate its ``width`` by which we can control how much it is shaped like a [triangle wave](sec-triangle-wave).
# 
# ```isc
# (
# SynthDef(\drone, {
#     var sig, amp, freqmod, widthmod;
# 	amp = 0.85;
# 	freqmod = SinOsc.kr(LFNoise0.kr(1)).range(1-\detune.kr(0.01), 1+\detune.kr(0.01));
# 	widthmod = SinOsc.kr(LFNoise0.kr(1)).range(0.35, 0.65);
# 	sig = VarSaw.ar(\freq.kr(150) * freqmod) * amp;
# 	Out.ar(0, sig);
# }).play;
# )
# ```
# 
# Let's duplicate to create some sort of unison:
# 
# ```isc
# (
# SynthDef(\drone, {
#     var sig, amp, freqmod, widthmod, n = 3;
# 	amp = 0.85;
# 
# 	sig = Array.fill(n, {
# 		arg i;
# 		freqmod = SinOsc.kr(LFNoise0.kr(1)).range(1-\detune.kr(0.01), 1+\detune.kr(0.01));
# 		widthmod = SinOsc.kr(LFNoise0.kr(1)).range(0.35, 0.65);
# 		sig = VarSaw.ar((i+1)*\freq.kr(150) * freqmod) * (i+1).reciprocal;
# 	}) * amp;
# 
# 	sig = Splay.ar(sig);
# 	sig = Balance2.ar(sig[0], sig[1], SinOsc.kr(LFNoise0.kr(0.1).range(0.05,0.2))*0.1);
#     //sig;
# 	Out.ar(0, sig);
# }).play;
# )
# ```
# 
# TODO
