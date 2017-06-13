from ..twitch_api import TwitchApi

if __name__ == "__main__":
    twitchApi = TwitchApi()
    followers = twitchApi.streams.getStreams('thehollidayinn')
    followers = json.loads(followers)
    print(followers)
    print(followers['_cursor'])

    for follower in followers['follows']:
        print(follower['user']['display_name'])
