#!/usr/bin/env python
# coding: utf-8

# (sec-routines-tasks)=
# # Routines & Tasks
# 
# A [Routine](https://doc.sccode.org/Classes/Routine.html) is like a function that you can evaluate only partly at a time.
# Routines and functions can be used almost interchangeable but routines can be scheduled/played on a clock.
# Within a routine, you use the ``yield`` method to return a value and pause its execution.
# The next time you evaluate the routine, it picks up where it left off.
# In that sense, a routine is similar to a [stream](sec-stream) but it does not only return values but can do stuff, i.e., realize *sideeffects*.
# 
# ```isc
# (
# r = Routine({
#     1.yield;
#     2.yield;
#     3.yield;
# });
# r.next.postln; // 1
# r.next.postln; // 2
# r.next.postln; // 3
# r.next.postln; // nil
# )
# ```
# 
# Routines that return numeric values can be scheduled on a *clock*.
# If we ``play`` the routine, it will be automatically scheduled on the default clock.
# 
# ```isc
# (
# r = Routine({
#     "1".postln;
#     1.yield;
#     "2".postln;
#     2.yield;
#     "3".postln;
#     3.yield;
#     "4".postln;
# });
# r.play;
# )
# ```
# 
# We can schedule the routine on a specific clock ``t`` by providing it via ``r.play(t)``
# 
# *Forking* a function via the ``fork`` keyword will transform the function into a routine and *play* it immediately.
# 
# ```isc
# (
# {
#     "1".postln;
#     1.yield;
#     "2".postln;
#     2.yield;
#     "3".postln;
#     3.yield;
#     "4".postln;
# }.fork;
# )
# ```
# 
# A [Task](https://doc.sccode.org/Classes/Task.html) is a pausable process.
# It can only be played in combination with a *clock*.
# In contrast to a routine, a task can be *paused*.
# In addition, it prevents you from playing it multiple times.
# 
# The following example is from *The SuperCollider Book* {cite}`wilson:2011`.
# Note that when the *task* reaches the line ``nil.yield`` it will *pause*.
# If you evaluate ``t.resume(0)``, it will *resume*.
# The example uses the *gated* [default instrument](sec-default-instrument).
# 
# ```isc
# (
# t = Task {
#     loop {
#         [56, 66, 60, 64].do { |midi|
#             x = Synth(\default, [\freq: midi.midicps]);
#             0.25.wait;
#             x.set(\gate, 0);
#         };
#         x = Synth(\default, [\freq: 64.midicps]);
#         1.wait;
#         x.set(\gate, 0);
#         "Waiting".postln;
#         nil.yield
#     };
# };
# )
# 
# t.play;
# t.resume(0);
# ```
# 
# Routines and task wait by a measure of beats not seconds!
# Therefore, to double the tempo we just have to schedule the routine/task on a clock with double the tempo.
# We can also change the tempo of the clock while playing.
# 
# ```isc
# (
# t = TempoClock(1);
# {
#     2.do {
#         (60..90).do{ |midi|
#             x = Synth(\default, [\freq: midi.midicps]);
#             0.25.wait;
#             x.set(\gate, 0);
#             t.tempo = t.tempo + 0.1;
#         };
#     };
# }.fork(t);
# )
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/routine-clock-change.mp3'
ipd.Audio(audio_path)


# Until now, we played the synth using ``Synth``, which gets translated into an [OSC message](sec-osc), which tells the server to start the synth immediately.
# Most of the time, this is not what we actually want since the timing can be off.
# Instead, one should use
# 
# ```isc
# s.bind { Synth(...) }
# ```
# 
# and also 
# 
# ```isc
# s.bind { synth.set(...) }
# ```
# 
# If you notice inaccurate timings, this might be the problem.
# A more elaborate explanation written by [Nathan Ho](https://nathan.ho.name/) can be found [here](https://scsynth.org/t/why-you-should-always-wrap-synth-and-synth-set-in-server-default-bind/7310/13).
# When we play [events](sec-playing-events) this problem does not appear because the pattern/event library takes care of using ``s.bind``.
# 
# Nathan is also quite opinionated when it comes to [pattern](sec-pattern).
# Interestingly, he prefers to stay away from them.
# 
# >I haven't used Patterns in years. If they don't appeal to you for whatever reason then you can always use Routine and Synth. -- Nathan Ho
