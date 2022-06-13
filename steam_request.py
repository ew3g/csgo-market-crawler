import json
import requests


class SteamRequest:

    def __init__(self, steam_api_key):
        self.steam_api_key = steam_api_key

    def make_request(self, query, max_results):
        cookie = {'steamLoginSecure': self.steam_api_key}
        url = f'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default' \
              f'{query}&count={max_results}&appid=730&sort_dir=desc&norender=1 '
        response = requests.get(url, cookies=cookie)
        return json.loads(response.content)
