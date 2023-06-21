#!/usr/bin/env python
# coding: utf-8

# # Wavetable Synthesis
# 
# The principle of *wavetable synthesis* is to exchange computation for memory by pre-computing the complete cycle of a specific waveform, save the values in a buffer and then read values from the buffer instead of computing them on the fly.
# 
# Most SC unit generators are actually wavetables!
# If you want certain harmonics in a signal but for each frequency you use the same envelope, then you can save a lot of performance by using a wavetable instead.
# 
# Creating a wavetable in SuperCollider is easy.
# First we need to allocate a [Buffer](https://doc.sccode.org/Classes/Buffer.html) on the server. 
# Then we have to write the one period of our waveform into the buffer.
# Then we can use the buffer to read from it at different frequencies.
# 
# For example, the unit generator [Osc](https://doc.sccode.org/Classes/Osc.html) is able to write out values from the buffer into the output channel.
# The number of elements in a wavetalbe has to be a power of 2.
# 
# First we create a **client-side** [Signal](https://doc.sccode.org/Classes/Signal.html) containing a sinewave.
# 
# ```isc
# ~sig = Signal.sineFill(size: 1024, amplitudes: [1], phases: [0]);
# ```
# 
# Before we can use the signal, we have to convert it into a wavetable format.
# 
# ```isc
# ~wt = ~sig.asWavetable;
# ```
# 
# Then we allocate a **server-side** buffer and load it with the wavetalbe.
# 
# ```{admonition} Wavetalbe Buffer Size
# :name: attention-wavetable-buffer
# :class: attention
# The size of a *buffer* containing a wavetalbe with $n$ signalpoints, has to be of size $2n$.
# ```
# 
# ```isc
# (
# b = Buffer.alloc(s, 2048);
# b.loadCollection(~wt);
# )
# ```
# 
# Finally, we can play it, i.e., the buffer.
# 
# ```isc
# {Osc.ar(b)}.play;
# ```

# In[1]:


audio_path = '../../sounds/wavetable-sine.mp3'
ipd.Audio(audio_path)


# Now, let us define a signal with many harmonics.
# And in fact, let us use another method to directly initialize a buffer.
# 
# ```isc
# (
# var amps = 1.0/[1,3,5,7,9,11,13,15,17];
# b = Buffer.alloc(
#     server: s,
#     numFrames: 512, 
#     numChannels: 1,
#     completionMessage: {|z| z.sine1Msg(amps: amps);},
# );
# )
# 
# {Osc.ar(b, freq: 200)!2}.play;
# ```
# 
# Nothing stops us from constructing very complex waveforms:
# 
# ```isc
# (
# var n = 16;
# b.sine3(
#     freqs: ({exprand(0.75, 30)}!n).sort,
#     amps: ({exprand(0.05, 0.85)}!n).sort.reverse,
#     phase:{rrand(0, 2*pi)}!n
# );
# )
# 
# {Osc.ar(b, freq: MouseX.kr(10,1000,1)) * [1, 2.01] * 0.4}.play;
# ```
# 
# Since we can transform an envelope [Env](https://doc.sccode.org/Classes/Env.html) into a [Signal](https://doc.sccode.org/Classes/Signal.html) and a signal into a [Wavetable](https://doc.sccode.org/Classes/Wavetable.html), we can construct our waveform using an envelople!
# 
# Let us create some crazy wavetables!
# 
# ```isc
# // increase the buffer size
# b = Buffer.alloc(s, 2048);
# 
# (
# var env, n = 16;
# env = Env(
#     levels: ({rrand(0.0, 1.0)}!(n-1) * [1, -1]).scramble,
#     times: {exprand(1,15)}!n,
#     curve: {rrand(-10, 10)}!n,
# );
# b.loadCollection(env.asSignal(1024).asWavetable);
# )
# 
# {LeakDC.ar(Osc.ar(b, freq: MouseX.kr(10,1000,1)) * [1, 2.01] * 0.4)}.play;
# ```
# 
# Since the waveform might be heavily biased towards the positive or negative, we could use [LeakDC](https://doc.sccode.org/Classes/LeakDC.html) to center it at the x-axis.
# 
# Another really useful way to create a signal is the ``waveFill`` method of an instance of a signal.
# Since it is an instance method, we first have to create a signal.
# 
# ```isc
# (
# var sig;
# sig = Signal.newClear(1024);
# sig.waveFill({
#     // x (0 to 2pi), y_old (old value here 0), index
#     arg x, y_old, i;
# 	var y_new = (sin(x**2))**2*3;
# 	y_new = y_new.fold(-1, 1);
# 	y_new
# }, 0, 2*pi);
# sig.plot;
# )
# ```
