# TODO: support ad results. Organic AND ads.

import pandas as pd
import argparse, json
from serpapi import GoogleSearch

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

args = parser.parse_args()

# TODO: support for multiple engines: bing, baidu, yahoo, duckduckgo, naver, yandex
# TODO: support multiple target keywords (keywords with spaces) and multiple target websites.

def main():
    for keyword, website in zip(args.tk, args.tw):
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
            if keyword.lower() in result['title'].lower() and website in result['link'] and not args.po:
                position_data.append(
                    {
                        'position': result['position'],
                        'country_of_the_search': params['gl'],
                        'title': result['title'],
                        'link': result['link'],
                    }
                )

            if keyword.lower() in result['title'].lower() and website in result['link'] and args.po:
                position_data.append(result['position'])

        return position_data


if __name__ == '__main__':
    # [1] or [1, 5, 20] - 1st, 5th and 20th positions
    if args.po:
        print(main())

    if not args.po:
        print(json.dumps(main(), indent=2, ensure_ascii=False))

        if args.to_csv:
            # chnage file output to the one you understand
            df = pd.DataFrame(main()).to_csv(f'results_for_query_{args.search_query.replace(" ", "_")}.csv', index=False, encoding='utf-8')
            print(f'Saved to "results_for_query_{args.search_query.replace(" ", "_")}.csv"')

        if args.to_json:
            # chnage file output to the one you understand
            pd.DataFrame(main()).to_json(f'results_for_query_{args.search_query.replace(" ", "_")}.json', orient='records')
            print(f'Saved to "results_for_query_{args.search_query.replace(" ", "_")}.json"')

    

    

    












# class PositionTracker:
#     def __params(self, lang, country, location, google_domain, number_of_results):
#         params = {
#             'api_key': os.getenv(args.api_key),
#             'engine': 'google',
#             'q': args.search_query,
#             'hl': lang,
#             'gl': country,
#             'location': location,
#             'google_domain': google_domain,
#             'num': number_of_results
#         }

#         search = GoogleSearch(params)
#         results = search.get_dict()
#         return results
    
#     def __parse(self, lang, country, location, google_domain, number_of_results):
#         position_data = []
        
#         if isinstance(args.target_website, str) and isinstance(args.target_keyword, str):
#             results = self.__params(
#                 lang=lang,
#                 country=country,
#                 location=location,
#                 google_domain=google_domain,
#                 number_of_results=number_of_results
#             )

#             for result in results['organic_results']:
#                 if (
#                     args.target_keyword in result['title']
#                     and args.target_keyword in result['link']
#                     and args.target_website in result['link']
#                     and args.position_only
#                 ):
#                     position_data.append(result['position'])

#                 if (
#                     args.target_keyword in result['title']
#                     and args.target_keyword in result['link']
#                     and args.target_website in result['link']
#                     and not args.position_only
#                 ):
#                     position_data.append(
#                         {
#                             'position': result['position'],
#                             'country_of_the_search': country,
#                             'title': result['title'],
#                             'link': result['link'],
#                         }
#                     )

#         if isinstance(args.target_website, list) and isinstance(args.target_keyword, list):
#             for website, keyword in zip(args.target_website, args.target_keyword):
#                 results = self.__params(
#                     lang=lang,
#                     country=country,
#                     location=location,
#                     google_domain=google_domain,
#                     number_of_results=number_of_results
#                 )

#                 for result in results['organic_results']:
#                     if (
#                         keyword in result['title']
#                         and keyword in result['link']
#                         and website in result['link']
#                         and args.position_only
#                     ):
#                         position_data.append(result['position'])

#                     if (
#                         keyword in result['title']
#                         and keyword in result['link']
#                         and website in result['link']
#                         and not args.position_only
#                     ):
#                         position_data.append(
#                             {
#                                 'position': result['position'],
#                                 'country_of_the_search': country,
#                                 'title': result['title'],
#                                 'link': result['link'],
#                             }
#                         )

#         return position_data

#     def get_google_position(self,
#          lang: str = 'en',
#          country: str = 'us',
#          location: str = 'United States',
#          google_domain: str = 'google.com',
#          number_of_results: int = 10,
#          ):

#         return self.__parse(
#             lang=lang,
#             country=country,
#             location=location,
#             google_domain=google_domain,
#             number_of_results=number_of_results
#          )

    # def get_brave_search_position(self,
    #      lang: str = 'en',
    #      country: str = 'us',
    #      location: str = 'United States',
    #      google_domain: str = 'google.com',
    #      ):

    #     if isinstance(args.target_keyword, str):
    #         return self.__parse(lang=lang, country=country, location=location, google_domain=google_domain)

