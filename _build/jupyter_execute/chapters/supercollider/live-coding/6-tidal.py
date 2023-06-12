#!/usr/bin/env python
# coding: utf-8

# # TidalCycles
# 
# I aim to demonstrate how one can utilize other intriguing environments like [Sarine](https://sardine.raphaelforment.fr/) or [Sonic Pi](https://sonic-pi.net/) in conjunction with SuperCollider. I have specifically chosen to explore [*TidalCycles*](https://tidalcycles.org/) or *Tidal*.
# 
# ## What is TidalCycles
# 
# As hinted at in my discussion of [pattern](sec-playing-pattern), different syntaxes, environments, languages, or technology in general can unlock new possibilities while simultaneously limiting others. Therefore, remaining open to a variety of tools until we find what we envision is invaluable.
# 
# Similar to SuperCollider, Tidal is a free and open-source coding environment, written in  ``Haskell`` by [Alex McLean](https://slab.org/).
# However, unlike SC, it focuses on live coding for algorithmic patterns. 
# Behind the scenes, Tidal uses SuperCollider's audio server to run synths. 
# Essentially, Tidal triggers events that will be executed by SuperCollider.
# 
# One might ask, why should I be interested in Tidal when it merely triggers SC events? 
# Well, using Tidal transforms your mindset entirely because it is based on the cycle and promotes a more transformative and linear flow of information.
# 
# With SuperCollider's [pattern](sec-playing-pattern), you have to conceive of the construction of events by combining multiple streams, each responsible for a specific argument. 
# Consequently, you have to manage a *non-linear flow of information*. 
# This can make it challenging to change or establish certain effects on the fly, as it is hard to keep the graph in your head, and to achieve a simple *linear* change, you often have to modify multiple streams.
# 
# Tidal introduces limitations (a specific structure), i.e., *the cycle*, and mutations on the flow that make intriguing on-the-fly changes easier. 
# It enables you to compose complex music with just a few lines of code.
# It relies on [SuperDirt](https://github.com/musikinformatik/SuperDirt), a general-purpose framework for playing samples and synths, controllable over the [Open Sound Control](sec-osc) protocol, and locally from the SuperCollider language. 
# Essentially, SuperDirt sits on top of SuperCollider.
# 
# ## Cycles
# 
# *TidalCycles* operates on the basis of **cycles** that run in the background, synchronized. 
# This means that the timing of events isn't based on a flexible start time and duration, but on how the event is positioned in relation to other events. There's no need to specify absolute timings. 
# By default, an event starts at the beginning of a cycle and spans the duration of a complete cycle.
# For example,
# 
# ```haskell
# d1 $ s "hh"
# ```
# 
# plays the sample "hh" (hi-hat) starting the sample at the beginning cycle for duration of one cycle which lasts for ``0.5625`` seconds by default.
# In fact, ``d1 $ s "hh"`` is a *pattern* which is a connection to the [SuperDirt](https://github.com/musikinformatik/SuperDirt) synthesizer one can use to play audio samples, synthesizers, and so on.
# We can use ``d1, d2, ..., d9`` and even our own named patterns.
# 
# One can change the *cycle per second* using ``setcps``:
# 
# ```haskell
# setcps (200/60/4)
# ```
# 
# By adding more "events", we change the alignment of events within a cycle but not the cycle itself.
# The following will schedule two events triggering a hi-hat but each will occupy half a cycle.
# 
# ```haskell
# d1 $ s "hh hh"
# ```
# 
# To achieve the same effect in SuperCollider, we would have to adjust the duration of the events accordingly.
# The drawback of Tidal on the other hand might be that we have to stick to the rigid thinking in cycles.
# 
# ## Combining Pattern
# 
# A core feature of *Tidal* is the ease in which one can combine pattern using *pattern matching* -- a technique of *functional programming*.
# *Tidal* always "trys" to find a way to match pattern even though they seem not really matchable.
# 
# For example,
# 
# ```haskell
# "2 3" + "4 5 6"
# ```
# 
# matches the Elements ``2``, ``3`` to ``4``, ``5``, and ``6`` but how?
# There are different possibilities.
# If the *structure* comes from the left, then this would result in ``"6 8"``.
# If the structure comes from the right, then we get ``"6 7 9 "`` and if it comes from both sides (which is the default) we get ``"6 7 8 9"``.
# 
# For example, in the following the cycle consists of 5 drum-, hh-, bd-events modified by different amount of a crush effect.
# The *structure* comes from both sides:
# 
# ```haskell
# d1 $ s "drum hh bd" + crush "2 2.2 10 2"
# ```
# 
# ``+`` is the same as writing ``|+|``.
# Using ``#`` or ``|+`` will cause the structure coming from the left, resulting in 3 events per cycle.
# 
# ```haskell
# d1 $ s "drum hh bd" # crush "2 2.2 10 2"
# ```
# 
# ## Further Reading
# 
# There's much more to explore. 
# For instance, the [mini notation](https://tidalcycles.org/docs/reference/mini_notation) s its own language within the Tidal language. 
# However, there are other, superior sources out there to study the possibilities of Tidal.
# For more information I recommand to have a look at the official website: [TidalCycle](https://tidalcycles.org/).
# What I aim going to illustrate here is how we can utilize our synth, defined by  ``SynthDef`` in *Tidal*.
# 
# ## Synthesizers
# 
# To use a SuperCollider synth in *Tidal* we have to transform it into a [SuperDirt](https://github.com/musikinformatik/SuperDirt) synth.
# First, make sure SuperDirt is running.
# 
# Then, let us take the basic synth ``\sine_beep`` defined in section [Synthesizers](sec-synths) and transform it into a SuperDirt synth.
# 
# ```isc
# (
# SynthDef(\sine_beep, {
#     arg freq = 440, amp = 0.5;
#     var sig, env;
#     env = Env([0,1,0], [0.01, 0.4], [5,-5]).ar(doneAction: Done.freeSelf);
#     sig = SinOsc.ar(freq: freq, mul: amp) * env!2;
#     Out.ar(0, sig);
# }).add;
# )
# ```
# 
# SuperDirt offers/requires some default arguments that it uses to control the scheduling of the synth:
# 
# + ``out``: the output channel
# + ``sustain``: the duration of the sound (default is 1)
# + ``freq``: the fundamental of the synth
# + ``speed``: controls how fast a sample is played back which will influence the pitch of the sample. Therefore, for a synth one might want to adjust the fundamental by ``speed``(default is 1)
# + ``begin``: controls at what position the playback of the sample will starts (between 0 and 1). Therefore, for a synth one might want to adjust the envelope accordingly (default is 0).
# + ``end``: controls at what position the playback of the sample will ends (between 0 and 1). Therefore, for a synth one might want to adjust the envelope accordingly (default is 1).
# + ``pan``: controls the panning (between -1 and 1, default is 0)
# + ``accelerate``: not sure
# + ``offset``: not sure
# 
# Let us adjust our ``SynthDef`` accodingly by introducing all those arguments and by removing ``amp``.
# We can keep our custom arguments but we do not require ``amp`` since SuperDirt will control the volume via ``gain``.
# In addition, we have to replace the unit generator [Out](https://doc.sccode.org/Classes/Out.html) with a more accurate version, that is, [OffsetOut](https://doc.sccode.org/Classes/OffsetOut.html).
# 
# ```isc
# (
# SynthDef(\sine_beep, {
#     arg out=0, accelerate=1, offset,  pan=1, freq=440, sustain=1, speed=1, begin=0, end=1, atk = 0.01;
#     var sig, env, rate;
# 
#     env = EnvGen.kr(
#         Env([0,1,0], [atk, sustain-atk], [5,-5]),
#         timeScale: sustain,
#         doneAction: Done.freeSelf
#     );
# 
#     sig = SinOsc.ar(freq: freq!2);
#     OffsetOut.ar(out, DirtPan.ar(sig, ~dirt.numChannels, pan, env));
# }).add;
# )
# ```
# 
# That's it!
# The ``timeScale`` argument of ``EnvGen`` scales the duration of our synth dependent on ``sustain``.
# Even if we do not use all arguments, we can already use ``\sine_beep``.
# 
# ```haskell
# d1 $ n "[7 0 3 0]*2" # s "sine_beep"
# ```
# 
# We are not using some of the arguments and that is ok.
# Some of these arguments might not make any sense for our synth.
# For example, ``begin`` and ``end`` could be used to start the envelope at a different position but most of the time this makes no sense because it would make the sound undesirable.
# 
# Let us take another example: the synth we created in section [Harmonic Series](sec-harmonic-series).
# This time I make use of the ``speed`` argument.
# Depending on ``speed``, I shorten the sustain of the envelope and increase the fundamental frequency.
# Furthermore, I use the control-rate notation, which also works just fine.
# 
# 
# ```isc
# (
# SynthDef(\sine_sum, {
#     var sig, harmonics, amps, phases;
# 
#     harmonics = [1, 3, 5, 6, 7, 8, 9];
#     phases = [0, 0, 0, 0.5, 0.25, 0, 0] * 2*pi;
#     amps = [0.5, 0.1, 0.2, 0.6, 0.6, 0.1, 0.1].normalizeSum();
# 
#     sig = harmonics.collect({ arg k, index;
#         var env = EnvGen.ar(Env.perc(
#             attackTime: \attk.kr(0.01) * Rand(0.8,1.2),
#             releaseTime: \rel.kr(5.0) * Rand(0.9,1.1),
#             curve: \curve.kr(-4)),
#         timeScale: \sustain.kr(1) / \speed.kr(1.0),
#         );
# 
#         var vibrato = 1 + LFNoise1.ar(\detuneFreq.kr(5)!2).bipolar(\detune.kr(0.015));
#         var harmonicFreq = \freq.kr(440) * \speed.kr(1.0) * vibrato * abs(k);
#         amps[index] * SinOsc.ar(harmonicFreq, phases[index]) / k * env.pow(1+((abs(k)-1)/3));
#     }).sum;
# 
#     sig = LPF.ar(sig, 1500);
#     sig = sig * \amp.kr(0.5);
#     DetectSilence.ar(sig, doneAction: Done.freeSelf);
#     OffsetOut.ar(\out.kr(0), DirtPan.ar(sig, ~dirt.numChannels, \pan.kr(0)));
# }).add;
# )
# ```
# 
# Let's try it out using a little two more complex pattern.
# 
# ```haskell
# d1 $ jux rev 
#     $ chunk 4 (fast 2 . (|- n 12)) 
#     $ off 0.25 (|+ 7) 
#     $ struct (iter 4 "t(5,8)")
#     $ n (scale "ritusen" "0 .. 7") 
#     # sound "sine_sum"
#     # gain 1.4
# 
# d2 $ jux rev 
#     $ n "3 ~ 0 [~ 3]" 
#     # s "clap" 
#     # speed 2
#     # gain (slow 8 $ range 0.8 1.2 sine)
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/tidal-sine-sum.mp3'
ipd.Audio(audio_path)


