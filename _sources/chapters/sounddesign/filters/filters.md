(sec-filters)=
# Subtractive Synthesis / Filters

The fundamental understanding of filters might be that they make parts of the signal quieter -- which is wrong.
They do far more than attenuate some frequencies.
Because many filters use some feedback cycle, they can be challenging to understand. 

Filters are essential for *subtractive synthesis*.
Filters do not only change the level of specific frequencies but apply a phase shift.
Many of the filters only apply such a shift, and we often do not think of them as filters.

Let me summarize some of the applications of filters:

+ We can use static filters to emphasize specific frequencies.
+ We can use static filters to create formants in a sound and imitate the characteristics of the human voice or traditional acoustic instruments.
+ A *resonance filter* with a moderate *resonance bandwidth* with a cutoff frequency that tracks the pitch can create a characteristic quality that remains tonally consistent as we play the keyboard.
+ For some *resonance filters*, if we decrease the *resonance bandwidth*, we enter an area where the filter is at the brick of self-oscillation. This creates a distinctive distortion that can be a perfect starting point.
+ If we decrease the *resonance bandwidth* even further, the filter will become a sine wave generator in its own right. In theory, no input signal is passed at this point, but few filters altogether remove all the signal, and the result is a tortured sound that has extensive uses in modern music.

In analog synthesis, filters are the defining element of a synthesizer!
They are also crucial in digital synthesis, and if you are into creative synthesis, your sound generation will depend upon what you have and what you do with it.