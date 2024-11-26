import matplotlib.pyplot as plt
import os

class SpectrogramVisualizer:
    """Handles visualization and image generation"""
    
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def save_spectrogram(self, spectrogram_data, timestamp, filename=None):
        """Save spectrogram as image"""
        plt.figure(figsize=(10, 6))
        plt.imshow(
            spectrogram_data['spectrogram'],
            aspect='auto',
            extent=[
                spectrogram_data['times'][0],
                spectrogram_data['times'][-1],
                spectrogram_data['frequencies'][0],
                spectrogram_data['frequencies'][-1]
            ],
            cmap='viridis'
        )
        plt.colorbar(label='Intensity (dB)')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        
        if filename is None:
            filename = f"spectrogram_{timestamp.strftime('%Y%m%d_%H%M%S')}.png"
            
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath)
        plt.close()
        
        return filepath
