(sec-filters)=
# Subtractive Synthesis

In [additive synthesis](sec-additive-synthesis) we start with silence and add more and more simple wave forms together to achieve a complex sound.
*Subtractive synthesis* works the opposite.
We start with rich / complex signal and apply *filters* to eliminate unwanted frequencies.
If we talk about subtractive synthesis, we have to talk about filters!

The fundamental understanding of filters might be that they make parts of the signal quieter -- which is wrong.
They do far more than attenuate some frequencies.
Apart from changing the level of specific frequencies, filters often change the phase of the signal, e.g., $\sin(2\pi t)$ is transformed to $\sin(2\pi t + 0.5\pi)$. 
Some filters do primarily apply such period shifts and we might not think of them as filters.

A lot of filters allow support a feedback cycle, i.e., the output signal of the filter goes back into the filter.
Each time the signal is fed into the filter, its level gets reduced such that the feedback eventually comes to an end.
Such feedback can be used to synthesis reverberation.

Let me summarize some of the applications of filters:

+ We can use static filters to emphasize specific frequencies.
+ We can use static filters to create formants in a sound and imitate the characteristics of the human voice or traditional acoustic instruments.
+ A [resonance filter](sec-resonance) with a moderate *resonance bandwidth* with a cutoff frequency that tracks the pitch can create a characteristic quality that remains tonally consistent as we play the keyboard.
+ For some *resonance filters*, if we decrease the *resonance bandwidth*, we enter an area where the filter is at the brick of self-oscillation. This creates a distinctive distortion that can be a perfect starting point.
+ If we decrease the *resonance bandwidth* even further, the filter will become a sine wave generator in its own right. In theory, no input signal is passed at this point, but few filters altogether remove all the signal, and the result is a tortured sound that has extensive uses in modern music.

In analog synthesis, filters are the defining element of a synthesizer.
They are also crucial in digital synthesis, and if you are into creative synthesis, your sound generation will depend upon what you have and what you do with it.