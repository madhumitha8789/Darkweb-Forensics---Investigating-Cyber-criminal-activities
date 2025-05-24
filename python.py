from langdetect import detect
from textblob import TextBlob
import google.generativeai as genai

suspicious_keywords = ['buy passport', 'credit card dump', 'drugs', 'exploit kit']

def detect_language(text):
    return detect(text)

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # -1 (negative) to +1 (positive)

def find_suspicious_phrases(text):
    return [kw for kw in suspicious_keywords if kw in text.lower()]

# API key for Gemini
GEMINI_API_KEY = "AIzaSyCw1dKWQc6Ri_Dj9m1FAK7oIIt-847mbh4"

def analyze_content_with_gemini(text, max_length=1000):
    """
    Uses Google's Gemini to analyze content for:
    - Content type and summary
    - Potentially illegal or harmful content
    - Risk assessment
    - Vulnerability predictions
    """
    if not GEMINI_API_KEY:
        return {
            "error": "Gemini API key not configured. Please replace the placeholder in analyzer.py with a valid API key."
        }
    
    try:
        # Configure the Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Use Gemini Flash model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Truncate text if it's too long
        text_to_analyze = text[:max_length] + "..." if len(text) > max_length else text
        
        # Create the prompt for content analysis with enhanced vulnerability assessment
        prompt = f"""
        Analyze the following content from a dark web site. Provide a detailed analysis with these sections:
        1. CONTENT_TYPE: Briefly describe what kind of content this appears to be
        2. RISK_LEVEL: Rate the content risk on a scale from 0-10 where 0 is benign and 10 is highly dangerous/illegal
        3. CONCERNS: List specific concerns about illegal content, scams, or harmful material
        4. VULNERABILITIES: Identify any technical vulnerabilities or security issues with the site content
        5. POTENTIAL_FUTURE_RISKS: Predict what kinds of vulnerabilities or risks might develop in the future based on this content
        6. SUMMARY: One sentence summary of what this site appears to be and its risk profile
        
        Content to analyze:
        {text_to_analyze}
        """
        
        # Generate the response
        response = model.generate_content(prompt)
        
        # Return the Gemini analysis
        return {
            "ai_analysis": response.text,
            "processed_chars": len(text_to_analyze),
            "total_chars": len(text)
        }
        
    except Exception as e:
        return {
            "error": f"Error using Gemini API: {str(e)}"
        } 
