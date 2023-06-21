#!/usr/bin/env python
# coding: utf-8

# (sec-reverb)=
# # Reverberation
# 
# Reverberation, often shortened to reverb, is a phenomenon where sound waves reflect off surfaces, resulting in a large number of echoes that gradually fade or "decay".
# It gives us a sense of the size and type of space we're in, whether it's a small bathroom or a large cathedral.
# 
# The *Haas effect* is an acoustic phenomenon.
# When a sound is followed by another sound separated by a sufficiently short delay ($< 50\,\text{ms}$), listeners perceive a single auditory event; the location of the first-arriving sound dominates its perceived spatial location.
# The lagging sound also affects the perceived location but its effect is suppressed by the first-arriving sound, i.e., the first wave front.
# 
# If we start shouting in a big concert hall, we will receive an echo.
# If the time between the initial shouting and the echo is short enough, we perceive *reverberation*.
# The sound wave gets reflected to us, and the reflected wave might get reflected again and again.
# Architects have these reflections in mind when they build a concert hall.
# Moreover, an instrument's timbre is determined by the instrument and how it is played, and in what environment it is played.
# 
# Humans are capable of separating sound sources from each other -- even in the absence of localization cues.
# For example, we can usually easily separate an oboe from a flute, and a flute from a violin, even though they play in the same register.
# The melody from the oboe will be heard separately from the melody of the flute.
# Both instrumental lines from a sound stream -- just like the words of a particular person in a party from a stream.
# These streams are examples of foreground streams.
# They carry specific and often different content and meaning, and we can choose to listen to one while excluding the other.
# 
# As long as a person is talking, the *reverberation* sounds continuous and has a constant level.
# At that point, it is a background stream.
# However, if we look at the sound signal on an oscilloscope, it is clear that the reverberation is decaying rapidly between syllables.
# When the speaking person stops, the reverberation becomes a foreground stream and is audible as a distinct sound event.
# Under these conditions, it is easy to hear that it is decaying.
# 
# The human hearing generally waits 50 milliseconds after a sound event's apparent end, before deciding it is over.
# Therefore, we perceive multiple sound cues within a period smaller than 50 ms as one continuous stream.
# Early reflections can be used to alter the timbre of a sound; to make it louder, heavier, spacially more interesting.
# 
# ```{figure} ../../../figs/sounddesign/reverberation.png
# ---
# width: 800px
# name: fig-reverberation
# ---
# Ideal reverberation profile (according to D. Griesinger).
# Time $t$ is measured in milliseconds.
# ```
# 
# In *The Theory and Practice of Perceptual Modeling -- How to use Electronic Reverberation to Add Depth and Envelopment Without Reducing Clarity* ([pdf](http://www.davidgriesinger.com/threedpm.pdf)) presented at the *Tonmeister conference (2000)* in Hannover, David Griesinger gives an excellent description of an *ideal reverberation profile for recording*.
# We need a strong early lateral field for producing a sense of distance, a mimimum of energy in the $50-150\,\text{ms}$ region, and adequate reverberant energy after $150\,\text{ms}$.
# Recordings with too much energy in the $50$ to $150,\text{ms}$ region sound muddy.
# This time range must be carefully minimized.
# 
# Reverberation can be simulated/approximated by adding [delayed signals](sec-filter-by-delay) that decay over a certain amount of time to the overall output.
# 
# ## Single Reflection
# 
# [DelayN](https://doc.sccode.org/Classes/DelayN.html) takes an input signal, delays it for ``delayTime`` (in seconds) and outputs the a *delayed copy* (without the original).
# Therefore, it can be useful to introduce a reverb effect.
# 
# In the following example we use a *decaying impulse* to generate a repeating exponential envelope.
# The [Impulse](https://doc.sccode.org/Classes/Impulse.html) decays over a period of ``0.2`` seconds.
# [Decay](https://doc.sccode.org/Classes/Decay.html) works similar to [Integrator](https://doc.sccode.org/Classes/Integrator.html) which basically integrate an incoming signal, which is another way of saying that it sums up all past values of the signal. 
# It realizes the following formular:
# 
# \begin{equation}
# y[n] = \sum\limits_{i=0}^n \alpha x[i]
# \end{equation}
# 
# which is realized inductively by
# 
# \begin{equation}
# y[n] = y[n-1] + \alpha x[n].
# \end{equation}
# 
# [Decay](https://doc.sccode.org/Classes/Decay.html) operates on the basis of more meaningful parameters which are independent from the *sample rate*.
# We multiply this repeating envelope with a [PinkNoise](sec-pink-noise) to get a simple beat.
# The *decaying impulse* is just a line going to zero.
# 
# ```isc
# {Decay.ar(Impulse.ar(1.0), 0.2) * PinkNoise.ar}.play
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/decay-beat.mp3'
ipd.Audio(audio_path)


