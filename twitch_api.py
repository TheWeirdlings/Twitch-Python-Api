import requests
import json
import config
from lib.Streams import StreamApi
from lib.Bits import BitsApi

class TwitchApi:
    def __init__(self):
        self.rootApiUrl = "https://api.twitch.tv/kraken/"
        self.streams = StreamApi(self.rootApiUrl)
        self.bits = BitsApi(self.rootApiUrl)

    def getFollowers(self, channel = None, cursor = None, limit = 25, direction = 'desc'):
        if channel is None:
            #TODO: throw?
            print("Channel is required")
            return

        url = self.rootApiUrl + "channels/%s/follows" % channel
        queryString = "?limit=%s&direction=%s" % (limit, direction)

        if cursor is not None:
            queryString += "&cursor=%s" % cursor

        headers = {
            'Client-ID': config.twitchClientID
        }

        req = requests.get(url + queryString, headers=headers)
        return req.text

    def getViewers(self, channel):
        url = "https://tmi.twitch.tv/group/user/%s/chatters" % channel
        queryString = ""
        req = requests.request('GET', url + queryString)
        return req.text

    def getChannel(self):
        url = self.rootApiUrl + "channel"
        queryString = ""

        headers = {
            'Client-ID': config.twitchClientID
        }
        print(headers)
        req = requests.request('GET', url + queryString, headers=headers)
        return req.text

    def getChannelById(self, channelId):
        url = self.rootApiUrl + "channels/%s" % channelId
        queryString = ""

        headers = {
            'Client-ID': config.twitchClientID
        }

        req = requests.request('GET', url + queryString, headers=headers)
        return req.text

if __name__ == "__main__":
    twitchApi = TwitchApi()
    followers = twitchApi.bits.getStreamsByUser('thehollidayinn')
    followers = json.loads(followers)
    print(followers)

    # followers = twitchApi.streams.getStreams()
    # followers = json.loads(followers)
    # print(followers)

    # followers = twitchApi.streams.getStreamsSummary()
    # followers = json.loads(followers)
    # print(followers)

    # followers = twitchApi.streams.getFeaturedStreams()
    # followers = json.loads(followers)
    # print(followers)

    # followers = twitchApi.streams.getFollowedStreams()
    # followers = json.loads(followers)
    # print(followers)

    # print(followers['_cursor'])
    #
    # for follower in followers['follows']:
    #     print(follower['user']['display_name'])
