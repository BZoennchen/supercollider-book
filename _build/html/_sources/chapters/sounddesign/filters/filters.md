(sec-filters)=
# Filters

The very basic understanding of filters might be that they just make parts of the signal quieter -- which is wrong.
They do far more than just attenuate some frequencies.
Because many filters use some kind of feedback cycle, I they can be difficult to understand. 

Filters are essential for *subtractive synthesis*.
Filters do not only change the level of certain frequencies but apply a phase shift.
Many of the filters only apply such a shift and we often do not think of them as filters.

Let me summarize some of the applications of filters:

+ We can use static filters to emphasis certain frequencies.
+ We can use static filters to create formants in a sound, and imitate the characteristics of the human voice or traditional acoustic instruments.
+ A *resonance filter* with a moderate *resonance bandwidth* with a cuttoff frequency that tracks the pitch, can create a characteristic quality that remains tonally consistent as we play the keyboard.
+ For some *resonance filters*, if we decrease the *resonance bandwidth* we enter an area where the filter is at the brick of self-oscillation. This creates a distinctive distortion that can be a very good starting point.
+ If we decrease the *resonance bandwidth* even further, the filter will become a sine wave generator in its own right. In theory, no input signal is passed at this point, but few filters completely remove all the signal, and the result is a tortured sound that has extensive uses in modern music.

In analogue synthesis, filters are the defining element of a synthesizer!
They are crucial, also in digital synthesis, and if you are into creative synthesis, your sound generation will depend upon what you have got and what you do with it.