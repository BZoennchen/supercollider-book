#!/usr/bin/env python
# coding: utf-8

# (sec-event-player)=
# # Event Player
# 
# Let us have a look at a first, very simple composition.
# We finally make use of [Pbind](https://doc.sccode.org/Classes/Pbind.html) to construct a *discreate musical event simulation*.
# 
# ```isc
# (
# Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], 4),
#     \dur, 0.4,
#     \sustain, 0.1 
# ).play;
# )
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/event-player-ex1.mp3'
ipd.Audio(audio_path)


# As already mentioned, [Pbind](https://doc.sccode.org/Classes/Pbind.html) is a unique [Pattern](https://doc.sccode.org/Classes/Pattern.html) that generates a [Stream](https://doc.sccode.org/Classes/Stream.html) that spits out (musical) [Events](https://doc.sccode.org/Classes/Event.html).
# Using the ``play`` method on the [Pbind](https://doc.sccode.org/Classes/Pbind.html) pattern, we play all the events the event stream gives us.
# In the above example we play a sequence of three notes 4 times on the ``\default`` instrument each seperated by ``0.4`` beats sustaining ``0.1`` beats.
# 
# ``dur`` determines the waiting time between two successive events.
# Thereby, we do not play all events instantly.
# Instead we create a rhythm.
# 
# ```{admonition} Legato and Duration
# :name: remark-legato-duration
# :class: remark
# If the sound sustains longer than ``dur`` we get overlapping sounds, i.e., [legato](sec-legato).
# ```
# 
# Legato is nice to control the amount of overlap relative to the duration of the event. For example:
# 
# ```isc
# (
# p = Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], 4),
#     \dur, 0.25,
#     \sustain, 0.5
# ).play;
# )
# ```
# 
# The same can be achieved by using the ``legato`` parameter:
# 
# ```isc
# (
# p = Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], 3),
#     \dur, 0.25,
#     \legato, 1.0 // two times dur overlap
# ).play;
# )
# ```

# In[2]:


audio_path = '../../../sounds/event-player-legato.mp3'
ipd.Audio(audio_path)


# We can call ``stop`` on the [Stream](https://doc.sccode.org/Classes/Stream.html) (not the [Pattern](https://doc.sccode.org/Classes/Pattern.html)!) to stop it (or we can hit ``CMD`` + ``.`` / ``Ctrl`` + ``.`` as always).
# 
# Now you might ask: what do the events actually look like?
# As already mentioned, each event is filled with default arguments if they are not defined.
# For each defined argument, in our case, ``instrument``, ``freq``, ``dur``, and ``legato``, the method ``next`` is called on the value referenced by the corresponding name.
# As we learned, if this value is a number, the number itself is returned.
# If it is a pattern, it was already transformed into a stream when ``play`` was called and will return what the recursive evaluation of ``next`` gives us.
# 
# ## Argument Dependence
# 
# Since we combine multiple [Streams](https://doc.sccode.org/Classes/Stream.html) we may want to influence one value stream by the other.
# For example, we might want that the ``amp`` depends on the frequency such that we can reduce the amplitude for higher pitches.
# There are multiple ways to do so.
# One is by using one of the most powerful [Pattern](https://doc.sccode.org/Classes/Pattern.html), that is [Pfunc](https://doc.sccode.org/Classes/Pfunc.html).
# 
# [Pfunc](https://doc.sccode.org/Classes/Pfunc.html) expects a function as an argument and this function is called whenever the respective [Stream](https://doc.sccode.org/Classes/Stream.html) generates its next value.
# The argument of the ``next`` call is passed to the function.
# 
# ```isc
# (
# var pattern = Pfunc({arg val; val*val;});
# var square = pattern.asStream();
# square.next(5);
# )
# ```
# 
# [Pbind](https://doc.sccode.org/Classes/Pbind.html) passes the whole event to this function.
# Therefore, we can look inside the event, and use the information to compute our value.
# In the following code snippet, we print the ``amp`` so you can see the effect.
# 
# ```isc
# (
# p = Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], inf),
#     \dur, 0.25,
#     \legato, 0.2,
#     \amp, Pfunc({|e| min(1.0, e[\freq].linexp(100, 500, 1.0, 0.2)).postln;})
# ).play;
# )
# ```
# 
# [Pfunc](https://doc.sccode.org/Classes/Pfunc.html) can do a lot of other things and there is a pattern that is specifically designed for our case.
# It is called [Pkey](https://doc.sccode.org/Classes/Pkey.html).
# Furthermore, we can use [utility function](sec-utility-debugging) ``trace`` to post the numbers a pattern spits out.
# The following code creates exactly the same sound.
# 
# ```isc
# (
# p = Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], inf),
#     \dur, 0.25,
#     \legato, 0.2,
#     \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2).trace
# ).play;
# )
# ```
# 
# The third way to do this is to use a global variable.
# However, this seems to be a really dirty method which I do not recommend.
# I think, using [Pkey](https://doc.sccode.org/Classes/Pkey.html) is the cleanest way to do things.
# 
# ## Cascading Pbinds
# 
# We can, of course, use multiple [Pbinds](https://doc.sccode.org/Classes/Pbind.html).
# 
# ```isc
# (
# var intro, middle, outro;
# intro = Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], 3),
#     \dur, 0.25,
#     \sustain, 0.3,
#     \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
# );
# 
# middle = Pbind(
#     \instrument, \default,
#     \freq, Pseq([233, 321, 344], 3),
#     \dur, 0.25,
#     \sustain, 0.3,
#     \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
# );
# 
# outro = Pbind(
#     \instrument, \default,
#     \freq, Pseq([440, 320, 430], 3),
#     \dur, 0.25,
#     \sustain, 0.3,
#     \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
# );
# 
# p = Pseq(list: [intro, middle, outro], repeats: 2);
# q = p.play;
# )
# ```
# 
# What a masterpiece ;).
# We can generate the same piece using only one [Pbind](https://doc.sccode.org/Classes/Pbind.html):
# 
# ```isc
# (
# p = Pbind(
#     \instrument, \default,
# 	\freq, Pseq([
# 		Pseq([440, 220, 330], 3), 
# 		Pseq([233, 321, 344], 3),
# 		Pseq([440, 320, 430], 3)
# 	], repeats: 2),
#     \dur, 0.25,
#     \sustain, 0.3,
#     \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
# );
# q = p.play;
# )
# ```

