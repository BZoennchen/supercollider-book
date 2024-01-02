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
import numpy as np
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
import matplotlib.pyplot as plt
import scipy.special
import seaborn as sns
from scipy.integrate import cumtrapz

dpi = 300
transparent = True
PI = np.pi
TWO_PI = 2*PI
NUM = 44000
show = False
cmap='coolwarm'

sns.set_theme('paper')
sns.set_style("whitegrid")
```

# FFT Processing

Before we start I highly recommand that you read section [Discrete Fourier Transform](sec-dft) since this section depends on it.

## Short-Time Fourier Transform

To compute the DFT and IDFT using the FFT algorithm in [SuperCollider (SC)](https://supercollider.github.io/), we use the unit generators [FFT](https://doc.sccode.org/Classes/FFT.html) and [IFFT](https://doc.sccode.org/Classes/IFFT.html), respectively.
And because the fast Fourier transform algorithm is so efficient, we can do it in real time!
Therefore, we "work" in frequency space by

1. Transforming the signal into the frequency space using the [FFT](https://doc.sccode.org/Classes/FFT.html) unit generator
2. Manipulating the coefficients as we desire
3. Transforming the signal back to the time domain using the [IFFT](https://doc.sccode.org/Classes/IFFT.html) unit generator

````{admonition} FFT and IFFT Buffers
:name: attention-fft-ifft-sc
:class: attention

[FFT](https://doc.sccode.org/Classes/FFT.html) and [IFFT](https://doc.sccode.org/Classes/IFFT.html) unit generators require a buffer to store the frequency-domain data. 
This buffer must have exactly **one** channel. 
Multichannel buffers are not supported.

To do [FFT](https://doc.sccode.org/Classes/FFT.html) processing on a multichannel signal, provide an array of mono buffers, one for each channel. 
Then, [FFT](https://doc.sccode.org/Classes/FFT.html)/[IFFT](https://doc.sccode.org/Classes/IFFT.html) will perform [multichannel expansion](sec-mce), to process each channel separately.
````

The following example has no effect on the input 'in' since we merely transform the signal and then promptly revert it.

```isc
(
{
    var in, out, chain, freq = 200;
    in = SinOsc.ar(freq);

    chain = FFT(
        buffer: LocalBuf(2048), 
        in: in, 
        hop: 0.5, // offset of te next FFT, rnages from > 0 to <= 1.
        wintype: 0, // -1 triangle, 0 sine, 1 Hann
        active: 1, // 1 active, <= 0 inactive
        winsize: 0 // 0 => equal to the buffer
    ); 	

    // here we could manipulate the coefficients
    chain.inspect; 
    out = IFFT(chain); // inverse FFT
    out;
}.play;
)
```

To process sound SuperCollider has a selection of phase vocoder (PV) unit genertors which are commonly used as in place operators on the [FFT](https://doc.sccode.org/Classes/FFT.html) data.
SuperCollider [phase vocoder](https://doc.sccode.org/Guides/FFT-Overview.html#PV%20and%20FFT%20UGens%20in%20the%20Standard%20Library) is a technique used in computer music to manipulate blocks of spectral data before reconversion.
The process of buffering, windowing, conversion, overlap-add, etc.

In the following example, we basically filter [WhiteNoise](https://doc.sccode.org/Classes/WhiteNoise.html) by randomly setting most coefficients thus frequencies to zero.
Whenever the impulse triggers [PV_RandComb](https://doc.sccode.org/Classes/PV_RandComb.html) and the selection of non-zero frequencies changes.
Since the ``windowsize`` determines the lowest frequency we can capture, increasing the buffer size will reduce the pitch of the result.

```isc
(
{
    var in, chain;
    in = WhiteNoise.ar(0.8);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_RandComb(chain, 0.95, Impulse.kr(0.4));
    IFFT(chain)
}.play;
)
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd

audio_path = '../../sounds/fft-wnoise.mp3'
ipd.Audio(audio_path)
```

Plotting the [spectrogram](sec-spectrogram) reveals the effect visually.

```{code-cell} python3
---
tags: 
    - remove-input
mystnb:
  image:
    width: 900px
  figure:
    name: spec-1
    caption: Spectrogram of the generated signal. 
---
import librosa
import matplotlib.pyplot as plt

x, sr = librosa.load('../../sounds/fft-wnoise.mp3')

hop_length = 512
n_fft = 2048
C = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)
S = librosa.amplitude_to_db(abs(C))