# Let's add a *delayed copy*:
# 
# ```isc
# ({
#     var sig = Decay.ar(Impulse.ar(1.0), 0.2) * PinkNoise.ar;
#     sig + DelayN.ar(sig, 0.5, delaytime: 0.15);
# }.play;
# )
# ```

# In[2]:


audio_path = '../../../sounds/decaying-delayed-impulse.mp3'
ipd.Audio(audio_path)


# If you want to modulate the *delay time* you should consider the interpolated versions, i.e., [DelayL](https://doc.sccode.org/Classes/DelayL.html) or [DelayC](https://doc.sccode.org/Classes/DelayC.html).
# 
# (sec-comb-allpass-filter)=
# ## Decaying Reflections
# 
# A [CombN](https://doc.sccode.org/Classes/CombN.html) delay line with no interpolation is a delay with feedback, i.e., the signal is fed back into the *delay*.
# The signal's power is reduced each time it is fed into the *delay*.
# The *decay time* is the period (in seconds) for which the signal decays by 60 decibels.
# Let's have a listen:
# 
# ```isc
# ({
#     var decaytime = 2.0;
#     var sig = Decay.ar(Impulse.ar(1.0), 0.5) * PinkNoise.ar;
#     sig + CombN.ar(sig, 0.5, delaytime: 0.15, decaytime: decaytime);
# }.play;
# )
# ```

# In[3]:


audio_path = '../../../sounds/decaying-comb-impulse.mp3'
ipd.Audio(audio_path)


# We can generate some exciting grain sounds by combining *modulated resonance* with a *comb delay line*:
# 
# ```isc
# ({
#     var centerFreq = LFNoise0.kr(40/3).exprange(20, 1800);
#     var sig = Saw.ar([32,33]) * 0.2;
# 
#     sig = BPF.ar(sig, freq: centerFreq, rq: 0.1).distort;
#     sig = CombN.ar(sig, 2, delaytime: 2, decaytime: 40);
#     sig;
# }.play;
# )
# ```

# In[4]:


audio_path = '../../../sounds/grain-saw.mp3'
ipd.Audio(audio_path)


# The [AllpassN](https://doc.sccode.org/Classes/AllpassN.html) *unit generator* implements a *Schroeder allpass filter*.
# It works and sounds very similar to the *comb delay line* but *allpass filters* **change the phase of signals** passed through them.
# For this reason, they are useful even though do not seem to differ much from *comb filters*.
# 
# ```isc
# ({
#     var decaytime = 2.0;
#     var sig = Decay.ar(Impulse.ar(1.0), 0.5) * PinkNoise.ar;
#     sig + AllpassN.ar(sig, 0.5, delaytime: 0.15, decaytime: decaytime);
# }.play;
# )
# ```

# In[5]:


audio_path = '../../../sounds/decay-allpass.mp3'
ipd.Audio(audio_path)


# ## Plucking
# 
# The [Pluck](https://doc.sccode.org/Classes/Pluck.html) *unit generator* realizes a *Karplus-Strong string synthesis* which is a method of [physical modeling](sec-pm) that loops a short waveform through a filtered *delay line* to simulate the sound of a hammered or plucked string or some types of percussion.
# The generator consists of a [OnePole](sec-onepole) lowpass filter and a *delay line*.
# 
# In the following, I tried to recreate the *pluck* using basic *unit generators*.
# I use two synth definitions, one for the *pluck* and the other for the *impulse* generation.
# The *impulse signal* is fed into the *pluck* by using SuperCollider's bus system.
# Evaluate each block one at a time from top to bottom.
# 
# ```isc
# // reconstrucktion of Pluck
# (
# SynthDef(\pluck,{
#     arg in, out;
#     var sig, dsig, local;
# 
#     local = LocalIn.ar(2);
#     sig = In.ar(in, 2);
#     sig = sig + local;
# 
#     local = OnePole.ar(DelayN.ar(sig, 0.01, 0.002), 0.3);
#     sig = OnePole.ar(sig, 0.3);
#     LocalOut.ar(local);
# 
#     Out.ar(out, local + sig);
# }).add;
# )
# 
# // Impulses
# (
# SynthDef(\impulse, {
#     arg out;
#     var sig = WhiteNoise.ar(0.6) * Impulse.ar(2!2);
#     Out.ar(out, sig);
# }).add;
# )
# 
# (
# ~impulses = Group(s, \addToHead);
# ~synths = Group(s, \addToTail);
# )
# 
# (
# ~impulse = Synth(\impulse, [\out, 4], ~impulses);
# ~pluck = Synth(\pluck, [\in, 4, \out, 0], ~synths);
# )
# ```

