from seo_position_tracker.seo_position_tracker import SeoPositionTracker
import json

tracker = SeoPositionTracker(
    query='coffee', 
    api_key='5868ece26d41221f5e19ae8b3e355d22db23df1712da675d144760fc30d57988', 
    keywords=['coffee', 'starbucks'], 
    websites=['starbucks.com'],
    lang='en', 
    country='us', 
    location='United States',
    domain='google.com'
)

google_results = tracker.scrape_google()

print(json.dumps(google_results, indent=2, ensure_ascii=False))