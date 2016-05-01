import requests
import json

class TwitchApi:
    def __init__(self):
        self.rootApiUrl = "https://api.twitch.tv/kraken/"

    def getFollowers(self, channel = None, cursor = None, limit = 25, direction = 'desc'):
        if channel is None:
            #TODO: throw?
            print("Channel is required")
            return

        url = self.rootApiUrl + "/channels/%s/follows" % channel
        queryString = "?limit=%s&direction=%s" % (limit, direction)

        if cursor is not None:
            queryString += "&cursor=%s" % cursor

        req = requests.request('GET', url + queryString)
        return req.text


if __name__ == "__main__":
    twitchApi = TwitchApi()
    followers = twitchApi.getFollowers('weirdlings')
    followers = json.loads(followers)
    print followers['_cursor']

    for follower in followers['follows']:
        print follower['user']['display_name']
