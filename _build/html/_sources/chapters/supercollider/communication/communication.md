# Communication

>Humans can not communicate. Only communication can communicate. -- Niklas Luhmann

In this section, I introduce ways to communicate with SuperCollider, i.e., the client (``sclang``) and the audio server (**scsynth**).
There are two primary possibilities:

1. The musical instrument digital interface (MIDI), and
2. The open sound control protocol (OSC)

We use MIDI, a technical standard, to communicate with ``sclang`` via our MIDI devices (keyboards, pads, ...).
It gives us the power to trigger synths, patterns, and anything else using physical (digital) instruments and devices.

OSC, on the other hand, is a network protocol for sound synthesis, computers, and other multimedia devices.
It is at the core of SuperCollider and is much more powerful than the MIDI standard.
Since it is supported by many software applications, e.g., DAWs, it can be used to communicate between different programs running in the network.

I will only give a concise introduction so that the reader can understand what is possible.