# In[3]:


audio_path = '../../../sounds/event-player-pbind-comb.mp3'
ipd.Audio(audio_path)


# We can also play multiple [Pbinds](https://doc.sccode.org/Classes/Pbind.html) in parallel.
# We can imagine that each [Pbind](https://doc.sccode.org/Classes/Pbind.html) represents one musician in our assemble.
# [Ppar](http://doc.sccode.org/Classes/Ppar.html) is a pattern that allows us to play multiple [Pbinds](https://doc.sccode.org/Classes/Pbind.html) in parallel.
# In this example I use a fixed ``dur`` and [Rest](http://doc.sccode.org/Classes/Rest.html) to adjust the actual duration.
# You can use any symbol to create a [Rest](http://doc.sccode.org/Classes/Rest.html) (i.e. do nothing).
# 
# ```isc
# (
# SynthDef(\snare,{arg hcutoff = 9000, lcutoff = 5000, amp = 1.4;
#     var env, hat, bass, sig, cutoff = 5000;
#     env = Env.perc(0.01, 0.15).kr(doneAction: Done.freeSelf);
#     hat = {PinkNoise.ar()}!2;
#     hat = HPF.ar(hat, XLine.ar(lcutoff/4, lcutoff, 0.2));
#     hat = LPF.ar(hat, hcutoff);
#     bass = LFTri.ar(XLine.kr(150, 10, 0.21))*0.2;
#     sig = (hat + bass) * env * amp;
#     Out.ar(0, sig);
# }).add;
# )
# 
# (
# var melody = Pbind(
#     \instrument, \default,
#     \scale, Scale.minor,
#     \octave, 5,
#     \degree, Pseq([
#         3, 4, 3, \r,
#         1, \r, 6, \r,
#     ], inf),
#     \dur, 1/4,
#     \sustain, 0.2
# );
# 
# var rythm = Pbind(
#     \instrument, \snare,
#     \dur, 1/8,
#     \amp, Pseq([
#         0.9, 1.2, \r, \r, 
#         0.8, \r, 1.3, \r,
#     ], inf)*0.2
# );
# 
# Ppar([rythm, melody], inf).play;
# )
# ```

# In[4]:


audio_path = '../../../sounds/event-player-ppar.mp3'
ipd.Audio(audio_path)


