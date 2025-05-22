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
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import pandas as pd
import os
import json
import uuid
import datetime
import re
import urllib.parse
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
import plotly.utils
# Assuming main.py is in the same directory
from main import run as run_crawler

# Import functions directly from crawler and analyzer
from crawler import crawl_site
from analyzer import detect_language, analyze_sentiment, find_suspicious_phrases, analyze_content_with_gemini
from utils import get_apparent_ip_through_tor

app = Flask(__name__)
app.secret_key = "darkwebcrawler_secret_key"  # For session management

# Constants
DATA_DIR = "data"
HISTORY_FILE = os.path.join(DATA_DIR, "analysis_history.json")
BATCH_DIR = os.path.join(DATA_DIR, "batch_jobs")

# Ensure data directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BATCH_DIR, exist_ok=True)

# Load analysis history or create if not exists
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return {"analyses": []}
    else:
        return {"analyses": []}

# Save analysis to history
def save_to_history(analysis_data):
    history = load_history()
    
    # Add timestamp and unique ID
    analysis_data['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    analysis_data['id'] = str(uuid.uuid4())
    
    # Add risk level and category if available from AI analysis
    if 'ai_analysis' in analysis_data:
        analysis_text = analysis_data['ai_analysis']
        
        # Extract risk level
        risk_match = re.search(r"RISK_LEVEL:\s*(\d+)", analysis_text)
        if risk_match:
            analysis_data['risk_level'] = int(risk_match.group(1))
        else:
            analysis_data['risk_level'] = 0
            
        # Try to extract content type/category
        content_match = re.search(r"CONTENT_TYPE:\s*([^\n]+)", analysis_text)
        if content_match:
            analysis_data['category'] = content_match.group(1).strip()
        else:
            analysis_data['category'] = "Unknown"
    
    # Append to history
    history["analyses"].append(analysis_data)
    
    # Only keep the latest 100 analyses
    if len(history["analyses"]) > 100:
        history["analyses"] = history["analyses"][-100:]
    
    # Save updated history
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)
    
    return analysis_data['id']

