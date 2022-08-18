import argparse
import pandas as pd
from serpapi import GoogleSearch
from typing import Optional
from typing import Sequence


# TODO: support ad results. Organic AND ads.
# TODO: support for multiple engines: bing, baidu, yahoo, duckduckgo, naver, yandex
# TODO: support multiple target keywords (keywords with spaces) and multiple target websites.

def main(argv: Optional[Sequence[str]] = None) -> int:
    # engines = ['google', 'bing', 'baidu', 'yahoo', 'duckduckgo', 'naver', 'yandex']  # multiple --search-engine, will be added in the next updates.
    parser = argparse.ArgumentParser(description='SerpApi SEO position tracker.')
    # usage: --api-key 213128sad or --api-key=213128sad or --api-key="213128sad"
    parser.add_argument('--api-key', required=True, type=str, help='your SerpApi API key. For more: https://serpapi.com/manage-api-key')
    parser.add_argument('-se', type=str, default='google', help=f'search engine. Currently only one can be passed. Default: Google')
    parser.add_argument('-po', action='store_true', help='returns website position only.')

    # usage: python <script.py> -q="<your are breathtaking>". Same with --search_query
    parser.add_argument(
        '-q',
        type=str,
        default='coffee',
        help='search query. Default: "Coffee"',
    )
    parser.add_argument(
        '-tk',
        type=str,
        # nargs='+', # will be added in the next update
        default='coffee',
        help='target keyword to track. Default: "coffee". Currently only one can be passed.',
    )
    parser.add_argument(
        '-tw',
        type=str,
        # nargs='+', # will be added in the next update
        default='starbucks.com',
        help='target website to track. Default: "starbucks.com". Currently only one can be passed.',
    )
    parser.add_argument('-l', type=str, default='en', help='language of the search. Default: "en" - English. For more: https://serpapi.com/google-languages')
    parser.add_argument('-c', type=str, default='us', help='country of the search. Default: "us" - United States. For more: https://serpapi.com/google-countries')
    parser.add_argument('-loc', type=str, default='United States', help='location of the search. Default: "United States". For more: https://serpapi.com/locations-api')
    parser.add_argument('--to-csv', action='store_true', help='saves results in the current directory to csv.')
    parser.add_argument('--to-json', action='store_true', help='saves results in the current directory to json.')

    args = parser.parse_args(argv)

    params = {
        'api_key': args.api_key,
        'engine': args.se,
        'q': args.q,
        'hl': args.l,
        'gl': args.c,
        'location': args.loc,
        'num': 100                  # 100 results from Google search
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    position_data = []

    for result in results['organic_results']:
        if args.tk.lower() in result['title'].lower() and args.tw in result['link'] and not args.po:
            position_data.append(
                {
                    'position': result['position'],
                    'country_of_the_search': params['gl'],
                    'title': result['title'],
                    'link': result['link'],
                }
            )

        # [1] or [1, 5, 20] - 1st, 5th and 20th positions
        if args.tk.lower() in result['title'].lower() and args.tw in result['link'] and args.po:
            position_data.append(result['position'])

    if args.to_json:
        # chnage file output to the one you understand
        pd.DataFrame(main()).to_json(f'results_for_query_{args.search_query.replace(" ", "_")}.json', orient='records')
        print(f'Saved to "results_for_query_{args.search_query.replace(" ", "_")}.json"')

    if args.to_csv:
        # chnage file output to the one you understand
        pd.DataFrame(main()).to_csv(f'results_for_query_{args.search_query.replace(" ", "_")}.csv', index=False, encoding='utf-8')
        print(f'Saved to "results_for_query_{args.search_query.replace(" ", "_")}.csv"')

    return position_data


if __name__ == '__main__':
    exit(main())
