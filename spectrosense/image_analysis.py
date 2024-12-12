# spectrosense/image_analysis.py
import os
from PIL import Image
import numpy as np
from datetime import datetime
import json
from .ai_integration import AIAnalyzer

class SpectrogramImageAnalyzer:
    """Handles direct analysis of spectrogram images"""
    
    def __init__(self, api_key, output_dir="output"):
        """Initialize the image analyzer"""
        self.ai_analyzer = AIAnalyzer(api_key)
        self.output_dir = output_dir
        self.supported_formats = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp'}
        os.makedirs(output_dir, exist_ok=True)
        
    def validate_image(self, image_path):
        """Validate if the file is a supported image format"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
            
        file_ext = os.path.splitext(image_path)[1].lower()
        if file_ext not in self.supported_formats:
            raise ValueError(f"Unsupported image format. Supported formats: {self.supported_formats}")
            
        try:
            with Image.open(image_path) as img:
                img.verify()
        except Exception as e:
            raise ValueError(f"Invalid or corrupted image file: {str(e)}")
            
        return True
        
    def preprocess_image(self, image_path):
        """Preprocess the image if needed"""
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if too large (optional)
            max_size = (1920, 1080)
            if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save preprocessed image
            output_path = os.path.join(self.output_dir, 
                                     f"preprocessed_{os.path.basename(image_path)}")
            img.save(output_path)
            
        return output_path
        
    def analyze_spectrogram_image(self, image_path):
        """Analyze a single spectrogram image"""
        # Validate image
        self.validate_image(image_path)
        
        # Preprocess image
        processed_path = self.preprocess_image(image_path)
        
        # Perform AI analysis
        analysis = self.ai_analyzer.analyze_image(processed_path)
        
        # Add metadata
        result = {
            "timestamp": datetime.now().isoformat(),
            "image_path": image_path,
            "analysis": analysis
        }
        
        # Save report
        report_path = os.path.join(self.output_dir, 
                                 f"analysis_{os.path.splitext(os.path.basename(image_path))[0]}.json")
        with open(report_path, 'w') as f:
            json.dump(result, f, indent=2)
            
        return result
        
    def batch_analyze_images(self, image_directory):
        """Analyze all supported images in a directory"""
        results = []
        
        # Find all supported images in directory
        for filename in os.listdir(image_directory):
            file_path = os.path.join(image_directory, filename)
            file_ext = os.path.splitext(filename)[1].lower()
            
            if file_ext in self.supported_formats:
                try:
                    result = self.analyze_spectrogram_image(file_path)
                    results.append(result)
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
                    
        # Save batch report
        batch_report = {
            "batch_timestamp": datetime.now().isoformat(),
            "directory": image_directory,
            "total_images": len(results),
            "results": results
        }
        
        batch_report_path = os.path.join(self.output_dir, 
                                       f"batch_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(batch_report_path, 'w') as f:
            json.dump(batch_report, f, indent=2)
            
        return batch_report