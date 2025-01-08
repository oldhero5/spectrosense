# SpectroSense 📡

SpectroSense is an AI-powered RF signal analysis and classification tool that combines advanced signal processing with large language models to automatically identify and classify radio frequency signals from spectrograms.

![SpectroSense Logo](https://raw.githubusercontent.com/oldhero5/spectrosense/main/docs/images/logo.png)

## 🚀 Features

- **Multiple AI Models**: Support for both Claude and Meta's Llama Vision model
- **Automated Signal Classification**: Leverages AI to identify RF signals in spectrograms
- **Direct Image Analysis**: Process existing spectrogram images in various formats
- **Batch Processing**: Process multiple recordings or images efficiently
- **Detailed Analysis Reports**: Generate comprehensive JSON reports of identified signals
- **Visualization Tools**: Generate high-quality spectrograms
- **Extensible Architecture**: Easy to add new signal types and analysis methods

## 🛠️ Installation

```bash
pip install spectrosense
```

For development installation:
```bash
git clone https://github.com/oldhero5/spectrosense.git
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
# For Claude
AI_MODEL_TYPE=claude
ANTHROPIC_API_KEY=your_api_key_here

# For Llama
AI_MODEL_TYPE=llama
VLLM_SERVER_URL=http://localhost:8000
```

## 📖 Quick Start

```python
from spectrosense import SpectrogramImageAnalyzer
from spectrosense.ai_integration import ModelType

# Using Claude
analyzer = SpectrogramImageAnalyzer(
    model_type=ModelType.CLAUDE,
    anthropic_api_key="your-api-key"
)

# Using Llama
analyzer = SpectrogramImageAnalyzer(
    model_type=ModelType.LLAMA,
    vllm_server_url="http://localhost:8000"
)

# Analyze a single image
result = analyzer.analyze_spectrogram_image("spectrogram.png")
print(result)

# Batch process a directory
results = analyzer.batch_analyze_images("spectrograms/")
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

## 🚀 Model Setup

### Claude Setup
1. Obtain an API key from Anthropic
2. Set the key in your environment

### Llama Setup
1. Install vLLM:
```bash
pip install vllm
```

2. Start the vLLM server:
```bash
python -m vllm.entrypoints.api_server \
    --model meta-llama/Llama-3.2-11B-Vision-Instruct \
    --port 8000
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [X] Support for more AI models
- [ ] Real-time signal processing
- [ ] Web interface for analysis
- [ ] GPU acceleration
- [ ] Batch processing optimization
- [ ] Custom model training

## 📚 Documentation

Full documentation is available at [spectrosense.readthedocs.io](https://spectrosense.readthedocs.io)

---
Made with ❤️ by the SpectroSense Team