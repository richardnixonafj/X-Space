import requests


def getx(endpoint, method=""):
    request_url = "https://api.spacexdata.com/v3/{end}/{meth}?pretty=true".format(end=endpoint, meth=method, timeout=0.001)
    res = requests.get(request_url)

    if not res.ok:
        res.raise_for_status()

    return res.json(), res.headers
