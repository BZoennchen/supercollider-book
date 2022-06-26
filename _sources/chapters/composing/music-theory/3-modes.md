(sec-modes)=
# Modes

Starting a scale from other than degree 1 or 6 produces additional scales that share the diatonic interval order.
These variations are called *modes*.

We also get the different modes by shifting the *interval order* of the *diatonic scale*.
In SuperCollider we can achieve this by *array rotation* using ``rotate``:

```isc
~majorIntervalOrder = [2,2,1,2,2,2,1]                // major interval order
~minorIntervalOrder = [2,1,2,2,1,2,2]                // (nat.) minor interval order
~intervalToDegrees.(~majorIntervalOrder)             // major degrees
~intervalToDegrees.(~minorIntervalOrder)             // (nat.) minor degrees
~intervalToDegrees.(~majorIntervalOrder.rotate(2))   // (nat.) minor degrees (by rotation)
```

Major and minor scales are synonyms for *Ionian* and *Aeolian modes* -- a quite elaborate naming convention.

The initial degree of a mode is called *final* because typically, music in a mode would end on that note.
For example, the *final* of the *Aeolian mode* is 6.
Since in ``sclang`` we count from zero, and there are 7 degrees, we get ``7-5==2``.

Note that we have to change the *interval order*!
Adding a fixed number of semitones/half steps does not suffice.
If we do so, we change the *key*, i.e., achieve another transformation called [transposition](sec-keys).
