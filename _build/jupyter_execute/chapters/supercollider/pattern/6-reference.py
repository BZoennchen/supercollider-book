#!/usr/bin/env python
# coding: utf-8

# # Reference
# 
# There are many different ``Pattern``, I will only discuss some of them which I find most important.
# The official [documentation of SuperCollider](https://doc.sccode.org/) is not always super helpful but the tutorial [Understanding Streams, Patterns and Events](https://doc.sccode.org/Tutorials/Streams-Patterns-Events1.html) is an excellent source to get started.
# 
# ## Primary Pattern
# 
# If you want to use the pattern library the following patterns are your bread and butter.
# 
# ### Lists
# 
# [Pseq](https://doc.sccode.org/Classes/Pseq.html) is the most basic pattern that can be used to play through a list of values.
# It is useful for deterministic number generatrion, e.g. playing a specific chord progression but also to combine non-deterministic patterns.
# ``repeats`` (which can be infinit ``inf``) spcifies how often the pattern goes through the list.
# ``offset`` indicate the starting index.
# 
# ```isc
# // [ 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2 ]
# Pseq(list: [1,2,3,4], repeats: 3, offset: 2).asStream.all;
# ```
# 
# [Prand](https://doc.sccode.org/Classes/Prand.html) chooses items from the list randomly (same as list.choose).
# You can reduce randomness if you but the same item into the list multiple times (or you use [Pwrand](https://doc.sccode.org/Classes/Pwrand.html) instead).
# 
# ```isc
# // e.g. [ 4, 3, 4, 3, 3, 2, 1, 3, 2, 4 ]
# Prand(list: [1,2,3,4], repeats: 10).asStream.all;
# ```
# 
# [Pxrand](https://doc.sccode.org/Classes/Pxrand.html) chooses randomly, but never repeat the same item twice.
# 
# ```isc
# // e.g. [ 2, 1, 2, 4, 3, 1, 4, 1, 2, 4 ]
# Pxrand(list: [1,2,3,4], repeats: 10).asStream.all;
# ```
# 
# [Pshuf](https://doc.sccode.org/Classes/Pshuf.html) shuffles the list in random order, and use the same random order ``repeats`` times.
# This introduces randomness deterministically.
# 
# ```isc
# // e.g. [ 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2 ]
# Pshuf(list: [1,2,3,4], repeats: 3).asStream.all;
# ```
# 
# [Pwrand](https://doc.sccode.org/Classes/Pwrand.html) choose randomly by weighted probabilities (like list.wchoose(weights)).
# **Tipp:** use ``normalizeSum`` to guarantee that weights add up to 1.0.
# 
# ```isc
# // e.g. [ 1, 2, 1, 2, 2, 2, 1, 2, 2, 2 ]
# Pwrand(list: [1,2,3,4], weights: [20, 30,1, 5].normalizeSum, repeats: 10).asStream.all;
# ```
# 
# ### Series
# 
# [Pseries](https://doc.sccode.org/Classes/Pseries.html) generates numbers according to the arithmetic series (addition).
# 
# ```isc
# // [ 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1 ]
# Pseries(start: 1, step: -0.1, length: 10).asStream.all;
# ```
# 
# [Pgeom](https://doc.sccode.org/Classes/Pgeom.html) generates numbers according to the geometric series (multiplication).
# 
# ```isc
# // [ 1, 0.5, 0.25, 0.125, 0.0625 ]
# Pgeom(start: 1, grow: 0.5, length: 5).asStream.all;
# ```
# 
# ### Distributions
# 
# [Pwhite](https://doc.sccode.org/Classes/Pwhite.html) generates random numbers equal/uniformly distributed (*white noise*), like ``rrand(lo, hi)``.
# 
# ```isc
# // e.g. [ 0.55498147010803, 1.88440990448, 1.8215901851654, 1.8560950756073 ]
# Pwhite(lo: 0, hi: 2.0, length: 4).asStream.all;
# ```
# 
# [Pexprand](https://doc.sccode.org/Classes/Pexprand.html) generates random numbers exponentially distributed, like ``exprand(lo, hi)``.
# **Attention:** Zero can not be in the interval!
# 
# ```isc
# // e.g. [ 0.35829930578573, 1.0719818402671, 1.0689460460456, 0.12406136454322 ]
# Pexprand(lo: 0.1, hi: 2.0, length: 4).asStream.all;
# ```
# 
# [Pbrown](https://doc.sccode.org/Classes/Pbrown.html) generates numbers according to the Brownian motion, arithmetic scale (addition).
# The ``step`` argument determines the maximum change per step.
# Internal, the pattern uses ``xrand2`` to determine the next step change, i.e., a uniform distribution fron ``-step`` to ``+step``.
# 
# ```isc
# // e.g. [ 0.044661736488342, 0.12499458789825, 0.20763206481934, 0.30759530067444 ]
# Pbrown(lo: 0, hi: 5, step: 0.1, length: 4).asStream.all;
# ```
# 
# (sec-pattern-ref-function)=
# ### Functions
# 
# [Pkey](https://doc.sccode.org/Classes/Pkey.html) gets the value of another ``key`` of a [Pbind](https://doc.sccode.org/Classes/Pbind.html).
# The ``key`` has to be specified before it can be accesed.
# In the following example we control the amplitude ``\amp`` via the ``\midinote`` we are playing such that higher notes are louder.
# 
# ```isc
# (
# Pbind(
#     \midinote, Prand([65,66,68,70], inf),
#     \amp, Pkey(\midinote).linlin(65, 70, 0.3, 1.0),
#     \dur, 0.25
# ).trace.play;
# )
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/pattern-ref-pkey.mp3'
ipd.Audio(audio_path)


