import requests


def getx(endpoint, method="", query={}):
    request_url = "https://api.spacexdata.com/v3/{end}/{meth}?pretty=true".format(end=endpoint, meth=method)
    res = requests.get(request_url, params=query)

    if not res.ok:
        res.raise_for_status()

    return res.json(), res.headers
