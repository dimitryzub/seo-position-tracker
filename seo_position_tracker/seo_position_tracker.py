from serpapi import GoogleSearch, BaiduSearch, BingSearch, DuckDuckGoSearch, YahooSearch, YandexSearch, NaverSearch
import json, csv


class SeoPositionTracker:
    def __init__(self, query: str, api_key: str, keywords: list, websites: list, lang: str = None, country: str = None, location: str = None, domain: str = None) -> None:
        self.query = query
        self.api_key = api_key
        self.keywords = keywords
        self.websites = websites
        self.lang = lang
        self.country = country
        self.location = location
        self.domain = domain


    def __find_positions(self, results: dict, engine: str) -> list:
        data = []

        for keyword in self.keywords:
            # links in Baidu Search have this format http://www.baidu.com/link?url=R9iXojWG2Aq-dp0xgO5UhGPqv2rwVH4dJ9g9zQHrMmyTZYrGbIOU1w7CAvf2QjR9Lj8UhkWp6PcUVsYE3ECqorYZojMeQ9O6kmoYfxJv2d3
            # so there is no way to check if the target website exists in the link
            if engine == 'baidu':
                for result in results.get('organic_results', []):
                    check = keyword.lower() in result.get('title', '').lower()
                    
                    if not check:
                        continue
                    
                    data.append({
                        'engine': engine,
                        'position': result.get('position'),
                        'title': result.get('title'),
                        'link': result.get('link')
                    })
            else:
                for website in self.websites:
                    for result in results.get('organic_results', []):
                        check = keyword.lower() in result.get('title', '').lower() and website in result.get('link')
                        
                        if not check:
                            continue
                        
                        data.append({
                            'engine': engine,
                            'position': result.get('position'),
                            'title': result.get('title'),
                            'link': result.get('link')
                        })
        
        return data


    def __check_params(self, lang: str = None, country: str = None, location: str = None, domain: str = None) -> tuple:
        '''The function checks if class variables exist. If there are any, then these variables are overwritten instead of the default parameters.'''
        checked_params = []

        if lang:
            if self.lang:
                lang = self.lang
            checked_params.append(lang)

        if country:
            if self.country:
                country = self.country
            checked_params.append(country)

        if location:
            if self.location:
                location = self.location
            checked_params.append(location)
        
        if domain:
            if self.domain:
                domain = self.domain
            checked_params.append(domain)

        if len(checked_params) == 1:
            return checked_params[0]
        
        return tuple(checked_params)

    
    def scrape_google(self, lang: str = 'en', country: str = 'us', location: str = 'United States', domain: str = 'google.com') -> list:
        '''
        The `lang` parameter defines the language to use for the Google search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). \
        Head to the [Google languages page](https://serpapi.com/google-languages) for a full list of supported Google languages.

        The `country` parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for United States, `uk` for United Kingdom, or `fr` for France). \
        Head to the [Google countries page](https://serpapi.com/google-countries) for a full list of supported Google countries.

        The `location` parameter defines from where you want the search to originate. If several locations match the location requested, the most popular will be selected. \
        Head to the [/locations.json API](https://serpapi.com/locations-api) if you need more precise control.
        
        The `domain` parameter defines the Google domain to use. It defaults to `google.com`. \
        Head to the [Google domains page](https://serpapi.com/google-domains) for a full list of supported Google domains.
        '''
        lang, country, location, domain = self.__check_params(lang=lang, country=country, location=location, domain=domain)
        
        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'q': self.query,                # search query
            'engine': 'google',             # search engine
            'google_domain': domain,        # Google domain to use
            'hl': lang,                     # language of the search
            'gl': country,                  # country of the search
            'location': location,           # location of the search
            'num': 100                      # 100 results from Google search
        }

        search = GoogleSearch(params)       # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'google')


    def scrape_baidu(self, lang: str = '1') -> list:
        '''
        The `lang` parameter defines which language to restrict results. Available options:

        `1` - All languages

        `2` - Simplified Chinese

        `3` - Traditional Chinese
        '''
        lang = self.__check_params(lang=lang)
        
        if lang not in ['1', '2', '3']:
            lang = '1'

        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'q': self.query,                # search query
            'engine': 'baidu',              # search engine
            'ct': lang,                     # language to restrict results
            'rn': 50                        # 50 results from Baidu search
        }

        search = BaiduSearch(params)        # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'baidu')


    def scrape_bing(self, country: str = 'us', location: str = 'United States') -> list:
        '''
        The `country` parameter defines the country to search from. It follows the 2-character [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) format. \
        (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.).
        
        The `location` parameter defines from where you want the search to originate. \
        If several locations match the location requested, we'll pick the most popular one. \
        Head to the [/locations.json API](https://serpapi.com/locations-api) if you need more precise control.
        '''
        country, location = self.__check_params(country=country, location=location)
        
        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'q': self.query,                # search query
            'engine': 'bing',               # search engine
            'cc': country,                  # country of the search
            'location': location,           # location of the search
            'count': 50                     # 50 results from Bing search
        }

        search = BingSearch(params)         # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'bing')


    def scrape_duckduckgo(self, location: str = 'us-en') -> list:
        '''
        The `location` parameter defines the region to use for the DuckDuckGo search. Region code examples: 
        
        `us-en` for United States
        
        `uk-en` for United Kingdom 
        
        `fr-fr` for France

        Head to the [DuckDuckGo regions](https://serpapi.com/duckduckgo-regions) for a full list of supported regions.
        '''
        location = self.__check_params(location=location)

        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'q': self.query,                # search query
            'engine': 'duckduckgo',         # search engine
            'kl': location
        }

        search = DuckDuckGoSearch(params)   # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'duckduckgo')


    def scrape_yahoo(self, lang: str = 'lang_en', country: str = 'us', domain: str = 'uk') -> list:
        '''
        The `lang` parameter defines language to limit the search to. It uses `lang_{two-letter language code}` to specify languages (e.g., `lang_fr` will only search French). \
        You can check [a full list of supported Yahoo! languages](https://serpapi.com/yahoo-vl-languages).

        The `country` parameter defines the country to use for the Yahoo! search. It's a two-letter country code (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). \
        Head to the [Yahoo! countries](https://serpapi.com/yahoo-vc-countries) for a full list of supported Yahoo! countries.
        
        The `domain` parameter defines the Yahoo! domain to use. It defaults to `uk`. If specified domain is allowed, \
        it will be prepended to the domain. You can check [a full list of supported Yahoo! domains](https://serpapi.com/yahoo-domains).
        '''
        lang, country, domain = self.__check_params(lang=lang, country=country, domain=domain)

        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'p': self.query,                # search query
            'engine': 'yahoo',              # search engine
            'yahoo_domain': domain,         # Yahoo! domain to use
            'vl': lang,                     # language of the search
            'vc': country                   # country of the search
        }

        search = YahooSearch(params)        # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'yahoo')


    def scrape_yandex(self, lang: str = 'en', domain: str = 'yandex.com') -> list:
        '''
        The `lang` parameter defines the language to use for the Yandex search. \
        Head to the [Yandex languages](https://serpapi.com/yandex-languages) for a full list of supported Yandex languages.

        The `domain` parameter defines the Yandex domain to use. It defaults to `yandex.com`. \
        Head to the [Yandex domains](https://serpapi.com/yandex-domains) for a full list of supported Yandex domains.
        '''
        lang, domain = self.__check_params(lang=lang, domain=domain)

        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'text': self.query,             # search query
            'engine': 'yandex',             # search engine
            'yandex_domain': domain,        # Yandex domain to use
            'lang': lang                    # language of the search
        }

        search = YandexSearch(params)       # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'yandex')


    def scrape_naver(self) -> list:
        params = {
            'api_key': self.api_key,        # https://serpapi.com/manage-api-key
            'query': self.query,            # search query
            'engine': 'naver',              # search engine
            'where': 'web'                  # web organic results
        }

        search = NaverSearch(params)        # data extraction on the SerpApi backend
        results = search.get_dict()         # JSON -> Python dict
        
        return self.__find_positions(results, 'naver')


    def save_to_csv(self, data: list) -> None:
        keys = data[0].keys()

        with open(f"{self.query.replace(' ', '_')}.csv", 'w', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, keys)
            writer.writeheader()
            writer.writerows(data)
        

    def save_to_json(self, data: list) -> None:
        with open(f"{self.query.replace(' ', '_')}.json", 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)


    def save_to_txt(self, data: list) -> None:
        with open(f'{self.query.replace(" ", "_")}.txt', 'w', encoding='utf-8') as txt_file:
            for element in data:
                txt_file.write(f"{element.get('engine')} {element.get('position')} {element.get('title')} {element.get('link')}\n")
