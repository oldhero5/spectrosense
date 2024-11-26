from anthropic import Anthropic
import json
import base64

class AIAnalyzer:
    """Handles AI-based signal analysis"""
    
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)
        
    def analyze_image(self, image_path):
        """Analyze spectrogram using Claude"""
        with open(image_path, 'rb') as img_file:
            image_data = base64.b64encode(img_file.read()).decode('utf-8')
            
        prompt = """Analyze this spectrogram and identify the type of radio signals present.
        Focus on:
        1. Signal patterns and characteristics
        2. Frequency ranges and bandwidths
        3. Modulation characteristics if visible
        4. Timing patterns
        5. Any distinctive features that indicate specific protocols or services
        
        Provide your analysis in JSON format with the following structure:
        {
            "signal_types": ["list of identified signals"],
            "confidence": "high/medium/low",
            "features": ["key features observed"],
            "notes": "additional observations"
        }
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
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
            return {
                "signal_types": ["unknown"],
                "confidence": "low",
                "features": [],
                "notes": f"Analysis failed: {str(e)}"
            }