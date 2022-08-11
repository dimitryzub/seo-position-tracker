'''
TestPositionTracker() class mimics PositionTracker() class.
The only difference is that reads HTML file, instead of calling requests.get() method.

This is ONLY for testing purpose because using mocks makes me punch the wall.
Later might be changed with appropriate thing.

PositionTracker() saves HTML locally if the response from requests.get() is OK,
then HTML is being passed to test_seo_position_tracker.py for testing purpose,
instead of making actual requests.get() which will slow testing speed a lot.

Thinking behind it: First, make it stupidly simple that just works.
'''

from pathlib import Path
from serpapi import GoogleSearch

HTMLS = {
    "google": Path(__file__).parent.resolve() / "htmls" / "google_tracker.html",
    "brave": Path(__file__).parent.resolve() / "htmls" / "brave_search_tracker.html"
}

params = {
    "query": "minecraft",
    "target_keyword": "minecraft",
    "target_website": "play.google.com",
}


class PositionTrackerTest:

    def __init__(self, params: {}):
        self.query = params["query"].lower().strip()
        self.target_keyword = params["target_keyword"].lower().strip()
        self.target_website = params["target_website"].lower().strip().replace(" ", "")

    def get_google_position(self, lang: str = "en", country: str = "us", return_position_only: bool = False):

        with open(HTMLS['google'], encoding='utf-8') as html:
            soup = BeautifulSoup(html.read(), "lxml")

            position_data = []

            for index, result in enumerate(soup.select(".tF2Cxc")):
                title = result.select_one(".DKV0Md").text.lower()
                link = result.select_one(".yuRUbf a")["href"].lower()

                if self.target_keyword in title and self.target_keyword in link and self.target_website in link and return_position_only:
                    position_data.append(index + 1)

                if self.target_keyword in title and self.target_keyword in link and self.target_website in link and not return_position_only:
                    position_data.append({
                        "position": index + 1,
                        "country_of_the_search": country,
                        "title": title,
                        "link": link
                    })

            return position_data

    def get_brave_search_position(self, return_position_only: bool = False):

        with open(HTMLS['brave'], encoding='utf-8') as html:
            soup = BeautifulSoup(html.read(), "lxml")

            position_data = []

            for index, result in enumerate(soup.select(".snippet.fdb")):
                title = result.select_one(".snippet-title").text.lower().strip()
                link = result.select_one("a")["href"].lower().strip()

                if self.target_keyword in title and self.target_keyword in link and self.target_website in link and return_position_only:
                    position_data.append(index + 1)

                if self.target_keyword in title and self.target_keyword in link and self.target_website in link and not return_position_only:
                    position_data.append({
                        "position": index + 1,
                        "title": title,
                        "link": link
                    })

            return position_data
