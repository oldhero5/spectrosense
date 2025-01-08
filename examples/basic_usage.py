from spectrosense import SpectrogramImageAnalyzer
from spectrosense.ai_integration import ModelType

# Use Llama model
analyzer_llama = SpectrogramImageAnalyzer(
    model_type=ModelType.LLAMA,
    vllm_server_url="http://localhost:8000"
)

# Use Claude model
analyzer_claude = SpectrogramImageAnalyzer(
    model_type=ModelType.CLAUDE,
    anthropic_api_key="your-api-key"
)

# Analyze with Llama
result_llama = analyzer_llama.analyze_spectrogram_image("spectrogram.png")
print("Llama analysis:", result_llama)

# Analyze with Claude
result_claude = analyzer_claude.analyze_spectrogram_image("spectrogram.png")
print("Claude analysis:", result_claude)