# ```isc
# // e.g. [ 3, 1, 3, 0, 0 ]
# Pfunc(nextFunc: {4.rand}, resetFunc: {}).asStream.nextN(5)
# ```
# 
# [Pfunc](https://doc.sccode.org/Classes/Pfunc.html) gets the stream values from a user-supplied function.
# 
# ```isc
# // e.g. [ 3, 1, 3, 0, 0 ]
# Pfunc(nextFunc: {4.rand}, resetFunc: {}).asStream.nextN(5)
# ```
# 
# [Pfuncn](https://doc.sccode.org/Classes/Pfunc.html) gets values from the function, but stop after ``repeats`` items.
# 
# ```isc
# // e.g. [ 3, 3, 2, 1, 0, 0, 0 ]
# Pfuncn(func: {4.rand}, repeats: 7).asStream.all;
# ```
# 
# [Prout](https://doc.sccode.org/Classes/Prout.html) uses the function like a routine.
# The function should return values using ``.yield`` or ``.embedInStream``.
# The folling code constructs a pattern that spits out the first 10 Fibonacci numbers.
# 
# ```isc
# // [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ]
# (
# Prout(routineFunc: {
#     var fib0 = 0, fib1 = 1, tmp = 0;
#     10.do {
#         fib0.yield;
#         tmp = fib0;
#         fib0 = fib1;
#         fib1 = tmp + fib1;
#     }
# }).asStream.all;
# )
# ```
# 
# ## Secondary Pattern
# 
# ### Lists
# 
# [Pser](https://doc.sccode.org/Classes/Pser.html) similar to [Pseq](https://doc.sccode.org/Classes/Pser.html) it plays through a list but the number of resulting times is defined by the second argument ``repeats``.
# 
# ```isc
# // [ 1, 2, 3 ]
# Pser(list: [1,2,3,4], repeats: 3, offset: 0).asStream.all;
# ```
# 
# [Pslide](https://doc.sccode.org/Classes/Pslide.html) plays overlapping segments from the list.
# 
# ```isc
# // [ 2, 3, 4, 5, 4, 5, 6, 1, 6, 1, 2, 3 ]
# (
# Pslide(
#     list: [1,2,3,4,5,6], 
#     repeats: 3, 
#     len: 4, 
#     step: 2, 
#     start: 1, 
#     wrapAtEnd: true).asStream.all;
# )
# ```
# 
# [Pwalk](https://doc.sccode.org/Classes/Pwalk.html) realizes a *random walk* over the list.
# The direction and the steps of the walk can be controled by patterns.
# 
# ```isc
# // [ 1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 1, 2, 3, 4 ]
# (
# Pwalk(
#     list: [1,2,3,4,5], 
#     stepPattern: Pseq([1,1,-1,1,1,-1], inf), 
#     directionPattern: 1, 
#     startPos: 0).asStream.nextN(15);
# )
# ```
# 
# [Place](https://doc.sccode.org/Classes/Place.html) interlaces any arrays found in the main list.
# Basically this pattern returns elements in the list. 
# But if an element is an array itself, it embeds the first element when it comes by first time, the second element when it comes by the second time and so on.
# The $n$-th when it comes by the $n$-th time.
# This can be very useful when we build a melodies.
# 
# ```isc
# // [ 1, 2, 5, 1, 3, 6 ]
# Place(list: [1,[2,3,4],[5,6]], repeats: 2, offset: 0).asStream.all;
# ```
# 
# [Ppatlace](https://doc.sccode.org/Classes/Ppatlace.html) similar to [Place](https://doc.sccode.org/Classes/Pser.html) but for patterns.
# Compare the following differences:
# 
# ```isc
# // [ 1, 2, 5, 6, 1, 3, 5, 6 ]
# Place(list: [1,[2,3,4],Pseq([5,6])], repeats: 2, offset: 0).asStream.all;
# 
# // [ 1, [ 2, 3, 4 ], 5, 1, [ 2, 3, 4 ], 6 ]
# Ppatlace(list: [1,[2,3,4],Pseq([5,6])], repeats: 2, offset: 0).asStream.all;
# 
# // [ 1, 2, 5, 1, 3, 6 ]
# Ppatlace(list: [1,Pseq([2,3,4]),Pseq([5,6])], repeats: 2, offset: 0).asStream.all;
# ```
# 
# [Ptuple](https://doc.sccode.org/Classes/Pwalk.html) collects the list items into an array as the return value.
# The ``list`` argument has to be an array of pattern.
# 
# ```isc
# // [ [ 1, 10, 4 ], [ 2, 11, 5 ], [ 1, 10, 4 ], [ 2, 11, 5 ] ]
# (
# Ptuple(list: 
#     [
#         Pseq([1,2,3]), 
#         Pseq([10,11,12]), 
#         Pseq([4,5,nil])
#     ], 
#     repeats: 2).asStream.all;
# )
# ```
# 
# ### Distributions
# 
# ### Pattern Manipulation
# 
# If a pattern returns numbers you can do all the math you can do with numbers.
# In addition, patterns can be [composed](sec-function-composition) similar to functions.
# This makes only sense for [Pbind](https://doc.sccode.org/Classes/Pbind.html) or [functional pattern](sec-pattern-ref-function).
# 
# ```isc
# // [ 1.0, 4.0, 9.0, 1.0, 4.0, 9.0 ]
# (Pfuncn(func: {|x| x**2}, repeats: 7) <> Pseq([1,2,3], 2)).asStream.all
# ```
# 
# ```isc
# // ( 'dur': 0.2, 'amp': 1.0, 'freq': 440 ) repeatedly
# (Pbind(\dur, 0.2, \amp, 1.0) <> Pbind(\freq, 440, \amp, 0.5)).trace.play
# ```
# 
# ### Filter Pattern
# 
# Filter pattern are manipulate existing pattern via the *decorator* approach.
# This means they not necessarily reduce the number of values a pattern generates.
# 
# [Pn](https://doc.sccode.org/Classes/Pn.html) repeatedly embed a pattern.
# This pattern is especially hand in the live coding environment when you want to adjust a pattern by decorate it by another pattern.
# If ``key`` is non-``nil``, it sets the value of that key to true whenever it restarts the pattern.
# This can be used to advance patterns enclosed by [Pgate](https://doc.sccode.org/Classes/Pgate.html).
# 
# ```isc
# // [ 1, 2, 3, 1, 2, 3, 1, 2, 3 ] equivalent to Pseq([1,2,3], 3)
# Pn(pattern: Pseq([1,2,3]), repeats: 3, key: nil).asStream.all;
# ```
# 
# [Pdup](https://doc.sccode.org/Classes/Pdup.html) repeat input stream values.
# Very similar to ``Pn`` but instead of repeating the pattern it repeats each value of the pattern.
# 
# ```isc
# // [ 1, 2, 2, 3, 3, 3, 1, 1, 1, 1 ]
# Pdup(n: Pseq([1,2,3,4]), pattern: Pseq([1,2,3], inf)).asStream.all;
# ```
# 
# [Pgate](https://doc.sccode.org/Classes/Pgate.html) listens to the ``key`` and if it is set to ``true`` the gate returns the **next** value in the source pattern.
# Otherwise it will return the **same** value.
# Suppose we want to advance a pattern when some other pattern spits out a specific value.
# ``Pgate`` can be used in that case.
# In the following we change the ``\root`` by 10 [cent](sec-cent-semitones) whenever the ``\rootStep`` spits out ``true``.
# 
# ```isc
# (
# Pbind(
#     \scale, Scale.minorPentatonic,
#     \degree, Pseq([1, 3, 5, 1], 20),
#     \rootStep, Pseq([false, false, true], inf),
#     \root, Pgate(Pseries(0, 0.1, inf), inf, \rootStep),
#     \dur, 0.25
# ).trace.play;
# )
# ```

