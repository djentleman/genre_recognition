# simple wrapper around HTTP APIs

import requests


def httpGet(req):
    res = requests.get(req)
    return res

def getJSON(req):
    return httpGet(req).json()
