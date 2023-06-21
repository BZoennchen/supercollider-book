#!/usr/bin/env python
# coding: utf-8

# # Inharmonic Series
# 
# In [Harmonic Series](sec-harmonic-series), we build a sound consisting only of specific harmonics, i.e., a sound wave consistent of many frequencies which are whole-number multiples of the fundamental.
# This gave us an harmonic tone.
# 
# We added a slight frequency modulation to simulate a vibrato effect to make the sound more natural.
# Furthermore, we increased the steepness of the envelope for increasing frequency to emulate the natural phenomenon of faster disappearing high frequencies.
# In the context of additive synthesis, *inharmonics* refer to frequencies that are **not** whole-number multiples of the fundamental frequency.
# 
# What sounds contain a lot of inharmonic content? 
# Many percussive instruments, like bells, gongs, or xylophones, produce inharmonic overtones. 
# We could use additive synthesis with inharmonics to emulate these types of sounds.
# Moreover, by carefully tuning the inharmonics, we could create complex, evolving pad sounds. 
# These could have a more dissonant or *out of tune* character compared to pads created with harmonics.
# Often metallic sounds, such as those produced by a struck piece of metal, have a high degree of inharmonicity.
# Compare, for instance, the sound of a *Glockenspiel*:

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/original-glockenspiel.mp3'
ipd.Audio(audio_path)


# If you're creating experimental or atonal music, inharmonics could be used to create novel, unusual, or dissonant sounds.
# Finally if we are creating experimental or *atonal* music, inharmonics could be used to create novel, unusual, or dissonant sounds.
# 
# Let us now synthesize a sound consistent of many inharmonics.
# 
# ```isc
# (
# SynthDef(\inharm, {
#   var freqs, sig, env;
#   freqs = \freq.kr(100) * [0.7, 0.8, 1.2, 1.8, 2.23];
# 
#   sig = SinOsc.ar(freqs *.x [1.0, 1.2]);
#   env = EnvGen.ar(
#     Env([0, 1.0, 0], [0.1, 1]), 
#     doneAction: Done.freeSelf);
#   sig = sig * env * freqs.size.reciprocal;
# 	sig = Splay.ar(sig);
#   Out.ar(0, sig);
# }).add;
# )
# 
# Synth(\inharm, [freq: 500]);
# ```

# In[2]:


audio_path = '../../../sounds/inharm.mp3'
ipd.Audio(audio_path)


# Remember, the key to additive synthesis is **balancing and shaping the volume and envelopes of the individual sine waves**. 
# You'll often need to adjust the volumes and envelopes of the inharmonics over time, creating a shifting, evolving sound. 
# This can be quite a complex process, but it allows for a high degree of sonic control and creativity.
# So let us develop the above example further and introduce individual envelopes:
# 
# ```isc
# (
# SynthDef(\inharm, {
#   var freqs, sig, env, amps, envs;
#   freqs = [0.88, 0.92, 1.2, 1.8, 2.23] *.x [1.0, 1.2, 0.91];
#   freqs = freqs.sort * \freq.kr(100);
#   amps = {rand(0.3, 1.0)}!freqs.size;
#   amps = amps.normalizeSum;
#   amps = amps.sort;
# 
#   sig = SinOsc.ar(freqs);
# 
#   envs = freqs.collect {
#     arg element, index;
#     var env = EnvGen.ar(Env(
#       [0, 1.0, 0.3, 0],
#       [ExpRand(0.01, 0.03), Rand(0.3, 1.15), ExpRand(0.2, 0.34)],
#       [Rand(3, 0.4), Rand(-1, 1), Rand(-3, -0.4)]
#     ));
#     env**(index*\envp.kr(1.3)+1);
#   };
# 
#   sig = sig * amps * envs;
#   sig = Splay.ar(sig);
#   DetectSilence.ar(sig, doneAction: Done.freeSelf);
#   Out.ar(0, sig);
# }).add;
# )
# ```
# 
# Please note that in the second line of the [SynthDef](http://doc.sccode.org/Classes/SynthDef.html), we utilize an [adverb](sec-array-adverbs) to multiply each element in the left list with every element in the right one. 
# Furthermore, we organize frequencies and amplitudes in a way that gives more gain to higher frequencies. 
# However, we also ensure these high frequencies decay faster using the formula ``env**(index*\envp.kr(1.3)+1)``.
# 
# Let us use a [pattern](sec-pattern) to play an inharmonic "melody".
# 
# ```isc
# (
# Pbindef(\melody,
#   \instrument, \inharm,
#   \dur, Pseq(0.25!6 ++ [Rest(2.0)], inf),
#   \scale, Scale.minor,
#   \root, 2,
#   \octave, 5,
#   \degree, Pseq([0, 3, 5, 3, 4, 0, Rest()], inf)
# ).play;
# )
# ```

# In[3]:


audio_path = '../../../sounds/inharm-env.mp3'
ipd.Audio(audio_path)


# The result does not sound amazing but we can hear a metallic tendency.
