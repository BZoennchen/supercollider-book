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


```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
```

# Dice Music

The Musikalisches Würfelspiel (German for *musical dice game*) was popular in the 18th century for adding an element of chance to music composition.
Typically, composers would prepare a set of musical phrases and use a dice to randomly put them in sequence.

```{prf:algorithm} Dice Music
:label: alg-dice-music

**Inputs:** The desired length of the piece $n \in \mathbb{N}$.

**Output:** A musical piece consisting of $n$ phrases.

1. Prepare a palette of musical phrases or notes which we can choose from.
2. Start with an empty piece.
3. If the song is shorter than your desired length:
    1. Randomly select a piece of music from the palette, and add it to the piece.
    2. Repeat step 3.
	
4. return the piece.
```

We can do something like this quite easily, by using ``SuperCollider`` to randomly pick out a sequence of notes to construct a piece.
Of course, even if we constrain the process by using only notes from a certain scale, the result sounds quite random.

```isc
(
Pbind(
    \instrument, \default,
    \degree, Pwhite(0, 7),
    \root, 3,
    \scale, Scale.minor,
    \dur, 0.15
).play
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/dice-music-ex1.mp3'
ipd.Audio(audio_path)
```

TODO