# The second one, ``d2``, plays samples from the ``clap`` directory in my samples folder. 
# The gain function takes the control pattern (cpattern) on the left and sets the amplitude to the number provided as the first argument, in this case, ``(slow 8 $ range 0.8 1.2 sine)``. 
# Although ``sine`` produces numbers ranging from -1 to 1, using range 0.8 1.2 modifies these values to 
# 
# ```haskell
# (+-1) * (upper-lower) + lower
# ``` 
# 
# resulting in a range of 0.4 to 1.2. The function ``speed 2`` raises the pitch of a sample by approximately one octave.
# 
# The structure of the pattern is defined by ``n "3 ~ 0 [~ 3]"``. Here, ``~`` represents a rest. 
# Thus, sample ``3`` is triggered at the onset of the cycle with a duration of 1/4 cycle. 
# This is followed by a rest of the same length. 
# Sample ``0`` is then triggered at the halfway point of the cycle. 
# Next, there is a 1/8 rest and another trigger of sample 3.
# 
# Lastly, ``rev`` is used to reverse a control pattern. However, since we use jux, this reversal is applied only to the right-hand channel.
# 
# The first pattern ``d1`` is more complicated.
# The best way to understand a pattern is listen to it while creating it.
# Let me try to explain the missing functions.
# ``off`` applies a function to a pattern, and layers up the result on top of the original pattern but shifted by a certain amount of time (measured in cycles).
# In this example, we add ``7`` (to the structure coming from the left) and shifting the result by 1/4 of a cycle.
# 
# ``iter`` divides a pattern into a given number of subdivisions, plays the subdivisions in order, but increments the starting subdivision each cycle.
# ``struct`` places a rhythmic *boolean* structure on the pattern you give it.
# In combination we generate a complex boolean pattern.
# The ``scale`` function interprets a pattern of note numbers into a particular named scale.
# ``"0 .. 7"`` results in ``"0 1 2 3 4 5 6 7"``.
# ``chunk`` divides a pattern into a given number of parts, then cycles through those parts in turn, applying the given function to each part in turn (one part per cycle).
# Therefore, ``chunk 4 ...`` applies ``(fast 2 . (|- n 12))`` to 1/4 of a cycle, where ``fast 2 . (|- n 12)`` is a composition of ``fast 2`` and ``|- n 12``, i.e., increasing the speed and reducing the note by one octave.
# The order in which theses transformations and functions are applied is determined by the ``$``, ``#`` and the brackets.
# ``$`` has the lowest priority and the brackets the highest.
# 
# Thus first 
# 
# ```haskell
#     $ n (scale "ritusen" "0 .. 7") 
#     # sound "sine_sum"
# ```
# 
# is evaluated.
# Then the ``# gain 1.4``.
# Then we are working us step by step up to ``d1``.
# 
# For further information, please look into the [official documentation](https://tidalcycles.org/docs/reference/even-more).
