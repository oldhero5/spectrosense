from spectrosense import SpectrogramImageAnalyzer

def main():
    # Initialize analyzer with your API key
    analyzer = SpectrogramImageAnalyzer(api_key="your_api_key_here")
    
    # Analyze a single image
    result = analyzer.analyze_spectrogram_image("path/to/your/spectrogram.png")
    print("Single image analysis:", result)
    
    # Or analyze all images in a directory
    batch_results = analyzer.batch_analyze_images("path/to/spectrogram/directory")
    print("Batch analysis complete:", batch_results["total_images"], "images processed")

if __name__ == "__main__":
    main()