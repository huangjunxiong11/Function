import requests
import json


class UrlGet(object):
    def __init__(self):
        pass

    def from_url_get_dict(self, url):
        # re = requests.get('http://108.88.4.4:5001')
        req = requests.get(url)
        json_str = req.content.decode(encoding='utf8')
        dict_str = json.loads(json_str)
        return dict_str


