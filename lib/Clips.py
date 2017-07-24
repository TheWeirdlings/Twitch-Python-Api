import requests
import json
import config

class ClipsApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getClip(self, slug=None):
        url = self.rootApiUrl + "/clips/" + slug + "?api_version=5"
        req = requests.request('GET', url, headers=self.headers)
        return req.text

    def getTopClips(self, channel=None, cursor=None, game=None, language=None, limit=10, period="week", trending=False):
        url = self.rootApiUrl + "/clips/top?api_version=5"

        if channel:
            queryString += '&channel=' + channel

        if cursor:
            queryString += '&cursor=' + cursor

        if game:
            queryString += '&game=' + game

        if language:
            queryString += '&language=' + language

        if limit:
            queryString += '&limit=' + limit

        if period:
            queryString += '&period=' + period

        if trending:
            queryString += '&trending=' + trending

        url = url + queryString

        req = requests.request('GET', url, headers=self.headers)
        return req.text

    def getFollowedClips(self, cursor=None, limit=10, trending=False):
        url = self.rootApiUrl + "/clips/followed?api_version=5"

        if cursor:
            queryString += '&cursor=' + cursor

        if limit:
            queryString += '&limit=' + limit

        if trending:
            queryString += '&trending=' + trending

        url = url + queryString

        req = requests.request('GET', url, headers=self.headers)
        return req.text
