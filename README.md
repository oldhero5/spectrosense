# SpectroSense 📡

SpectroSense is an AI-powered RF signal analysis and classification tool that combines advanced signal processing with large language models to automatically identify and classify radio frequency signals from spectrograms.

![SpectroSense Logo](https://raw.githubusercontent.com/yourusername/spectrosense/main/docs/images/logo.png)

## 🚀 Features

- **Automated Signal Classification**: Leverages Claude AI to identify RF signals in spectrograms
- **Batch Processing**: Process multiple recordings efficiently
- **Detailed Analysis Reports**: Generate comprehensive JSON reports of identified signals
- **Visualization Tools**: Generate high-quality spectrograms
- **Extensible Architecture**: Easy to add new signal types and analysis methods

## 🛠️ Installation

```bash
pip install spectrosense
```

For development installation:
```bash
git clone https://github.com/yourusername/spectrosense.git
cd spectrosense
pip install -e ".[dev]"
```

## 🔧 Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your settings:
```bash
ANTHROPIC_API_KEY=your_api_key_here
```

## 📖 Quick Start

```python
from spectrosense import SignalProcessor, SpectrogramVisualizer, AIAnalyzer

# Initialize components
processor = SignalProcessor()
visualizer = SpectrogramVisualizer()
analyzer = AIAnalyzer(api_key="your-api-key")

# Process a recording
data = processor.load_signal("recording.wav")
segments, timestamps = processor.generate_spectrogram(data)

# Generate and analyze spectrograms
for segment, timestamp in zip(segments, timestamps):
    image_path = visualizer.save_spectrogram(segment, timestamp)
    analysis = analyzer.analyze_image(image_path)
    print(analysis)
```

## 📊 Example Output

```json
{
    "signal_types": ["wifi_halow"],
    "confidence": "high",
    "features": [
        "2MHz channel bandwidth",
        "Regular packet structure",
        "Center frequency: 919MHz"
    ],
    "notes": "IEEE 802.11ah signal with MCS0 modulation"
}
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] Real-time signal processing
- [ ] Web interface for analysis
- [ ] Support for more signal types
- [ ] GPU acceleration
- [ ] Batch processing optimization
- [ ] Integration with more LLMs
- [ ] Custom model training

## 📚 Documentation

(In Progress) Full documentation is available at [spectrosense.readthedocs.io](https://spectrosense.readthedocs.io)

## 🔍 Example Use Cases

- Amateur Radio Signal Analysis
- RF Environment Monitoring
- Protocol Identification
- Spectrum Management
- Research and Education

## ⚡ Performance

- Processes 1 hour of recordings in ~5 minutes
- Supports files up to 2GB
- 90%+ classification accuracy for common signals

## 🛟 Support

- 📫 For bugs and features, open an issue
- 💬 For questions, use [Discussions](https://github.com/oldhero5/spectrosense/discussions)

## 🙏 Acknowledgments

- Anthropic for Claude AI
- SciPy community
- Contributors and testers

---
Made with ❤️ by the SpectroSense Team