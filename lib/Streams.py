import requests
import json
import config

class StreamApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getStreamsByUser(self, channelId, stream_type='live'):
        url = self.rootApiUrl + "streams/%s" % channelId
        queryString = ""
        if stream_type is not None:
            queryString += '?stream_type=' + stream_type
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getStreams(self):
        url = self.rootApiUrl + "streams"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getStreamsSummary(self):
        url = self.rootApiUrl + "streams/summary"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getFeaturedStreams(self):
        url = self.rootApiUrl + "streams/featured"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getFollowedStreams(self):
        url = self.rootApiUrl + "streams/followed"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text
