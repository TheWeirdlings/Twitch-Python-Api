import requests
import json
import config

class BitsApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getCheermotes(self, channelId=None):
        url = self.rootApiUrl + "bits/actions?api_version=5"
        queryString = ""
        if channelId is not None:
            queryString += '&channel_id=' + channelId

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text
