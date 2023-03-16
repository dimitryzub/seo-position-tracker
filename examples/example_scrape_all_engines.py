from seo_position_tracker.seo_position_tracker import SeoPositionTracker
import json

tracker = SeoPositionTracker(
    query='coffee', 
    api_key='<your_serpapi_api_key>', 
    keywords=['coffee', 'starbucks'], 
    websites=['starbucks.com']
)

position_data = []

google_results = tracker.scrape_google(lang='en', country='us', location='United States', domain='google.com')
position_data.extend(google_results)

baidu_results = tracker.scrape_baidu(lang='1')
position_data.extend(baidu_results)

bing_results = tracker.scrape_bing(country='us', location='United States')
position_data.extend(bing_results)

duckduckgo_results = tracker.scrape_duckduckgo(location='us-en')
position_data.extend(duckduckgo_results)

yahoo_results = tracker.scrape_yahoo(lang='lang_en', country='us', domain='uk')
position_data.extend(yahoo_results)

yandex_results = tracker.scrape_yandex(lang='en', domain='yandex.com')
position_data.extend(yandex_results)

naver_results = tracker.scrape_naver()
position_data.extend(naver_results)

print(json.dumps(position_data, indent=2, ensure_ascii=False))