<h1 align="center">SEO Position Tracker 📡</h1>

<p align="center">A simple Python CLI and in-code SEO position tracking tool for Google and 6 other search engines.</p>
<p align="center">This project uses <a href="http://serpapi.com/">SerpApi</a></p>


<div align="center">

  <a href="https://pepy.tech/project/seo-position-tracker">![Downloads](https://static.pepy.tech/personalized-badge/seo-position-tracker?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)</a>
  <a href="">![licence](https://img.shields.io/github/license/dimitryzub/seo-position-tracker?color=blue)</a>

</div>


## 🔎 Current search engines support

- Google Search - first 100 organic results.
- Baidu Search - first 50 organic results.
- Bing Search - first 50 organic results.
- DuckDuckGo Search - up to 30 organic results.
- Yahoo! Search - first 10 organic results.
- Yandex Search - up to 15 organic results.
- Naver Search - first 15 organic results.


## ⚙️Installation

```bash
$ pip install seo-position-tracker
```

Install from source:

```bash
$ git clone https://github.com/dimitryzub/seo-position-tracking.git
$ cd seo_position_tracker/
$ python -m venv env && source env/bin/activate # or env/Scripts/activate for Windows
$ poetry install
```

If you get an error, try: 
```bash
$ pip install chardet 
$ poetry install
```


## 🤹‍♂️Usage

#### Available CLI arugments:

```bash
$ python main.py -h
```

```lang-none
SerpApi SEO position tracker [-h] [-q] [-tk  [...]] [-tw  [...]] [-se  [...]] [-ak] [-hl] [-gl] [-loc] [-d] [-st]

A simple Python CLI for SEO position tracking from Google, Baidu, Bing, DuckDuckGo, Yahoo, Yandex and Naver.

optional arguments:
  -h, --help            show this help message and exit
  -q , --query          Search query. Default "coffee".
  -tk  [ ...], --target-keywords  [ ...]
                        Target keywords to track. Default "['coffee']".
  -tw  [ ...], --target-websites  [ ...]
                        Target websites to track. Default "['starbucks.com']".
  -se  [ ...], --search-engine  [ ...]
                        Choosing a search engine to track: "google", "baidu", "bing", "duckduckgo", "yahoo", "yandex", "naver". You can select multiple search engines. All search   
                        engines are selected by default.
  -ak , --api-key       Your SerpApi API key: https://serpapi.com/manage-api-key. Default is a test API key to test CLI.
  -hl , --lang          Language of the search. Supported only for "google", "baidu", "yahoo" and "yandex" engines. Default "None". Find more by Googling: "SerpApi supported        
                        <engine> languages"
  -gl , --country       Country of the search. Supported only for "google", "bing" and "yahoo" engines. Default "None". Find more by Googling: "SerpApi supported <engine>
                        countries"
  -loc , --location     Location of the search. Supported only for "google", "bing", "duckduckgo" and "yandex" engines. Default "None". Find more by Googling: "SerpApi supported    
                        <engine> locations"
  -d , --domain         Search engine domain to use. Supported only for "google", "yahoo" and "yandex" engines. Default "None". Find more by Googling: "SerpApi supported <engine>   
                        domains"
  -st , --save-to       Saves the results in the current directory in the selected format (CSV, JSON, TXT). Default CSV.

Found a bug? Open issue: https://github.com/dimitryzub/seo-position-tracker/issues
```

## 🤹‍♂️Examples

#### Extracting positions from all search engines for a given query with a target website and a target keyword:

```bash
$ python main.py --api-key=<your_serpapi_api_key> \
-q "minecraft" \
-tk official \
-tw minecraft.net
```

```json
[
  {
    "engine": "google",
    "position": 1,
    "title": "Welcome to the Minecraft Official Site | Minecraft",
    "link": "https://www.minecraft.net/en-us"
  },
  {
    "engine": "bing",
    "position": 1,
    "title": "Minecraft - Official Site",
    "link": "https://minecraft.net/"
  },
  {
    "engine": "bing",
    "position": 2,
    "title": "Welcome to the Minecraft Official Site | Minecraft",
    "link": "https://www.minecraft.net/en-us"
  },
  {
    "engine": "bing",
    "position": 10,
    "title": "Minecraft Official Site | Minecraft Education",
    "link": "https://education.minecraft.net/en-us"
  },
  {
    "engine": "duckduckgo",
    "position": 1,
    "title": "Minecraft - Official Site",
    "link": "https://minecraft.net/"
  },
  {
    "engine": "duckduckgo",
    "position": 2,
    "title": "Welcome to the Minecraft Official Site | Minecraft",
    "link": "https://www.minecraft.net/en-us"
  },
  {
    "engine": "yahoo",
    "position": 1,
    "title": "Minecraft - Official Site",
    "link": "https://minecraft.net/"
  },
  {
    "engine": "yahoo",
    "position": 2,
    "title": "Welcome to the Minecraft Official Site | Minecraft",
    "link": "https://www.minecraft.net/en-us"
  },
  {
    "engine": "yandex",
    "position": 2,
    "title": "Welcome to the Minecraft Official Site | Minecraft",
    "link": "https://www.minecraft.net/"
  }
]
```

#### Extracting positions from 3 search engines with default arguments and saving to JSON:

```bash
$ python main.py --api-key=<your_serpapi_api_key> \
-se google bing duckduckgo \
-st JSON
```

```json
[
  {
    "engine": "google",
    "position": 6,
    "title": "Starbucks Coffee Company",
    "link": "https://www.starbucks.com/"
  },
  {
    "engine": "bing",
    "position": 12,
    "title": "The Best Coffee from Starbucks Coffee: Starbucks Coffee Company",
    "link": "https://www.starbucks.com/coffee/"
  },
  {
    "engine": "duckduckgo",
    "position": 11,
    "title": "The Best Coffee from Starbucks Coffee: Starbucks Coffee Company",
    "link": "https://www.starbucks.com/coffee/"
  }
]
```

#### Extracting positions from one engine with all arguments for it:

```bash       
$ python main.py --api-key=<your_serpapi_api_key> \
-q serpapi \
-tk serpapi \
-tw https://serpapi.com/ https://github.com/ \
-se google \
-hl de \
-gl de \
-loc Germany \
-d google.de \
-st TXT
```

```json
[
  {
    "engine": "google",
    "position": 1,
    "title": "SerpApi: Google Search API",
    "link": "https://serpapi.com/"
  },
  {
    "engine": "google",
    "position": 3,
    "title": "SerpApi - GitHub",
    "link": "https://github.com/serpapi"
  }
]
```

#### Extracting positions from all search engines manually (without CLI):

```python
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
```

## 💡Issues or suggestions

Visit [issues](https://github.com/dimitryzub/seo-position-tracking/issues) page.

## 📜 Licence

SEO Position Tracker is released under the [BSD-3-Clause Licence](https://github.com/dimitryzub/seo-position-tracker/blob/407a561b23e0905d88e4d9dd22390330e96889e1/LICENSE).

