import requests
import json
import config

class ChannelFeedsApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getChannel(self):
        url = self.rootApiUrl + "/channel/
        req = requests.request('GET', url, headers=self.headers)
        return req.text

    def getChannelById(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "?api_version=5"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def updateChannel(self, channelId=None, status=None, game=None, delay=None, channel_feed_enabled=None):
        url = self.rootApiUrl + "/channel/" + channelId + "?api_version=5"
        queryString = ""

        data = {
            'status': status,
            'game': game,
            'delay': delay,
            'channel_feed_enabled': channel_feed_enabled,
        }

        req = requests.request('PUT', url, headers=self.headers, data)
        return req.text

    def getChannelEditors(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/editors?api_version=5"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getChannelFollows(self, channelId=None, limit=25, offset=0, cursor=None, direction='desc'):
        url = self.rootApiUrl + "/channel/" + channelId + "/follows?api_version=5"
        queryString = ""

        if limit:
            queryString += '&limit=' + limit

        if offset:
            queryString += '&offset=' + offset

        if cursor:
            queryString += '&cursor=' + cursor

        if direction:
            queryString += '&direction=' + direction

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getChannelTeams(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/teams?api_version=5"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getChannelSubscriptions(self, channelId=None, limit=25, offset=0, direction='desc'):
        url = self.rootApiUrl + "/channel/" + channelId + "/subscriptions?api_version=5"
        queryString = ""

        if limit:
            queryString += '&limit=' + limit

        if offset:
            queryString += '&offset=' + offset

        if direction:
            queryString += '&direction=' + direction

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getChannelSubscriptionByUser(self, channelId=None, userId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/subscriptions/" + userId + "?api_version=5"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getChannelVideos(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/videos?api_version=5"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def startChannelCommercial(self, channelId=None, length=30):
        url = self.rootApiUrl + "/channel/" + channelId + "/commercial?api_version=5"
        queryString = ""

        data = {
            'length': length
        }

        req = requests.request('POST', url + queryString, headers=self.headers, data)
        return req.text

    def resetChannelStreamKey(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/stream_key?api_version=5"
        queryString = ""
        req = requests.request('DELETE', url + queryString, headers=self.headers)
        return req.text

    def getChannelCommunity(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/community?api_version=5"
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def setChannelCommunity(self, channelId=None, communityId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/community" + communityId + "?api_version=5"
        queryString = ""
        req = requests.request('PUT', url + queryString, headers=self.headers)
        return req.text

    def deleteChannelFromCommunity(self, channelId=None):
        url = self.rootApiUrl + "/channel/" + channelId + "/community?api_version=5"
        queryString = ""
        req = requests.request('DELETE', url + queryString, headers=self.headers)
        return req.text
