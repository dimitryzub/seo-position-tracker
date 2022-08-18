<h1 align="center">SEO Position Tracker 📡</h1>

<p align="center">A simple Python tool for SEO position tracking from Google and other search engines.</p>

<div align="center">

  <a href="https://pepy.tech/project/seo-position-tracker">![Downloads](https://static.pepy.tech/personalized-badge/seo-position-tracker?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)</a>
  <a href="">![licence](https://img.shields.io/github/license/dimitryzub/seo-position-tracker?color=blue)</a>

</div>


## 🔎 Current search engines support

- Google Search - looks for first 100 organic results.
- [See what's coming next](https://github.com/dimitryzub/seo-position-tracker/projects).


## ⚙️Installation

```bash
$ pip install seo-position-tracker
```

```bash
$ git clone https://github.com/dimitryzub/seo-position-tracking.git
```


## 🤹‍♂️Usage

#### Available CLI arugments:

```bash
$ python seo_position_tracker.py -h 
```

```lang-none
SerpApi SEO position tracker.

optional arguments:
  -h, --help         show this help message and exit
  --api-key API_KEY  your SerpApi API key. For more: https://serpapi.com/manage-api-key
  -se SE             search engine. Currently only one can be passed. Default: Google
  -po                returns website position only.
  -q Q               search query. Default: "Coffee"
  -tk TK             target keyword to track. Default: "coffee". Currently only one can be passed.
  -tw TW             target website to track. Default: "starbucks.com". Currently only one can be passed.
  -l L               language of the search. Default: "en" - English. For more: https://serpapi.com/google-languages
  -c C               country of the search. Default: "us" - United States. For more: https://serpapi.com/google-countries
  -loc LOC           location of the search. Default: "United States". For more: https://serpapi.com/locations-api
  --to-csv           saves results in the current directory to csv.
  --to-json          saves results in the current directory to json.
```

#### Example:

```bash
$ python seo_position_tracker.py --api-key=<your_serpapi_api_key> \
> -q="minecraft buy" \
> -tk minecraft \
> -tw minecraft.net \
> -l en -c us
```

```json
[
  {
    "position": 1,
    "country_of_the_search": "us",
    "title": "Get Minecraft: Gaming Platform Features",
    "link": "https://www.minecraft.net/en-us/get-minecraft"
  },
  {
    "position": 5,
    "country_of_the_search": "us",
    "title": "I Want to Buy Minecraft on a Non-Windows Device",
    "link": "https://help.minecraft.net/hc/en-us/articles/6661712171405-I-Want-to-Buy-Minecraft-on-a-Non-Windows-Device"
  }
]
```



#### Get position only

```bash
$ python seo_position_tracker.py --api-key=<your_serpapi_api_key> \
> -q="minecraft buy" \
> -tk minecraft \
> -tw  minecraft.net \
> -l en -c us \
> -po
```

```lang-none
[1]
# or 
[1, 5, ...]
```

## 💡Issues or suggestions

Visit [issues](https://github.com/dimitryzub/seo-position-tracking/issues) page.

## 📜 Licence

SEO Position Tracker is released under the [BSD-3-Clause Licence](https://github.com/dimitryzub/seo-position-tracker/blob/407a561b23e0905d88e4d9dd22390330e96889e1/LICENSE).

