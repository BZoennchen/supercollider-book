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

# Playing Sound

Let us create the most simple sound possible: the sound of a sine wave.
First, we define a function that returns a so-called unit generator [UGen](sec-ugens) that starts when we call ``play()``.
In fact ``play()`` is shorthand for

1. transforming our [UGen](sec-ugens) into a full [SynthDef](sec-synths) (synth definition), 
2. adding it to the audio server and 
3. executing it by generating a synth on it.

```{admonition} Protect your ears!
:name: attention-protect-your-ears
:class: attention
[SC](https://supercollider.github.io/) will not protect you from any wrongdoing. 
It will play the sound you defined, and if this sound can hurt your ears, you have to be sure to protect them.
It is good practice to use headphones far away from your ears if you do not know what sound to expect!
```

There are hundreds of different [UGens](sec-ugens).
Basically, they spit out real numbers over time. 
For example, [SinOsc](https://doc.sccode.org/Classes/SinOsc.html) samples a sine wave.

```isc
~sine = {arg freq=200; SinOsc.ar(freq, mul: 0.2)};
~sineplay = ~sine.play();
```

If we execute this code, we get a warning that the server ``localhost`` is not running.
We have to boot the real-time audio server **scsynth** first:

```isc
Server.local.boot;  // boots the local server on your machine
//s.boot;           // is equivalent
~sine = {arg freq=200; SinOsc.ar(freq, mul: 0.2)};
~sineplay = ~sine.play();
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/sine-wave.mp3'
ipd.Audio(audio_path)
```

``~sine`` is a function that returns ``SinOsc.ar(freq, mul: 0.2)`` which is a [BinaryOpUGen](https://doc.sccode.org/Classes/BinaryOpUGen.html).

```{admonition} Sound termination
:name: attention-sound-termination
:class: attention
To terminate all sound press ``CMD`` + ``.``. **This might be the most important shortcut of all.**
```

If we press ``CMD`` + ``i`` while the curser is at ``play()`` and we select the implementation for [Function](https://doc.sccode.org/Classes/Function.html), we can see lookup what ``~sine.play()`` actually does:

```isc
play { arg target, outbus = 0, fadeTime = 0.02, addAction=\addToHead, args;
    var def, synth, server, bytes, synthMsg;
    target = target.asTarget;
    server = target.server;
    if(server.serverRunning.not) {
        ("server '" ++ server.name ++ "' not running.").warn; ^nil
    };
    def = this.asSynthDef(
        fadeTime:fadeTime,
        name: SystemSynthDefs.generateTempName
    );
    synth = Synth.basicNew(def.name, server);
        // if notifications are enabled on the server,
        // use the n_end signal to remove the temp synthdef
    if(server.notified) {
        OSCFunc({
            server.sendMsg(\d_free, def.name);
        }, '/n_end', server.addr, argTemplate: [synth.nodeID]).oneShot;
    };
    synthMsg = synth.newMsg(target, [\i_out, outbus, \out, outbus] ++ args, addAction);
    def.doSend(server, synthMsg);
    ^synth
}
```

``play()`` constructs a new [SynthDef](https://doc.sccode.org/Classes/SynthDef.html), adds it to the server, and generates a synth which is returned.
The ``fadeTime`` makes sure that the sound ramps up over a certain amount of seconds.
For example, we can increase ``fadeTime``:

```isc
~sineplay = ~sine.play(fadeTime: 2.0);
```

``play`` comes in handy if we wanna just try something out -- if we want to explore sounds in a quick and dirty way.
For complex synth, we will define our own [SynthDef](https://doc.sccode.org/Classes/SynthDef.html).
