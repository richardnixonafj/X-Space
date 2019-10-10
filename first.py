
# GET Past Launches
import requests
url = 'https://api.spacexdata.com/v3/launches/past'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)

# Upcoming Launches
import requests
url = 'https://api.spacexdata.com/v3/launches/upcoming'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)

# GET Latest Launch
import requests
url = 'https://api.spacexdata.com/v3/launches/latest'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)

# GET Next Launch
import requests
url = 'https://api.spacexdata.com/v3/launches/next'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)