plt.figure(figsize=(15, 5))
librosa.display.specshow(S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear', cmap=cmap);
plt.colorbar(format='%+2.0f dB');
```

If we want to modify spectral data individually, we can utilize ``pvcollect``.
In the following instance, I simulate [PV_RandComb](https://doc.sccode.org/Classes/PV_RandComb.html) by using a random [Array](https://doc.sccode.org/Classes/Array.html) named ``active`` that contains zeros and ones.
Moreover, the operation 

```isc
index.linexp(b.numFrames, 0, 0.3, 1.0);
``` 

reduces the amplitude of high frequencies.
To infuse movement, I deploy 2048 low-frequency [Pluse](https://doc.sccode.org/Classes/Pluse.html) unit generators.
Since ``active`` is smaller than the number frames/windows, i.e. ``b.numFrames`` I utilize ``wrapAt`` to wrap around.
Consequently, a pattern of active frequencies is repeated.

```isc
(
{
    var in, chain, b, active, g_amp = 14.0;
    b = LocalBuf(2048);
    active = Array.fill(200, {if(1.0.rand > 0.97, 1, 0)});
    in = PinkNoise.ar();
    chain = FFT(b, in);

    chain = chain.pvcollect(b.numFrames, {|mag, phase, bin, index|
        var factor = index.linexp(b.numFrames, 0, 0.3, 1.0);
        var amp = Pulse.kr(
            rrand(3, 20), 
            rrand(0.1, 0.8)).range(0, 0.9) * factor;
            
        [mag*amp*active.wrapAt(index)*g_amp, phase]
    });

    Pan2.ar(IFFT(chain))
}.play;
)
```

```{code-cell} python3
:tags: [remove-input]

audio_path = '../../sounds/fft-pvcollect.mp3'
ipd.Audio(audio_path)
```

Again, let us look at the [spectrogram](sec-spectrogram):

```{code-cell} python3
---
tags: 
    - remove-input
mystnb:
  image:
    width: 900px
  figure:
    name: spec-2
    caption: Spectrogram of the generated signal. 
---

x, sr = librosa.load('../../sounds/fft-pvcollect.mp3')

hop_length = 512
n_fft = 2048
C = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)
S = librosa.amplitude_to_db(abs(C))

plt.figure(figsize=(15, 5))
librosa.display.specshow(S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear', cmap=cmap);
plt.colorbar(format='%+2.0f dB');
```

You might notice the repeating frequncy pattern.

## Mel Frequency Cepstral Coefficients

I introduced the [mel-spectogram](sec-mel-spectrogram) in the section [discrete Fourier transform](sec-dft) and I recommand reading it before you continue.

In the following example, we use two synth.
One creates the audio signal and the other applies a mel-analysis and sends 13 mel-coefficient to a control bus.
Every 0.1 second we read from the control bus and store the data in an $n \times 13$ array.

```isc
(
SynthDef(\signal, {
    var sig, n = 25;
    sig = 0;
    n.do {
        arg i;
        var harmonic = SinOsc.ar((i+1)!2 * \freq.kr(440));
        harmonic = harmonic * ((i+1)**2).reciprocal * exprand(1.0, 0.1);
        sig = sig + harmonic;
    };
    sig* 0.5;
    Out.ar(\out.kr(0), sig);
}).add;

SynthDef(\mel, {
    var sig, fft, array;
    sig = In.ar(\in.kr(0));
    fft = FFT(LocalBuf(1024), sig);
    array = MFCC.kr(fft, numcoeff: 13);
    Out.kr(\cout.kr(0), array); // control bus out
    Out.ar(\out.kr(0), Pan2.ar(sig)); // audio bus out
}).add;
)

(
var audio = Bus.control(s, numChannels: 2);
var control = Bus.audio(s, numChannels: 2);
var data = [];

a = Synth(\mel, [in: audio, out: 0, cout: control]);
b = Synth(\signal, [freq: 150, out: audio]);
a.setn(1!13);
	
fork {
    100.do {
        control.getn(13, { |val| { data.add(val); }.defer });
        0.1.wait;
    };
    data.postln;
    a.free;
    b.free;
}.play;
)
```

```{code-cell} python3
:tags: [remove-input]

audio_path = '../../sounds/mel-ex1.mp3'
ipd.Audio(audio_path)
```

Then I plot the ``data`` array in ``Python``.

```{code-cell} python3
---
tags: 
    - remove-input
mystnb:
  image:
    width: 900px
  figure:
    name: mel-example-1
    caption: Mel-spectrogram of the generated signal. 
---
import numpy as np
import matplotlib.pyplot as plt

# Assuming 'mfccs' is your numpy array with shape (timesteps, 13)
# For example:
# mfccs = np.random.rand(100, 13)  # Dummy data

mfccs = np.array([ [ 0.19543661177158, 0.60864043235779, 0.40062326192856, 0.19973906874657, 0.35547721385956, 0.41562807559967, 0.26596361398697, 0.24172988533974, 0.32264801859856, 0.24569401144981, 0.16687235236168, 0.0, 0.0 ] ])

def plot_mfcc(mfccs):
    plt.figure(figsize=(15, 5))
    plt.imshow(mfccs.T, aspect='auto', origin='lower', cmap=cmap)
    plt.ylabel('MFCC Coefficients')
    plt.xlabel('Time')
    plt.title('MFCCs over Time')
    plt.colorbar(label='Amplitude')
    plt.show()

plot_mfcc(mfccs)
```
