# Seo Position Tracker 📡
A simple Python package for SEO position tracking from Google and other search engines.
___

[![codecov](https://codecov.io/gh/dimitryzub/seo-position-tracker/branch/main/graph/badge.svg?token=RX5P8YWEZG)](https://codecov.io/gh/dimitryzub/seo-position-tracker)
![CI workflow](https://github.com/dimitryzub/seo-position-tracker/actions/workflows/ci.yml/badge.svg)
[![Downloads](https://static.pepy.tech/personalized-badge/seo-position-tracker?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/seo-position-tracker)

![python versions](https://img.shields.io/pypi/pyversions/seo-position-tracker)
![licence brought by shields.io](https://img.shields.io/github/license/dimitryzub/seo-position-tracker?color=blue)


![twitter account brought by shield.io](https://img.shields.io/twitter/follow/DimitryZub?style=social)



Currently, supports:
- Google Search
- Brave Search
- [See what's coming next](https://github.com/dimitryzub/seo-position-tracker/projects).

See [how results being checked](https://github.com/dimitryzub/seo-position-tracker/#-how-results-are-being-filtered).

## 🤹‍♂️Usage

_The following examples will be pretty much the same for other search engines._

Each `get_SEARCH_ENGINE_NAME_position()` will have its own arguments. 

#### 1. Define parameters

```python
# define parameters and pass them to PositionTracker() class
params = {
    "query": "minecraft",
    "target_keyword": "minecraft",
    "target_website": "play.google.com"
}
```

#### 2. Get position only

```python
from seo_position_tracker import PositionTracker

                             # other_search_engine()
PositionTracker(params=params).get_google_position(return_position_only=True)
# [3] (third position on the first page)
```

#### 3. Get position with additional info

```python
from seo_position_tracker import PositionTracker

                             # other_search_engine()
PositionTracker(params=params).get_google_position(country="uk", lang="en") # change to what you need

'''
[
  {
    "position": 3,
    "title": "minecraft - apps on google play",
    "link": "https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en_us&gl=us"
  }
  # might be other results.. 
]
'''
```

## 🛸 How results are being filtered

Result comes out of checking if **target_keyword** is in _title_ and _link_, and **target_website** is in _link_. 

```python
params = {
    "query": "minecraft",                 # just a query
    "target_keyword": "minecraft",        # being checked for match both in title and link
    "target_website": "play.google.com"   # checks for match in website URL 
}


#                target_website                                target_keyword
#                     ↓↓↓                                           ↓↓↓
# Link: https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en&gl=US

# ------------------------------------------

#      target_keyword     
#           ↓↓↓
# Title: Minecraft - Apps on Google Play
```

## ⚙️Installation

```python
pip install seo-position-tracker
```

```lang-none
git clone https://github.com/dimitryzub/seo-position-tracking.git
```


## 💡Suggestions
For suggestions, visit [suggestions](https://github.com/dimitryzub/seo-position-tracking/discussions) page.

## 🔦Issues
For issues, visit [issues](https://github.com/dimitryzub/seo-position-tracking/issues) page.
