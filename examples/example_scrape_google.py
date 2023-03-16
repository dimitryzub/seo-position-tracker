from seo_position_tracker.seo_position_tracker import SeoPositionTracker
import json

tracker = SeoPositionTracker(
    query='coffee', 
    api_key='<your_serpapi_api_key>', 
    keywords=['coffee', 'starbucks'], 
    websites=['starbucks.com'],
    lang='en', 
    country='us', 
    location='United States',
    domain='google.com'
)

google_results = tracker.scrape_google()

print(json.dumps(google_results, indent=2, ensure_ascii=False))