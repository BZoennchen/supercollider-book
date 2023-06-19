---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Inharmonic Series

In [Harmonic Series](sec-harmonic-series), we build a sound consisting only of specific harmonics, which gives us a harmonic sound.
We added a slight frequency modulation to simulate a vibrato effect to make the sound more natural.
Furthermore, we increased the steepness of the envelope for increasing frequency to emulate the natural phenomenon of faster disappearing high frequencies.

Let us now synthesize a sound consistent of many inharmonics.
My motivation is to generate a sound similar to the Glockenspiel.
Let's listen to a sample:

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/original-glockenspiel.mp3'
ipd.Audio(audio_path)
```

It has a metallic but still very clear sound.
Each metal plate is tuned to a certain pitch, i.e. it has to have harmonic content.
The envelope is percussive with; a short attack and a long release.

To achieve the metallic sound I use a bunch of inharmonics and mix in harmonics to fix the pitch.


TODO!