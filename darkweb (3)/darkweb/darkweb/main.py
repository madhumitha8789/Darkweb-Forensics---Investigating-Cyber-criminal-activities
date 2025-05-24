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