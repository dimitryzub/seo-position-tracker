import requests, lxml
from bs4 import BeautifulSoup

# TODO: add list of countries Google domain as an optional argument: "google.br/google.uk/google.au", etc.
# TODO: add corresponding language ("hl" param) to defined Google domain. Example: if google.br -> hl:es (spanish)
# TODO: loop through all domains with appropriate language (later big release)

params = {
    "query": "minecraft",
    "target_keyword": "minecraft",
    "target_website": "play.google.com",
}


class PositionTracker:

    def __init__(self, params: {}):
        self.query = params["query"].lower().strip()
        self.target_keyword = params["target_keyword"].lower().strip()
        self.target_website = params["target_website"].lower().strip().replace(" ", "")

    def get_google_position(self, lang: str = "en", country: str = "us", return_position_only: bool = False):

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }

        params = {
            "q": self.query,
            "hl": lang,
            "gl": country
        }

        html = requests.get("https://www.google.com/search", params=params, headers=headers)
        soup = BeautifulSoup(html.text, "lxml")

        # if bad response from soup -> don't save HTML, otherwise -> SAVE to test it.

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

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }

        params = {"q": self.query}

        html = requests.get("https://search.brave.com/search", params=params, headers=headers)
        soup = BeautifulSoup(html.text, "lxml")

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
