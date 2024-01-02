import librosa
import matplotlib.pyplot as plt
import numpy as np

filename = librosa.example('nutcracker')
x, sr = librosa.load(filename)

hop_length = 512
n_fft = 2048
C = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)
S = librosa.amplitude_to_db(abs(C))

plt.figure(figsize=(15, 5))
librosa.display.specshow(S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear', cmap='magma')
plt.colorbar(format='%+2.0f dB')


M = librosa.feature.melspectrogram(y=x, n_fft=n_fft, hop_length=hop_length, sr=sr, n_mels=13, fmax=8000)

M_dB = librosa.power_to_db(np.abs(M));
plt.figure(figsize=(15, 5))
librosa.display.specshow(M_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, cmap='RdYlBu_r')
plt.colorbar(format='%+2.0f dB');
plt.show()