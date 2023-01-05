(sec-filters)=
# Subtractive Synthesis and Filters

In [additive synthesis](sec-additive-synthesis) we start with silence and add more and more simple wave forms together to achieve a complex sound.
*Subtractive synthesis* works the opposite.
We start with rich / complex signal, such as *white noise* and apply *filters* to reduce, remove, or even amplify the amplitude of certain frequency bands.
Consequently, if we talk about subtractive synthesis, we have to talk about **filters**!

>Any medium through which the music signal passes, whatever its form, can be regarded as a filter. 
However, we do not usually think of something as a filter unless it can modify the sound in some way. 
For example, speaker wire is not considered a filter, but the speaker is (unfortunately).
-- Julius O. Smith

A *digital filter* is just a filter that operates on digital signals, such as sound represented inside a computer.
Because of how we normally interprete the term *filter* our fundamental understanding of filters might be that they make parts of the signal quieter -- which is not the whole story.
Filters have a 

1. **amplitude filter response**, and
2. **phase response**.

Apart from changing the level of specific frequencies, filters often change the phase of the signal, e.g., $\sin(2\pi t)$ is transformed to $\sin(2\pi t + 0.5\pi)$.
Some filters do primarily apply such period shifts and we might not think of them as filters.
For example, the *allpass filter* does passes all frequencies untouched but attunes the phases.

*Low pass filters* are used everywhere because they can smoothen the harshness of a sound.
A lot of filters allow support a feedback cycle, i.e., the output signal of the filter goes back into the filter.
Each time the signal is fed into the filter, its level gets reduced such that the feedback eventually comes to an end.
Such feedback can be used to synthesis reverberation.
In combination with an *impulse* (e.g. [Impuse](https://doc.sccode.org/Classes/Impulse.html)) filters can be used to contruct surprising effects.
And with ressonance, filters can add many aspects to the timbre of a sound.

[SuperCollider](https://supercollider.github.io/) offers a large variety of filters.
Execute

```isc
Filter.dumpClassSubtree;
```

to print a list of all filters to the post window.

In summary, filters and substractive synthesis are inseperable.

+ We can use static filters to emphasize specific frequencies.
+ We can use static filters to create formants in a sound and imitate the characteristics of the human voice or traditional acoustic instruments.
+ A [resonance filter](sec-resonance) with a moderate *resonance bandwidth* with a cutoff frequency that tracks the pitch can create a characteristic quality that remains tonally consistent as we play the keyboard.
+ For some *resonance filters*, if we decrease the *resonance bandwidth*, we enter an area where the filter is at the brick of self-oscillation. This creates a distinctive distortion that can be a perfect starting point.
+ If we decrease the *resonance bandwidth* even further, the filter will become a sine wave generator in its own right. In theory, no input signal is passed at this point, but few filters altogether remove all the signal, and the result is a tortured sound that has extensive uses in modern music.

In analog synthesis, filters are the defining element of a synthesizer.
They are also crucial in digital synthesis, and if you are into creative synthesis, your sound generation will depend upon what you have and what you do with it.