# Process a single URL
def process_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        text = crawl_site(url)
        lang = detect_language(text)
        sentiment = analyze_sentiment(text)
        suspicious = find_suspicious_phrases(text)
        text_snippet = (text[:500] + '...') if len(text) > 500 else text
        
        # Get AI analysis of the content
        ai_result = analyze_content_with_gemini(text)
        if "error" in ai_result:
            ai_analysis = f"AI Analysis Error: {ai_result['error']}"
        else:
            ai_analysis = ai_result['ai_analysis']

        result = {
            'url': url,
            'language': lang,
            'sentiment': sentiment,
            'suspicious_keywords': suspicious if suspicious else [],
            'raw_text_snippet': text_snippet,
            'ai_analysis': ai_analysis,
            'full_text': text,
            'success': True,
            'processed_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save analysis to history
        analysis_id = save_to_history(result)
        result['id'] = analysis_id
        
        return result
    except Exception as e:
        error_detail = str(e)
        print(f"Error processing URL {url}: {error_detail}")
        return {
            'url': url,
            'error': error_detail,
            'success': False,
            'processed_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# Generate statistics from history
def generate_stats():
    history = load_history()
    if not history["analyses"]:
        return None
    
    stats = {
        "total_sites": len(history["analyses"]),
        "languages": Counter(),
        "categories": Counter(),
        "risk_levels": {
            "high": 0,
            "medium": 0,
            "low": 0
        },
        "avg_sentiment": 0,
        "common_keywords": Counter(),
        "recent_sites": []
    }
    
    sentiment_sum = 0
    sentiment_count = 0
    
    for analysis in history["analyses"]:
        # Count languages
        if "language" in analysis and analysis["language"]:
            stats["languages"][analysis["language"]] += 1
            
        # Count categories
        if "category" in analysis:
            stats["categories"][analysis["category"]] += 1
            
        # Count risk levels
        if "risk_level" in analysis:
            if analysis["risk_level"] >= 7:
                stats["risk_levels"]["high"] += 1
            elif analysis["risk_level"] >= 4:
                stats["risk_levels"]["medium"] += 1
            else:
                stats["risk_levels"]["low"] += 1
                
        # Calculate average sentiment
        if "sentiment" in analysis and analysis["sentiment"] is not None:
            sentiment_sum += float(analysis["sentiment"])
            sentiment_count += 1
            
        # Collect common suspicious keywords
        if "suspicious_keywords" in analysis and analysis["suspicious_keywords"]:
            if isinstance(analysis["suspicious_keywords"], list):
                for kw in analysis["suspicious_keywords"]:
                    stats["common_keywords"][kw] += 1
            elif isinstance(analysis["suspicious_keywords"], str):
                keywords = [k.strip() for k in analysis["suspicious_keywords"].split(",")]
                for kw in keywords:
                    if kw and kw.lower() != "none":
                        stats["common_keywords"][kw] += 1
    
    # Calculate average sentiment
    if sentiment_count > 0:
        stats["avg_sentiment"] = round(sentiment_sum / sentiment_count, 2)
    
    # Get most recent sites
    sorted_analyses = sorted(history["analyses"], 
                             key=lambda x: x.get("timestamp", ""), 
                             reverse=True)
    stats["recent_sites"] = sorted_analyses[:10]
    
    return stats

# Create visualization charts
def create_charts():
    stats = generate_stats()
    if not stats or stats["total_sites"] == 0:
        return None
        
    charts = {}
    
    # Risk Level Pie Chart
    risk_labels = ["High Risk", "Medium Risk", "Low Risk"]
    risk_values = [stats["risk_levels"]["high"], 
                   stats["risk_levels"]["medium"], 
                   stats["risk_levels"]["low"]]
    
    risk_fig = go.Figure(data=[go.Pie(
        labels=risk_labels,
        values=risk_values,
        hole=.3,
        marker_colors=['#ff4d4d', '#ffa64d', '#6bc25d']
    )])
    risk_fig.update_layout(
        title_text="Risk Level Distribution",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        margin=dict(l=20, r=20, t=40, b=20),
        height=300
    )
    charts["risk_chart"] = json.loads(plotly.utils.PlotlyJSONEncoder().encode(risk_fig))
    
    # Language Bar Chart
    if stats["languages"]:
        top_langs = stats["languages"].most_common(5)
        lang_labels = [lang for lang, count in top_langs]
        lang_values = [count for lang, count in top_langs]
        
        lang_fig = go.Figure(data=[go.Bar(
            x=lang_labels, 
            y=lang_values,
            marker_color='#9966cc'
        )])
        lang_fig.update_layout(
            title_text="Top Languages",
            xaxis_title="Language",
            yaxis_title="Count",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e0e0'),
            margin=dict(l=20, r=20, t=40, b=40),
            height=300
        )
        charts["language_chart"] = json.loads(plotly.utils.PlotlyJSONEncoder().encode(lang_fig))
    
    # Category Bar Chart
    if stats["categories"]:
        top_cats = stats["categories"].most_common(5)
        cat_labels = [cat for cat, count in top_cats]
        cat_values = [count for cat, count in top_cats]
        
        cat_fig = go.Figure(data=[go.Bar(
            x=cat_labels, 
            y=cat_values,
            marker_color='#56347c'
        )])
        cat_fig.update_layout(
            title_text="Top Content Categories",
            xaxis_title="Category",
            yaxis_title="Count",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e0e0'),
            margin=dict(l=20, r=20, t=40, b=80),
            height=300
        )
        cat_fig.update_xaxes(tickangle=-45)
        charts["category_chart"] = json.loads(plotly.utils.PlotlyJSONEncoder().encode(cat_fig))
    
    return charts

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    data_for_template = []
    error_message = None
    success_message = None
    tor_ip_address = None
    charts = None
    columns = ['url', 'language', 'sentiment', 'suspicious_keywords', 'raw_text_snippet', 'ai_analysis']

    # Generate stats and charts for dashboard
    stats = generate_stats()
    if stats and stats["total_sites"] > 0:
        charts = create_charts()

    if request.method == 'POST':
        # Get Tor IP
        print("Flask app: Attempting to get IP via Tor...")
        tor_ip_address = get_apparent_ip_through_tor()
        print(f"Flask app: Apparent IP via Tor session: {tor_ip_address}")

        # Process URL submission
        if 'onion_url' in request.form and request.form.get('onion_url'):
            onion_url = request.form.get('onion_url')
            print(f"Flask app: Received URL for processing: {onion_url}")
            
            result = process_url(onion_url)
            
            if result['success']:
                print(f"Flask app: Successfully processed URL: {onion_url}")
                data_for_template.append(result)
            else:
                error_detail = result['error']
                if "SOCKSHTTPConnectionPool" in error_detail or "SOCKSConnection" in error_detail:
                    error_message = f"Failed to connect to {onion_url} via Tor. Ensure Tor is running and the URL is correct/accessible. Details: {error_detail}"
                elif "No SOCKS proxy specified" in error_detail:
                    error_message = f"Tor proxy not configured for requests. Details: {error_detail}"
                else:
                    error_message = f"Error processing {onion_url}: {error_detail}"
        
        # Process batch URLs submission
        elif 'batch_urls' in request.form and request.form.get('batch_urls'):
            batch_urls = request.form.get('batch_urls').strip().split('\n')
            batch_urls = [url.strip() for url in batch_urls if url.strip()]
            
            if batch_urls:
                # Create batch job
                batch_id = str(uuid.uuid4())
                batch_file = os.path.join(BATCH_DIR, f"{batch_id}.json")
                
                batch_data = {
                    "id": batch_id,
                    "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "status": "pending",
                    "total_urls": len(batch_urls),
                    "processed_urls": 0,
                    "urls": batch_urls,
                    "results": []
                }
                
                with open(batch_file, 'w') as f:
                    json.dump(batch_data, f)
                
                # Redirect to batch processing page
                return redirect(url_for('batch_process', batch_id=batch_id))
    
    return render_template('index.html', 
                          data=data_for_template, 
                          columns=columns, 
                          error_message=error_message,
                          success_message=success_message,
                          tor_ip_address=tor_ip_address,
                          stats=stats,
                          charts=charts)

@app.route('/dashboard')
def dashboard():
    stats = generate_stats()
    charts = create_charts()
    return render_template('dashboard.html', stats=stats, charts=charts)

@app.route('/history')
def history():
    history_data = load_history()
    return render_template('history.html', history=history_data)

@app.route('/analysis/<analysis_id>')
def view_analysis(analysis_id):
    history_data = load_history()
    analysis = None
    
    for item in history_data["analyses"]:
        if item.get("id") == analysis_id:
            analysis = item
            break
            
    if not analysis:
        return redirect(url_for('history'))
        
    return render_template('analysis_details.html', analysis=analysis)

@app.route('/batch')
def batch():
    # Get all batch jobs
    batch_jobs = []
    for filename in os.listdir(BATCH_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(BATCH_DIR, filename), 'r') as f:
                batch_jobs.append(json.load(f))
                
    # Sort by creation date (newest first)
    batch_jobs = sorted(batch_jobs, key=lambda x: x.get("created", ""), reverse=True)
    
    return render_template('batch.html', batch_jobs=batch_jobs)

@app.route('/batch/<batch_id>', methods=['GET', 'POST'])
def batch_process(batch_id):
    batch_file = os.path.join(BATCH_DIR, f"{batch_id}.json")
    
    if not os.path.exists(batch_file):
        return redirect(url_for('batch'))
        
    with open(batch_file, 'r') as f:
        batch_data = json.load(f)
    
    # If POST method, process the next URL
    if request.method == 'POST' and batch_data["status"] != "completed":
        # Find next unprocessed URL
        processed_urls = len(batch_data["results"])
        if processed_urls < len(batch_data["urls"]):
            url = batch_data["urls"][processed_urls]
            
            # Process URL
            result = process_url(url)
            
            # Add to results
            batch_data["results"].append(result)
            batch_data["processed_urls"] = len(batch_data["results"])
            
            # Check if batch is complete
            if batch_data["processed_urls"] >= batch_data["total_urls"]:
                batch_data["status"] = "completed"
                batch_data["completed"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save updated batch data
            with open(batch_file, 'w') as f:
                json.dump(batch_data, f)
    
    return render_template('batch_process.html', batch=batch_data)

@app.route('/api/stats')
def api_stats():
    stats = generate_stats()
    return jsonify(stats)

@app.route('/api/process', methods=['POST'])
def api_process():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
        
    data = request.get_json()
    
    if 'url' not in data:
        return jsonify({"error": "URL is required"}), 400
        
    result = process_url(data['url'])
    return jsonify(result)

@app.route('/report/<analysis_id>')
def generate_report(analysis_id):
    history_data = load_history()
    analysis = None
    
    for item in history_data["analyses"]:
        if item.get("id") == analysis_id:
            analysis = item
            break
            
    if not analysis:
        return redirect(url_for('history'))
        
    return render_template('report.html', analysis=analysis)

@app.route('/vulnerability')
def vulnerability():
    """
    Route for the vulnerability assessment tab
    """
    # Get latest analyses with risk levels
    history = load_history()
    
    # Sort by timestamp (newest first) and get those with risk_level
    recent_assessments = [a for a in history["analyses"] if "risk_level" in a]
    recent_assessments = sorted(recent_assessments, key=lambda x: x.get("timestamp", ""), reverse=True)[:8]
    
    return render_template('vulnerability.html', recent_assessments=recent_assessments)

if __name__ == '__main__':
    # The 'templates' directory should be at the same level as app.py
    # Flask automatically looks for templates in a 'templates' folder.
    print("Flask app: Starting server on http://127.0.0.1:5000")
    print("Flask app: Enter an .onion URL in the browser to start analysis.")
    print("Flask app: Ensure Tor is running and configured correctly for the crawler to work (SOCKS5h on 127.0.0.1:9150).")
    app.run(debug=True, host='0.0.0.0', port=5000) 
from bs4 import BeautifulSoup
from utils import get_tor_session

def crawl_site(url):
    session = get_tor_session()
    response = session.get(url, timeout=40)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text 
from crawler import crawl_site
from analyzer import detect_language, analyze_sentiment, find_suspicious_phrases
import pandas as pd

def run():
    onion_urls = ['http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion/']  # Replace with actual .onion sites
    data = []

    for url in onion_urls:
        try:
            text = crawl_site(url)
            lang = detect_language(text)
            sentiment = analyze_sentiment(text)
            suspicious = find_suspicious_phrases(text)

            data.append({
                'url': url,
                'language': lang,
                'sentiment': sentiment,
                'suspicious_keywords': suspicious
            })

        except Exception as e:
            print(f"Error on {url}: {e}")

    df = pd.DataFrame(data)
    df.to_csv("results.csv", index=False)

if __name__ == "__main__":
    run() 