# In[2]:


audio_path = '../../../sounds/pattern-ref-pgate.mp3'
ipd.Audio(audio_path)


# [Pcollect](https://doc.sccode.org/Classes/Pcollect.html) is the equivalent to ``collect``.
# This pattern is rarely needed since we can treat patterns like numbers.
# 
# ```isc
# // [ 2, 4, 6, 8 ] equivalent to Pseq([1,2,3,4]) * 2
# Pcollect(func: {|x| x*2}, pattern: Pseq([1,2,3,4])).asStream.all;
# ```
# 
# [Pselect](https://doc.sccode.org/Classes/Pselect.html) is the equivalent to ``select``.
# This pattern can be used to literally filter another pattern.
# 
# ```isc
# // [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]
# Pselect(func: {|x| x % 2 == 0}, pattern: Pseq((0..20))).asStream.all;
# ```
# 
# [Preject](https://doc.sccode.org/Classes/Preject.html) similar to ``Pselect`` but selects the exact opposite items.
# This pattern can be used to literally filter another pattern.
# 
# ```isc
# // [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
# Preject(func: {|x| x % 2 == 0}, pattern: Pseq((0..20))).asStream.all;
# ```
# 
# [Pdrop](https://doc.sccode.org/Classes/Pdrop.html) drops the first ``count`` elements from a pattern.
# 
# ```isc
# // [ 4, 5 ]
# Pdrop(count: 3, pattern: Pseq([1,2,3,4,5])).asStream.all;
# ```
# 
# [Pfin](https://doc.sccode.org/Classes/Pfin.html) drops all elements from a stream after the first ``count`` elements.
# It terminates the stream early.
# 
# ```isc
# // [ 1, 2, 3 ]
# Pfin(count: 3, pattern: Pseq([1,2,3,4,5])).asStream.all;
# ```
# 
# [Pfindur](https://doc.sccode.org/Classes/Pfindur.html) limits total duration of **events** embedded in a stream.
# It terminates the stream early.
# **Attention:** Note that ``pattern`` has to be a pattern for an event stream.
# In the following we terminate an infinite event stream early, i.e. after 7 beats.
# 
# ```isc
# (
# Pfindur(
#     dur: 7, 
#     pattern: Pbind(
#         \dur, Pseq([0.25, 0.5, 0.25, 1.0], inf),
#         \midinote, Pseq([65, 67, 69, [50, 62]], inf)
#     ),
#     tolerance: 0.001
# ).play;
# )
# ```

