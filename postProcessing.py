import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
df = pd.read_csv(r"E:\airwriting\Dataset\2D-Range-Doppler Data\Digit_7\Digit_7_1.csv", header=None)
def complex_str_to_complex(complex_str):
    parts = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', complex_str)
    if len(parts) >= 2:
        real_part = float(parts[0])
        imag_part = float(parts[1])
    else:
        real_part = float(parts[0])
        imag_part = 0.0
        return complex(real_part, imag_part)
    data = df.applymap(complex_str_to_complex).values
    magnitude_spectrogram = np.abs(data)
    plt.imshow(20 * np.log10(magnitude_spectrogram), aspect='auto', cmap='viridis', interpolation='bicubic', 
    extent=[0, 23, 0, 900])
    plt.gca().invert_yaxis()
    plt.show()