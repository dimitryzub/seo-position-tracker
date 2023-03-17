from seo_position_tracker import SeoPositionTracker
import json, argparse


def main():
    parser = argparse.ArgumentParser(
        prog='SerpApi SEO position tracker', 
        description='A simple Python CLI for SEO position tracking from Google, Baidu, Bing, DuckDuckGo, Yahoo, Yandex and Naver.', 
        epilog='Found a bug? Open issue: https://github.com/dimitryzub/seo-position-tracker/issues'
    )

    parser.add_argument('-q', '--query', metavar='', required=False, type=str, default='coffee', help='Search query. Default "%(default)s".')
    parser.add_argument('-tk', '--target-keywords', metavar='', required=False, type=str, default=['coffee'], nargs='+', help='Target keywords to track. Default "%(default)s".')
    parser.add_argument('-tw', '--target-websites', metavar='', required=False, type=str, default=['starbucks.com'], nargs='+', help='Target websites to track. Default "%(default)s".')
    parser.add_argument('-se', '--search-engine', metavar='', required=False, type=str, default=['google', 'baidu', 'bing', 'duckduckgo', 'yahoo', 'yandex', 'naver'], nargs='+', help='Choosing a search engine to track: "google", "baidu", "bing", "duckduckgo", "yahoo", "yandex", "naver". You can select multiple search engines. All search engines are selected by default.')
    parser.add_argument('-ak', '--api-key', metavar='', required=False, type=str, default='5868ece26d41221f5e19ae8b3e355d22db23df1712da675d144760fc30d57988', help='Your SerpApi API key: https://serpapi.com/manage-api-key. Default is a test API key to test CLI.')
    parser.add_argument('-hl','--lang', metavar='', required=False, type=str, default=None, help='Language of the search. Supported only for "google", "baidu", "yahoo" and "yandex" engines. Default "%(default)s". Find more by Googling: "SerpApi supported <engine> languages"')
    parser.add_argument('-gl','--country', metavar='', required=False, type=str, default=None, help='Country of the search. Supported only for "google", "bing" and "yahoo" engines. Default "%(default)s". Find more by Googling: "SerpApi supported <engine> countries"')
    parser.add_argument('-loc', '--location', metavar='', required=False, type=str, default=None, help='Location of the search. Supported only for "google", "bing", "duckduckgo" and "yandex" engines. Default "%(default)s". Find more by Googling: "SerpApi supported <engine> locations"')
    parser.add_argument('-d','--domain', metavar='', required=False, type=str, default=None, help='Search engine domain to use. Supported only for "google", "yahoo" and "yandex" engines. Default "%(default)s". Find more by Googling: "SerpApi supported <engine> domains"')
    parser.add_argument('-st','--save-to', metavar='', required=False, type=str, default='CSV', help='Saves the results in the current directory in the selected format (CSV, JSON, TXT). Default %(default)s.')
    args = parser.parse_args()
    
    tracker = SeoPositionTracker(
        query=args.query, 
        api_key=args.api_key, 
        keywords=args.target_keywords, 
        websites=args.target_websites,
        lang=args.lang, 
        country=args.country, 
        location=args.location,
        domain=args.domain
    )

    engine_methods = {
        'google': tracker.scrape_google,
        'baidu': tracker.scrape_baidu,
        'bing': tracker.scrape_bing,
        'duckduckgo': tracker.scrape_duckduckgo,
        'yahoo': tracker.scrape_yahoo,
        'yandex': tracker.scrape_yandex,
        'naver': tracker.scrape_naver
    }
    
    position_data = []

    for engine in args.search_engine:
        if engine in engine_methods:
            data = engine_methods[engine]()
            position_data.extend(data)
        else:
            print(f'"{engine}" is an unknown search engine.')

    if position_data:
        print(json.dumps(position_data, indent=2, ensure_ascii=False))
        print(f'Saving data in {args.save_to.upper()} format...')

        if args.save_to.upper() == 'CSV':
            tracker.save_to_csv(position_data)
        elif args.save_to.upper() == 'JSON':
            tracker.save_to_json(position_data)
        elif args.save_to.upper() == 'TXT':
            tracker.save_to_txt(position_data)

        print(f'Data successfully saved to {args.query.replace(" ", "_")}.{args.save_to.lower()} file.')
    else:
        print('Unfortunately, no matches were found.')


if __name__ == '__main__':
    main()