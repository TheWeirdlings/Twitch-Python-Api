import requests
import json
import config

class ChatApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getChatBadgesByChannel(self, channelId):
        url = self.rootApiUrl + "chat/%s/badges" % channelId
        queryString = ""

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getChatEmoticonsBySet(self, emotesets=[]):
        url = self.rootApiUrl + "chat/emoticon_images"
        queryString = ""
        if emotesets is not None:
            queryString += '?emotesets=' + emotesets
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getAllChatEmoticons(self, channelId):
        url = self.rootApiUrl + "streams/emoticon_images"
        queryString = ""

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text
