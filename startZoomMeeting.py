import requests
from requests.structures import CaseInsensitiveDict
import webbrowser

url = "https://api.zoom.us/v2/meetings/{meetingId}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {bearerToken}"


resp = requests.get(url, headers=headers).json()
url = resp['start_url']
webbrowser.open(url)