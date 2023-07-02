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
from music21 import *
from IPython.display import Image as img
from PIL import Image
```

(sec-piece-analysis)=
# Analysis

## Prelude I

Every pianist played Bach's *Prelude I in C major* at least ten times.
It is made to learn the keys of the piano, especially major and minor chords, but it is also a beautiful and simple piece of music.

(1-4) The piece starts and ends at the tonic C, more preceisly at **C** (**I**), that is, C-E-G.
In the above voices, Bach uses an arpeggio that relentlessly keeps moving through the piece.
Going from **C**=C-E-F (**I**) to **Dm**=D-F-A (**ii**) to D-F-G in the first three top bars and C-E, C-D and B-D in the bottom bars.
Combining **Dm** with C gives us a D minor seventh chord, i.e., **Dm7**.
Furthermore, adding the B to D-F-G gives us G major seventh (G-B-D)-F, i.e. the dominant seventh.
Finally Bach moves back to the tonic **C** and resolves the tention built up by the dominant.
In summary, Bach moves from a major chord, i.e. **C** (I), to a minor chord, i.e., **Dm7** (ii) to **G7** first inversion (V) to **C** (I) thus he establishes the harmonic world of the piece in just four simple bars.

(5-7)  Next, Bach moves into the dominant **Am**/C (first inversion A minor) which leads into a **D7**/C (with the seventh in the base) and then into a **G**/B (first inversion).
Overall we have (vi)-(II)-(V).

(8-11) Bach moves on to **C7**/B into **Am7** and **D7** and again to **G** (V).
From there a long journey back to **C** (I) begins.
In summary: (I)-(vi)-(II)-(V).

(12-15) Bach starts of with a sequence of chord that functionally acts as a [circle of fifths](sec-circle-of-fifths) but that use diminished chords instead.
He takes us into a **C#m7**/G followed by **Dm**/F and **Bm7**/F (diminised) until we land in **Cm**/E.
The tonic, i.e., C is still missing in the base.
In summary: (?)-(?)-(vii)-(?).

(16-19) Bach stretches out the resolution over three more bars: **F7**/E, **Dm7** and **G7**.
Then we finally reach the home **C** again.
In summary: (IV)-(?)-(V)-(I).

```{figure} ./../../../figs/composing/prelude-bach-1.png
---
width: 800px
name: fig-prelude-back-1
---
```

The rest of the piece is a kind of reaffirmation of the tonic.

(20-24) Bach moves again away from the C major into **C7** diminished, **F7**, to the dominant via **F#m7** diminished, **Fm6**/Ab (inverted) with the B acting as a passing note into the dominant **G7**.
Therefore, reaching the dominant feels like a resolution.
In summary: (I)-(IV)-(?)-(?)-(V).

From the dominant Bach moves back to the tonic.

(25-28) The top voice moves chromatically from E to G by **C**/G (E on top), **G7** (F on top), 
**Am** diminisehd seventh (F# added), **C**/G (G on top).
We can clearly preceive some disonance here. 
In summary: (I)-(V)-(vi)-(I).

(29-34) Then we fall down into an F supported by C-D-G which leads smoothly to **G7**.
Now we expect the perfect cadence to end by going home to the tonic **C** but instead Bach gives us one more round using a **C7** diminished and moving into the dominant **D7**/C (third inversion) and finally, via almost all keys except A, into the tonic I, i.e., **C**.
In summary: (?)-(V)-(I)-(V)-(?)-(I).

```{figure} ./../../../figs/composing/prelude-bach-2.png
---
width: 800px
name: fig-prelude-back-2
---
```

## Nuvole Bianche

Let us apply what we have learned by analysing the beginning of the famous piece *Nuvole Bianche* by *Ludovico Enaudi*.

From the signature of the piece we can see that there are 4 diminished accidentals.
Using the [circle of fifths](sec-circle-of-fifths) we can deduce that this hints towards either **Ab** (Ab major) or **Fm** (F minor).
However the piece ends on Ab which strongly hints at **Ab** and indeed that is correct.

```{code-cell} python3
:tags: [remove-input]
c = converter.parse('./../../../compositions/nuvole_bianche.mxl')
c.metadata.title = 'Nuvole Bianche'
c.metadata.movementName = 'Nuvole Bianche'
c.metadata.composer = 'Ludovico Enaudi'
c.show()
```

Therefore, we have the following scale:

Ab-Bb-C-Db-Eb-F-G-Ab

with the following chords:

| Number          | Chord        |
| --------------- | ------------ |
| I               | Ab-C-Eb      | 
| ii              | Bb-Db-F      | 
| iii             | C-Eb-G       |
| IV              | Db-F-AB      |
| V               | Eb-G-Bb      |     
| vi              | F-Ab-C       |
| vii             | G-Bb-Db      |