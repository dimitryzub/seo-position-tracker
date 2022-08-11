import argparse, json
from serpapi import GoogleSearch
import pandas as pd

parser = argparse.ArgumentParser(prog='SerpApi SEO Position Tracker')

# usage: --api-key 213128sad or --api-key=213128sad or --api-key="213128sad"
parser.add_argument('--api-key', required=True, type=str, help='Your SerpApi API key.')
parser.add_argument('-se', '--search-engine', type=str, default='google', help='Search engine where search happens.')
parser.add_argument('-po', '--position-only', action='store_true', help='Returns website position only')

# usage: python <script.py> -q="<your are breathtaking and this sentance is long and beautiful>". Same with --search_query
parser.add_argument(
    '-q',
    '--search-query',
    type=str,
    default='coffee',
    help='Search query. Default: "Coffee"',
)
parser.add_argument(
    '-tk',
    '--target-keyword',
    type=str,
    nargs='+',
    default='coffee',
    help='Target keyword to track. Should be at least 1. Default: "Coffee"',
)
parser.add_argument(
    '-tw',
    '--target-website',
    type=str,
    nargs='+',
    default='starbucks.com',
    help='Target website to track. Should be at least 1. Default: "starbucks.com"',
)
parser.add_argument('--to-csv', action='store_true', help='Saves Results to CSV.')
parser.add_argument('--to-json', action='store_true', help='Saves Results to JSON.')

args = parser.parse_args()

for keyword, website in zip(args.target_keyword, args.target_website):
    print(website)
    print(keyword)

def main():

    for website, keyword in zip(args.target_website, args.target_keyword):
        params = {
            'api_key': args.api_key,
            'engine': 'google',
            'q': args.search_query,
            'hl': 'en',
            'gl': 'us',
            'location': 'United States',
            'google_domain': 'google.com',
            'num': 100
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        position_data = []

        for result in results['organic_results']:
            if (
                keyword in result['title'].lower()
                and keyword in result['link']
                and website in result['link']
                and args.position_only
            ):
                position_data.append(result['position'])

                return position_data

            if (
                keyword in result['title'].lower()
                and keyword in result['link']
                and website in result['link']
                and not args.position_only
            ):
                position_data.append(
                    {
                        'position': result['position'],
                        'country_of_the_search': params['gl'],
                        'title': result['title'],
                        'link': result['link'],
                    }
                )

                return position_data


if __name__ == '__main__':
    if not args.position_only:
        print(json.dumps(main(), indent=2, ensure_ascii=False))

        if args.to_csv:
            df = pd.DataFrame(main()).to_csv(f'position_for_{args.search_query}_and_{args.target_website}.csv', index=False, encoding='utf-8')
            print(f'Saved to "position_for_{args.search_query}_and_{args.target_website}.csv"')

        if args.to_json:
            pd.DataFrame(main()).to_json(f'position_for_{args.search_query}_and_{args.target_website}.json', orient='records', lines=True)
            print(f'Saved to "position_for_{args.search_query}_and_{args.target_website}.json"')

    # [1] -> 1
    if args.position_only:
        print(main()[0])

    

    












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

