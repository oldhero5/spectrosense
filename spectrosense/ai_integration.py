# spectrosense/ai_integration.py
from anthropic import Anthropic
import json
import base64
import requests
from typing import Optional, Dict, Any, Literal
from enum import Enum
import logging

class ModelType(Enum):
    CLAUDE = "claude"
    LLAMA = "llama"

class AIAnalyzer:
    """Handles AI-based signal analysis with support for multiple models"""
    
    def __init__(self, 
                 model_type: ModelType = ModelType.CLAUDE,
                 anthropic_api_key: Optional[str] = None,
                 vllm_server_url: Optional[str] = "http://localhost:8000",
                 max_tokens: int = 8000):
        """
        Initialize the AI analyzer
        
        Args:
            model_type: Which model to use (claude or llama)
            anthropic_api_key: API key for Claude (required if using Claude)
            vllm_server_url: URL of vLLM server (required if using Llama)
            max_tokens: Maximum tokens in response
        """
        self.model_type = model_type
        self.max_tokens = max_tokens
        
        if model_type == ModelType.CLAUDE:
            if not anthropic_api_key:
                raise ValueError("Anthropic API key required for Claude model")
            self.client = Anthropic(api_key=anthropic_api_key)
        else:
            if not vllm_server_url:
                raise ValueError("vLLM server URL required for Llama model")
            self.vllm_url = vllm_server_url.rstrip('/')
            
        self.logger = logging.getLogger(__name__)

    def _prepare_prompt(self, image_data: str) -> str:
        """Prepare prompt based on model type"""
        base_prompt = """Analyze this spectrogram and identify the type of radio signals present.
        Focus on:
        1. Signal patterns and characteristics
        2. Frequency ranges and bandwidths
        3. Modulation characteristics if visible
        4. Timing patterns
        5. Any distinctive features that indicate specific protocols or services
        
        Please output your analysis in JSON format with the following structure:
        {
            "signal_types": ["list of identified signals"],
            "confidence": "high/medium/low",
            "features": ["key features observed"],
            "notes": "additional observations"
        }
        """
        
        if self.model_type == ModelType.LLAMA:
            # Llama specific prompt formatting
            return f"<image>{image_data}</image>\n{base_prompt}"
        else:
            # Claude uses default prompt
            return base_prompt

    def _call_vllm_server(self, prompt: str) -> Dict[str, Any]:
        """Make request to vLLM server running Llama model"""
        try:
            response = requests.post(
                f"{self.vllm_url}/v1/completions",
                json={
                    "model": "meta-llama/Llama-3.2-11B-Vision-Instruct",
                    "prompt": prompt,
                    "max_tokens": self.max_tokens,
                    "temperature": 0.1,  # Low temperature for more focused analysis
                    "stop": ["}"],  # Stop after JSON completion
                }
            )
            response.raise_for_status()
            
            # Extract JSON from response
            result = response.json()
            text_response = result['choices'][0]['text']
            
            # Ensure we have complete JSON
            if not text_response.strip().endswith('}'):
                text_response += '}'
                
            return json.loads(text_response)
            
        except Exception as e:
            self.logger.error(f"Error calling vLLM server: {str(e)}")
            return {
                "signal_types": ["unknown"],
                "confidence": "low",
                "features": [],
                "notes": f"Analysis failed: {str(e)}"
            }

    def analyze_image(self, image_path: str) -> Dict[str, Any]:
        """Analyze spectrogram using selected AI model"""
        try:
            # Read and encode image
            with open(image_path, 'rb') as img_file:
                image_data = base64.b64encode(img_file.read()).decode('utf-8')
                
            # Prepare prompt
            prompt = self._prepare_prompt(image_data)
            
            if self.model_type == ModelType.LLAMA:
                return self._call_vllm_server(prompt)
            else:
                # Use Claude
                response = self.client.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=self.max_tokens,
                    messages=[{
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image", "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_data
                            }}
                        ]
                    }]
                )
                
                return json.loads(response.content[0].text)
                
        except Exception as e:
            self.logger.error(f"Analysis failed: {str(e)}")
            return {
                "signal_types": ["unknown"],
                "confidence": "low",
                "features": [],
                "notes": f"Analysis failed: {str(e)}"
            }