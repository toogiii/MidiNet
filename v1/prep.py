import pypianoroll
import numpy as np
multitrack = pypianoroll.read(r"C:\Users\garvg\Downloads\CymaticsLofiToolkit-V1-m2d\Cymatics - Lofi Toolkit\MIDI\Cymatics - Lofi MIDI 9 - D# Maj.mid")
pypianoroll.save("test.npz", multitrack)
x = np.load("test.npz")
print(x["pianoroll_0_csc_shape"])