(sec-midi)=
# MIDI

In the article [An introduction to MIDI](https://web.archive.org/web/20120830211425/http://www.doc.ic.ac.uk/~nd/surprise_97/journal/vol1/aps2/), *Andrew Swift* states that the musical instrument digital interface is a technical standard (a sort of agreement) that describes a communications protocol, digital interface, and electrical connectors that connect a wide variety of electronic musical instruments, computers, and related audio devices for playing, editing, and recording music.

If a modern music producer presses a key on his MIDI device, such as a keyboard or launchpad, she sends a piece of information directly to the computer.
I have a little keyboard that I can connect to my computer via USB, and if I press a key on the keyboard, that is exactly what happens.
However, since no program is listening to incoming MIDI commands, nothing is happening.
If I start a digital workstation such as [Helm](https://tytel.org/helm/) (after I connect my MIDI device to my computer), the application reacts to me playing the keyboard.

## Listening to MIDI-messages

SuperCollider is perfectly capable to listen to incoming MIDI-commands:

```isc
// Connect SuperCollider to all possible MIDI-devices of this computer
MIDIIn.connectAll;    

// Print out every MIDI-command SuperCollider is receiving.
MIDIFunc.trace(true);   
```

If I press a key on the keyboard, the post window shows the following message:

```
MIDI Message Received:
    type: noteOn            // type of the command
    src: 668746688          // device id
    chan: 0                 // channel number
    num: 52                 // key id
    val: 104                // value (velocity for noteOn)
```

and if I release the key, the following shows up:

```
MIDI Message Received:
    type: noteOff           // type of the command
    src: 668746688          // device id
    chan: 0                 // channel number
    num: 52                 // key id
    val: 127                // value (velocity for noteOff)
```

Pressing multiple keys results in multiple messages.
MIDI messages/commands are made up of 8-bit words (1 byte) that are transmitted serially at a rate of 31.25 kbit/s.
A message consists of a status byte, which indicates the type of the message, followed by up to two data bytes that contain the parameters.

There are five types, but here we are only looking at the *channel voice message* since they can be used to control our instrument by transmitting real-time performance data over a single channel, i.e., to all devices listening to that channel.
MIDI notes are numbered from 0 to 127 assigned to $\text{C}_{-1}$ to $\text{G}_9$ corresponding to a range of $8.175799$ to $12543.85$ Hz (assuming equal temperament and 440 Hz for $\text{A}_4$).

## Playing a Non-Sustaining Synth

Now let us suppose we have the following percussive synth defined by the following ``SynthDef``.

```isc
(
SynthDef(\tri, {
    arg freq=200, harm=8, rel=0.6, amp=0.3, out=0;
    var sig, env;
    sig = {LFTri.ar(freq + Rand(-2.0, 2.0))}!8;
    sig = Splay.ar(sig);
    sig = RLPF.ar(sig, (freq*harm).clip(20, 20000), 0.5);
    env = EnvGen.ar(Env.perc(0.001, rel), doneAction: Done.freeSelf);
    sig = sig * env * amp;
    Out.ar(out, sig);
}).add;
)
```

Playing the synth via my keyboard is rather easy after we connected SuperCollider to all MIDI-devices using ``MIDIIn.connectAll;``
We can use the ``MIDIdef.noteOn`` callback function to execute code if a MIDI-message of type ``noteOn`` arrives.

```isc
(
MIDIdef.noteOn(\on, {
    // value, num = midi note, channel and src = device
    arg val, num, chan, src;
    Synth(\tri, [\amp, 0.1, \freq, num.midicps, \harm, exprand(4,20)]);
});
)
```

We are perfectly capable of playing multiple notes without a problem since we can forget about the synth after it is scheduled on the audio server because it will be automatically destroyed by the ``doneAction: Done.freeSelf`` configuration.

## Playing Sustainable Synth

If we wanna control the length of a note via keyboard we need a sustaining envelope within the ``SynthDef``.
Let us change the definition accordingly.
I change only one line of the definition introducing an attack-sustain-release envelope using a fast attack, a sustain level at half the amplitude and a parameterizes release.

```isc
env = EnvGen.ar(Env.asr(0.001, 0.5, rel), gate: gate, doneAction: Done.freeSelf);
```

Most importantly, the envelope has a gate!
When we release the key, my keyboard sends a ``noteOff`` MIDI-message and we have to set the gate argument to 0.
To do so, we need a reference to the synth running on the audio server.
Therefore, I introduce a global variable ``~synth`` that I initialize when the keyboard sends a ``noteOn`` message.

```isc
(
MIDIdef.noteOn(\on, {
    arg val, num, chan,src;
    ~synth = Synth(\tri, [\amp, 0.1, \freq, num.midicps, \harm, exprand(4,20)]);
});

MIDIdef.noteOff(\off, {
    arg val, num, chan,src;
    ~synth.set(\gate, 0);
});
)
```

This works as long as we only play one note at a time.
If two ``noteOn`` messages arrive before any ``noteOff``message does, the reference of the first synth is lost, and we can no longer terminate it.

Since it is impossible to press the same key twice before releasing it, we can save each synth reference within an array where the index of the array slot corresponds to the key number ``num``.
To be absolutely safe, we only play a new synth if the old one got removed.
The MIDI key numbers on my keyboard range from 0 to 120.

```isc
(
~synths = Array.fill(127, nil);
MIDIdef.noteOn(\on, {
    arg val, num, chan,src;
    if(~synths[num] == nil, {  // To be absolutely save
        ~synths[num] = Synth(\tri, [
            \amp, 0.1, 
            \freq, num.midicps, 
            \harm, exprand(4,20)]);
    });
});

MIDIdef.noteOff(\off, {
    arg val, num, chan,src;
    if(~synths[num] != nil, {  // To be absolutely save
        ~synths[num].set(\gate, 0);
        ~synths[num] = nil;    // Remove the reference
    });
});
)
```

I use 127 here since this will give us $2^7$ possibilities, guessing that ``num`` is expressed via 7 bit.

## Beyond Playing Synths

We can, of course, bind the MIDI note to anything.
For example, we could use different octaves for different synths.
We could also trigger specific patterns using our MIDI device.
The limits are our imaginations.