# Open Sound Control

Open Sound Control (OSC) is a protocol for networking sound synthesizers, computers, and other multimedia devices for musical performance or show control purposes.

OSC is ingrained into SuperCollider.
It is its core element.
In fact, whenever we interact with the real-time audio server **scsynth**, for example, when we add a ``SynthDef`` to the server, SuperCollider translates all the code into OSC messages.

Since OSC is a network protocol, the audio server could run on some other machine in our network.
This opens up sheer endless collaborative possibilities.
Via OSC we build connections to musicians, artists, devices and other software systems.
As long as the instance undestands OSC, we can integrate it into our performance.

## Receiving Messages

In the following, I use a [Processing](https://processing.org/) sketch, which sends the position of a square, i.e., its $x$ and $y$ coordinates as OSC messages to the port.

```{figure} ../../../figs/supercollider/communication/processing-xy-input.png
---
width: 400px
name: fig-processing-xy-input
---
```

You can download the sketch [here](http://www.doc.gold.ac.uk/~mas01rf/WekinatorDownloads/wekinator_examples/all_source_zips/Simple_MouseXY_2Inputs.zip).
It was created by [Rebecca Fiebrink](https://researchers.arts.ac.uk/1594-rebecca-fiebrink/) to use it as an example for her incredible project of Creative Computing, i.e., making machine learning techniques more accessible for artists.
We will later use her [Wekinator](http://www.wekinator.org/) in combination with SuperCollider.

We can see that messages are sent to ``/wek/inputs`` and port ``6448``.
If we do not specify a port, SuperCollider listens at

```isc
NetAddr.langPort; // default is 57120
```

If we start the [Processing](https://processing.org/) sketch and run the following code

```isc
(
OSCdef(
    \getCoords,
    {
        arg val; val.postln;
    },
    '/wek/inputs',
    recvPort: 6448
);
)
```

We can see messages like

```
[ /wek/inputs, 248.0, 185.0 ]
```

in the post window.
We receive an [Array](sec-array) of values.
The first value is the ``path`` of the receiver, the second is the $x$ and the third the $y$ coordinate of our square in the sketch.
Let's create a ``SynthDef`` such that we can manipulate the arguments of a playing synth by moving our rectangle around:

```isc
(
SynthDef(\fireworks,{
    var sig;
    sig = Dust.ar([\density.kr(3), \density.kr(3)-0.5]);
    sig = Ringz.ar(sig, freq: \freq.kr(300), decaytime: 0.1) * 0.55;
    sig = FreeVerb.ar(sig, 0.6, 0.9, 0.8);
    sig = LPF.ar(in: sig, freq: \cutofffreq.kr(21000));
    Out.ar(0, sig);
}).add;
)

~fireworks = Synth(\test);

(
OSCdef(
    \getCoords,
    {
        arg val; var x, y;
        x = val[1];
        y = val[2];
        ~fireworks.set(\density, x.linlin(0, 650, 0.6, 10));
        ~fireworks.set(\freq, y.linlin(0, 460, 100, 600));
    },
    '/wek/inputs',
    recvPort: 6448
);
)
```

Ok, nice but that is nothing special.
We could get the same effect by using the [MouseX](https://doc.sccode.org/Classes/MouseX.html) and [MouseY](https://doc.sccode.org/Classes/MouseY.html) ugens without using any explicit OSC communication.
However, this example shows, how OSC opens up the space of possiblities because suddenly we are communicating with another program running in the network.

## Sending Messages

Using OSC we can send messages from the client to the server, the server to the client and the client to the client itself.
First we have to declare a [NetAddr](https://doc.sccode.org/Classes/NetAddr.html) of the receiver.
Let's send a message from the client to the client.

```isc
(
OSCdef(\self, {arg val; val.postln;},'/self');
)

~me = NetAddr("localhost", NetAddr.langPort);
~me.sendMsg('\self', 42);
```

After executing this code you should see the sent message

```
[ /self, 42 ]
```

in the post window.
Of course, the sender can be anyone in the network!

To send OSC messages from the server to the client we use the [SendReply](https://doc.sccode.org/Classes/SendReply.html) ugen.
In the following I use a very simple synth that sends its amplitude back to the client 30 times a second.
Again, we are listening via [OSCdef](https://doc.sccode.org/Classes/OSCdef.html).

```isc
({
    var amp;
    amp = SinOsc.ar(0.25).range(0,1);
    SendReply.kr(Impulse.kr(30), '/amp', amp);
    WhiteNoise.ar(0.2!2) * amp;
}.play;
)

(
OSCdef(\self, {arg val; val.postln;},'/amp');
)
```

You should see the following kind of messages in the post window.

```isc
[ /amp, 1083, -1, 0.60563856363297 ]
```

Note that the fourth value in the array is the actual amplitude.