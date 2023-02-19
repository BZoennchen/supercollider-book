#!/usr/bin/env python
# coding: utf-8

# # Utility Functions
# 
# Since SuperCollider is used to generate sound and music, it has built-in functions that are special to the field of audio processing.
# I will introduce some of these functions which I think are most important and useful.
# 
# We perceive the frequency and the loudness of sound on a logarithmic scale.
# For example, doubling the frequency pushes the pitch, one, not two, octaves higher.
# However, we often want to deal with linear measures since humans are certainly imperfect at grasping non-linear relationships intellectually.
# Therefore, musicians use semitones instead of frequencies, see section [Notes & Midi Notes](sec-notes).
# 
# ## Frequency and Semitones
# 
# The function ``x.midiratio`` computes the factor to multiply a frequency $f$ such that it will be changed by ``x`` semitones.
# 
# The function ``y.midicps`` converts a [midi note](sec-midi-notes) into the respective frequency (assuming a twelve-tone equal temperament tuning (12-TET)).
# 
# The function ``z.cpsmidi`` is the inverse of ``midicps``.
# It transforms the frequency ``z`` into a midi note (possibly a floating point number). 
# 
# The function ``w.ratiomidi`` is the inverse of ``midiratio``.
# It transforms ``w`` the factor to multiply a frequency with into the semitones added to the pitch to have the same effect.
# 
# ```isc
# 60.midicps                      // 261.6255653006
# 1.midiratio                     // 1.0594630943591
# 1.0594630943591.ratiomidi       // 0.99999999999681 (almost 1)
# 
# 261.6255653006 * 1.midiratio    // 277.18263097681
# 277.18263097681.cpsmidi         // 60.999999999996 (almost 61)
# ```
# 
# Especially if we defines a [synth definition](sec-synths), we want to deal with frequencies.
# The [pattern library](sec-playing-events) takes care of many value conversions such that we can use midi notes, degrees of a scale etc out of the box.
# However, if we introduce more specific arguments we can not rely on that comfort.
# It is handy to offer tonal arguments such as ``detune`` in a measure of semitones because the linear scale is more meaningful to us.
# To be able to still use measures in frequency we use, for example, ``midicps``.
# 
# ## Amplitude and Decibel
# 
# To use decibal instead of amplitude, where 0 decibal is equivalent to 1.0 amplitude, we can make use of the built-in functions ``x.ampdb`` and ``y.dbamp``.
# ``x.ampdb`` converts a loudness value in amplitude into decibal.
# ``y.dbamp`` is the inverse operation.
# 
# ```isc
# -3.dbamp        // 0.70794578438414
# -3.dbamp.ampdb  // -3.0
# ```
# 
# ## Example
# 
# In the following example we use frequency for ``\freq``, amplitude for ``\amp`` and semitones for ``\detune``.
# Furthermore, we convert -7 decibals into amplitude and make use of ``k.reciprocal`` which computes ``1/k``.
# 
# ```isc
# (
# SynthDef(\detune_sines, {
#     arg freq=440, detune=0.2, amp = 0.5;
#     var sig, env;
#     sig = SinOsc.ar(freq * [0.0, detune, (-1)*detune].midiratio);
#     sig = sig * amp * 3.reciprocal;
#     sig = Splay.ar(sig);
#     Out.ar(0, sig);	
# }).add;
# )
# 
# Synth(\detune_sines, [\freq, 440, \amp, -7.dbamp, \detune: 0.01]);
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/detune-sines.mp3'
ipd.Audio(audio_path)

