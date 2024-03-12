import json
import requests
import urllib.request

class PostcodesAPI:
    def __init__(self, postcodes_url):
        postcodes_info = self._open_json_file(postcodes_url)
        self.status = postcodes_info['status']
        self.result = postcodes_info['result']

    def _open_json_file(self, url):
        with urllib.request.urlopen(url) as postcodes_url:
            return json.load(postcodes_url)


random_postcodes_obj = PostcodesAPI("https://api.postcodes.io/random/postcodes")
query_postcode_obj = PostcodesAPI("https://api.postcodes.io/postcodes/SW195AE")

print(random_postcodes_obj.status)
print(random_postcodes_obj.result)
print(query_postcode_obj.result)