# Another way to sequence [Pbinds](http://doc.sccode.org/Classes/Pbind.html) and [Pattern](http://doc.sccode.org/Classes/Pattern.html) is to use [Pspawner](https://doc.sccode.org/Classes/Pspawner.html).
# It allows you to play patterns in parallel or in sequence, via a callback function.
# 
# ```isc
# (
# var melody = Pbind(
#     \instrument, \default,
#     \scale, Scale.minor,
#     \octave, 5,
#     \degree, Pseq([
#         3, 4, 3, \r,
#         1, \r, 6, \r,
#     ]),
#     \dur, 1/4,
#     \sustain, 0.2
# );
# var rythm = Pbind(
#     \instrument, \snare,
#     \dur, 1/8,
#     \amp, Pseq([
#         0.9, 1.2, \r, \r, 
#         0.8, \r, 1.3, \r,
#     ])*0.2
# );
# 
# Pspawner({ arg sp;
#     3.do {
#         sp.par(melody);
#         sp.seq(rythm);
#         sp.seq(rythm);
#     };
#     sp.seq(rythm);
#     sp.seq(melody);
# }).play;
# )
# ```

# In[5]:


audio_path = '../../../sounds/event-player-pspawner.mp3'
ipd.Audio(audio_path)


# Later we will see that we can organize our piece by using multiple [Pbind](http://doc.sccode.org/Classes/Pbind.html).
# But for now, let's move on.
# 
# ## Dynamic Changes
# 
# Ok, so we can define a pattern of events, i.e., a [Pbind](http://doc.sccode.org/Classes/Pbind.html) and play it.
# But would it not be nice to change the pattern while playing it?
# SuperCollider supports live programming via its powerful [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html).
# I will discuss live programming in detail in section [Live Coding](sec-live-coding), but here, I want to mention the [Pbindef](https://doc.sccode.org/Classes/Pbindef.html) class.
# 
# [Pbindef](http://doc.sccode.org/Classes/Pbindef.html) keeps a reference to a [Pbind](http://doc.sccode.org/Classes/Pbind.html) in which single keys can be replaced.
# It plays on when the old stream ends and a new stream is set and schedules the changes to the beat.
# Basically, this means that we can:
# 
# 1. change our pattern
# 2. re-evaluate the code 
# 
# and the change will appear soon after without ever stopping the pattern.
# The only difference to [Pbind](http://doc.sccode.org/Classes/Pbind.html) is that a [Pbindef](http://doc.sccode.org/Classes/Pbindef.html)  requires a unique name.
# Use the following [Pbindef](http://doc.sccode.org/Classes/Pbindef.html) , change the frequencies and re-evaluate the code.
# Listen to what happens!
# 
# ```isc
# (
# Pbindef(\melody,
#     \instrument, \default,
#     \freq, Pseq([440, 220, 330], inf),
#     \dur, 0.4,
#     \sustain, 0.1 
# ).play;
# )
# ```
# 
# There is, however, a pitfall.
# If you are using [Pbindef](http://doc.sccode.org/Classes/Pbindef.html)  and you change your style of defining pitch, you might run into problems.
# Once you define ``\freq``, there is no way to use any other argument that determines the frequency since it will always be overwritten by ``\freq``.
# For example, try ``\midinote`` in the above example. 
# You will notice that it does not work.
# If you change the name of the [Pbindef](http://doc.sccode.org/Classes/Pbindef.html)  it will work as long as you do not define the ``\freq`` argument!
# Another solution is to set ``\freq`` to ``nil``.
# 
# ```{admonition} Overwriting Arguments
# :name: attention-overwriting-args
# :class: attention
# Once you use an argument within a ``Pbindef`` you can only unuse it by overwriting it or by setting it to ``nil``!
# ```
# 
# ## Naming Conventions
# 
# As mentioned in section [Value Conversions](sec-value-conversion), behind the scenes SuperCollider's event player helps us transforming different values into other values.
# For example, we can play ``\midinote`` instead of ``\freq``.
# The player will convert the pitch to the correct frequency.
# 
# However, we can only take advantage of this support if we name the arguments of the function defined in the [SynthDef](http://doc.sccode.org/Classes/SynthDef.html) appropriately.
# 
# ```{admonition} Naming Conventions
# :name: attention-naming-convention
# :class: attention
# Always use the appropriate names, such as ``amp`` and ``freq`` for your ``SynthDef`` arguments!
# ```
