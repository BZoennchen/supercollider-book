# Bela

Bela is an open-source platform for creating interaction with sensors and sound.
It’s a combination of hardware and software.
It can be used to create responsive, real-time interactive systems with audio and sensors thus new instruments.
While you can program the Bela-device using ``C/C++`` it also provides support for [PureDate](https://puredata.info/), [Csound](https://csound.com/) and [SuperCollider](https://supercollider.github.io/).

Of course, I will only focus on SuperCollider.
I bought myself a *Bela Starter Kit*.
After connecting my device to my computer using a appropriate USB cable and waiting for round about 40 seconds I am ready to go.
A quick start tutorial can be found [here](https://learn.bela.io/get-started-guide/quick-start/).

As described in section [The Ecosystem](sec-ecosystem) SuperCollider consists of three components: the audio server **scsynth**, the language ``sclang`` and the IDE.
Bela replaces the IDE with a browser based IDE which you can access after connecting typing ``http://bela.local/`` into your browser.
Furthermre, **scsynth** is running on the server in real-time and this can be controlled by analog and digital sensors connected to the system.

Because the SuperCollider architecture consists of a audio server and a client, there are two possible modi we can use the Bela device.
First is the *all on Bela* modus where the code execution of the ``sclang`` code (client) and the audio server **scsynth** runs on the Bela device.
We still communicate via [OSC](sec-osc) messages as usual.

The second option is called *remote control*, that is, the client code runs on our laptop or some other device.
Therefore, we establish a the communcation between our laptop and the Bela device via [OSC](sec-osc).
This provides a flexible coding approach for development, so you can continuously and fluidly experiment and try things out.
Once you've finalized your project you may want to run both ``sclang`` and **scsynth** on Bela to be able to run your program without live-coding interaction, for instance to make a stand-alone instrument running on battery.

It’s also possible to [live code](sec-live-coding) Bela from the SuperCollider IDE.

However, we must set some specific settings for the server:

```isc
s = Server.default;

// Set up options for the Bela
s.options.numAnalogInChannels = 2; // can be 2, 4 or 8
s.options.numAnalogOutChannels = 2; // can be 2, 4 or 8
s.options.numDigitalChannels = 0;
s.options.maxLogins = 4;

// allow anyone on the network connect to this server
s.options.bindAddress = "0.0.0.0";

s.options.blockSize = 16;
s.options.numInputBusChannels = 2;
s.options.numOutputBusChannels = 2;
```

After these lines we use

```isc
s.waitForBoot {
    // Your code goes here.
};

// quit if the button is pressed
ServerQuit.add({ 0.exit });
```

TODO