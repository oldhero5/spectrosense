# spectrosense/config.py
import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass
class SpectroSenseConfig:
    """Configuration class for SpectroSense"""
    # API Keys
    anthropic_api_key: str
    openai_api_key: str = None
    
    # Processing Configuration
    max_segment_duration: int
    sample_rate: int
    fft_size: int
    overlap: int
    
    # Output Configuration
    output_dir: Path
    save_intermediate: bool
    image_format: str
    report_format: str
    
    # Visualization Settings
    colormap: str
    figure_dpi: int
    figure_width: int
    figure_height: int
    
    # Model Configuration
    default_model: str
    confidence_threshold: float
    
    # Feature Flags
    enable_advanced_analysis: bool
    enable_batch_processing: bool
    enable_real_time_processing: bool
    enable_gpu_acceleration: bool
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables"""
        load_dotenv()
        
        return cls(
            # API Keys
            anthropic_api_key=os.getenv('ANTHROPIC_API_KEY'),
            openai_api_key=os.getenv('OPENAI_API_KEY'),
            
            # Processing Configuration
            max_segment_duration=int(os.getenv('MAX_SEGMENT_DURATION', 10)),
            sample_rate=int(os.getenv('SAMPLE_RATE', 44100)),
            fft_size=int(os.getenv('FFT_SIZE', 1024)),
            overlap=int(os.getenv('OVERLAP', 512)),
            
            # Output Configuration
            output_dir=Path(os.getenv('OUTPUT_DIR', './output')),
            save_intermediate=os.getenv('SAVE_INTERMEDIATE', 'true').lower() == 'true',
            image_format=os.getenv('IMAGE_FORMAT', 'png'),
            report_format=os.getenv('REPORT_FORMAT', 'json'),
            
            # Visualization Settings
            colormap=os.getenv('COLORMAP', 'viridis'),
            figure_dpi=int(os.getenv('FIGURE_DPI', 300)),
            figure_width=int(os.getenv('FIGURE_WIDTH', 10)),
            figure_height=int(os.getenv('FIGURE_HEIGHT', 6)),
            
            # Model Configuration
            default_model=os.getenv('DEFAULT_MODEL', 'claude-3-opus-20240229'),
            confidence_threshold=float(os.getenv('CONFIDENCE_THRESHOLD', 0.7)),
            
            # Feature Flags
            enable_advanced_analysis=os.getenv('ENABLE_ADVANCED_ANALYSIS', 'true').lower() == 'true',
            enable_batch_processing=os.getenv('ENABLE_BATCH_PROCESSING', 'true').lower() == 'true',
            enable_real_time_processing=os.getenv('ENABLE_REAL_TIME_PROCESSING', 'false').lower() == 'true',
            enable_gpu_acceleration=os.getenv('ENABLE_GPU_ACCELERATION', 'false').lower() == 'true'
        )

# Usage example:
if __name__ == "__main__":
    config = SpectroSenseConfig.from_env()
    print(f"Using model: {config.default_model}")
    print(f"Output directory: {config.output_dir}")