# In[6]:


audio_path = '../../../sounds/pluck-reimpl.mp3'
ipd.Audio(audio_path)


# I also make use of [Groups](https://doc.sccode.org/Classes/Group.html), a concept I did not cover yet.
# [Groups](https://doc.sccode.org/Classes/Group.html) help me to bring the synths in the right order on the audio server.
# ``\impulse`` is a synth that outputs impulses of *white noise*.
# This impulse is read by ``\pluck``, therefore, ``\pluck`` has to operate after ``\impulse``.
# Since I add the ``~impulse`` group to the head and the ``~synths`` group to the tail, all synth in the ``~impulse`` group operate before synths in the ``~synths`` group.
# 
# The following signal flow graph shows how the output is computed.
# 
# 
# ```{figure} ../../../figs/sounddesign/filters/pluck.png
# ---
# width: 800px
# name: fig-pluck
# ---
# Signal-flow graph of the construction above.
# ```
# 
# Using [Pluck](https://doc.sccode.org/Classes/Pluck.html) instread, generates a slightly different sound:
# 
# ```isc
# ({
# Pluck.ar(
#     in: WhiteNoise.ar(0.1!2), 
#     trig: Impulse.kr(2), 
#     maxdelaytime: 0.002, 
#     delaytime: 0.002, 
#     decaytime: 10, 
#     coef: 0.3)
# }.play;
# )
# ```

# In[7]:


audio_path = '../../../sounds/pluck.mp3'
ipd.Audio(audio_path)


# ## Reverberation
# 
# SuperCollider offers out of the box *reverberation unit generators*: [FreeVerb](https://doc.sccode.org/Classes/FreeVerb.html), [FreeVerb2](https://doc.sccode.org/Classes/FreeVerb2.html), and [GVerb](https://doc.sccode.org/Classes/GVerb.html).
# 
# In this example, I use *grains* sampled from a single sine wave that changes its frequency whenever the envelope is triggered.
# ``\gverb`` applies reverb to the grain.
# This time I do not make use of [Groups](https://doc.sccode.org/Classes/Group.html), therefore, I have to be careful of the oder in which I add synth to the audio server.
# 
# ```isc
# (
# SynthDef(\sin_grain, {
#     arg out = 0;
#     var n = 10, sig, env, trigger, freqs;
#     trigger = Dust.kr(5);
#     env = EnvGen.ar(Env.sine(0.02), trigger);
#     freqs = Dseq(Array.exprand(n, 100, 5000), inf);
# 
#     sig = SinOsc.ar(Demand.kr(trigger, 0 ,freqs)) * env * \amp.kr(0.2);
#     sig = Splay.ar(sig);
#     Out.ar(out, sig);
# }).add;
# )
# 
# (
# SynthDef(\gverb, {
#     arg in, out=0;
#     var sig = GVerb.ar(
#         in: In.ar(in, 1), // mono input
#         roomsize: 15, // in square meters
#         revtime: 3, // in seconds
#         damping: 0.13, // 0 => complete damping, 1 no damping
#         inputbw: 0.13, // damping control but on the input
#         spread: 15,
#         drylevel: 1,
#         earlyreflevel: 0.3,
#         taillevel: 0.1,
#         maxroomsize: 300);
#     Out.ar(out, sig!2);
# }).add;
# )
# 
# (
# ~gverb = Synth(\gverb, [\in, 4, \out, 0]);
# ~grains = Synth(\sin_grain, [\out, 4]);
# )
# ```

# In[8]:


audio_path = '../../../sounds/grain-gverb.mp3'
ipd.Audio(audio_path)

