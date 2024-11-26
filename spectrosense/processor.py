import numpy as np
from scipy.io import wavfile
from scipy import signal
from datetime import datetime
import os

class SignalProcessor:
    """Handles signal processing and spectrogram generation"""
    
    def __init__(self, sample_rate=None):
        self.sample_rate = sample_rate
        
    def load_signal(self, file_path):
        """Load signal from WAV file"""
        sample_rate, data = wavfile.read(file_path)
        self.sample_rate = sample_rate
        return data
    
    def generate_spectrogram(self, data, segment_duration=10):
        """Generate spectrogram from signal data"""
        samples_per_segment = int(segment_duration * self.sample_rate)
        segments = []
        timestamps = []
        
        for i in range(0, len(data), samples_per_segment):
            segment = data[i:i + samples_per_segment]
            if len(segment) < samples_per_segment:
                break
                
            frequencies, times, Sxx = signal.spectrogram(
                segment,
                fs=self.sample_rate,
                nperseg=1024,
                noverlap=512
            )
            
            Sxx_db = 10 * np.log10(Sxx + 1e-10)
            Sxx_norm = (Sxx_db - np.min(Sxx_db)) / (np.max(Sxx_db) - np.min(Sxx_db))
            
            segments.append({
                'frequencies': frequencies,
                'times': times,
                'spectrogram': Sxx_norm
            })
            timestamps.append(datetime.now())
            
        return segments, timestamps