# In[3]:


audio_path = '../../../sounds/pattern-ref-pfindur.mp3'
ipd.Audio(audio_path)


# [Psubdivide](https://doc.sccode.org/Classes/Psubdivide.html) subdivides floating numbers spit out by ``pattern`` into ``n`` parts.
# This is nice to change the rhythm of an event player without influencing its overall duration.
# In the following we split the 0.5 duration note into two 0.25 notes.
# 
# ```isc
# (
# Pbind(
#     \dur, Psubdivide(
#         n: Pseq([1, 2, 1, 1], inf), 
#         pattern: Pseq([0.25, 0.5, 0.25, 1.0], inf)),
#     \midinote, Pseq([65, 67, 69, [50, 62]], inf)
# ).play;
# )
# ```
# 
# With [Pclutch](https://doc.sccode.org/Classes/Pclutch.html) one can control when another ``pattern`` spits out its next or previous value.
# If ``connected`` spits out 1 or ``true``, the next value is spit out, otherwise the previous.
# 
# ```isc
# // [ 1, 1, 2, 2, 2, 2, 3, 4, 4, 4 ]
# (
# Pclutch(
#     pattern: Pseq([1, 2, 3, 4, 5], 3), 
#     connected: Pseq([0, 0, 1, 0, 0, 0, 1, 1], inf)
# ).asStream.nextN(10);
# )
# ```
# 
# To keep the range of numbers spit out by a pattern within a specific range defined by ``lo`` and ``hi``, we can use [Pwrap](https://doc.sccode.org/Classes/Pwrap.html).
# 
# ```isc
# // [ 4, 5, 3, 4, 5, 3, 4, 5, 3, 4 ]
# Pwrap(pattern: Pseq([1,2,3,4,5,6], inf), lo: 3, hi: 5).asStream.nextN(10)
# ```
# 
# To build chords from an arpegio one can use [Pclump](https://doc.sccode.org/Classes/Pclump.html) which packs the values generated by ``pattern`` into arrays of length ``n``.
# 
# ```isc
# //  [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]
# Pclump(n: 2, pattern: Pseq([1,2,3,4,5,6], inf)).asStream.nextN(3)
# ```
# 
# The reverse can be achieved by [Pflatten](https://doc.sccode.org/Classes/Pflatten.html).
# 
# ```isc
# // [ [ 1, 2, 3 ], [ 1, 3, 4 ], 1, 1, 1, [ 1, 2, 3 ] ]
# Pflatten(n: 1, pattern: Pseq([[[[1,2,3], [1,3,4]]], [1,1,1]], inf)).asStream.nextN(6)
# ```
# 
# 
# ### Others
# 
# + [Pfset](https://doc.sccode.org/Classes/Pfset.html)
# + [Psetpre](https://doc.sccode.org/Classes/Psetpre.html)
# + [Paddpre](https://doc.sccode.org/Classes/Paddpre.html)
# + [Pmulpre](https://doc.sccode.org/Classes/Pmulpre.html)
# + [Psync](https://doc.sccode.org/Classes/Psync.html)
# + [Pconst](https://doc.sccode.org/Classes/Pconst.html)
# + [Plag](https://doc.sccode.org/Classes/Plag.html)
# + [Pbindf](https://doc.sccode.org/Classes/Pbindf.html)
# + [Psubdivide](https://doc.sccode.org/Classes/Psubdivide.html)
# + [Pwhile](https://doc.sccode.org/Classes/Pwhile.html)
# + [Pavaroh](https://doc.sccode.org/Classes/Pavaroh.html)
# + [Prorate](https://doc.sccode.org/Classes/Prorate.html)
# + [Pdiff](https://doc.sccode.org/Classes/Pdiff.html)
