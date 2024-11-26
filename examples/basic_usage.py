from spectrosense import SignalProcessor, SpectrogramVisualizer, AIAnalyzer, SignalAnalyzer

def analyze_recording(file_path, api_key):
    # Initialize components
    processor = SignalProcessor()
    visualizer = SpectrogramVisualizer("output")
    ai_analyzer = AIAnalyzer(api_key)
    analyzer = SignalAnalyzer()
    
    # Process signal
    data = processor.load_signal(file_path)
    segments, timestamps = processor.generate_spectrogram(data)
    
    # Generate and analyze images
    analyses = []
    for segment, timestamp in zip(segments, timestamps):
        # Save spectrogram
        image_path = visualizer.save_spectrogram(segment, timestamp)
        
        # Analyze with AI
        analysis = ai_analyzer.analyze_image(image_path)
        
        analyses.append({
            "timestamp": timestamp.isoformat(),
            "analysis": analysis
        })
    
    # Generate report
    report = analyzer.generate_report(analyses, file_path, "output/analysis_report.json")
    return report

if __name__ == "__main__":
    report = analyze_recording("recording.wav", "your-api-key-here")
    print(json.dumps(report, indent=2))