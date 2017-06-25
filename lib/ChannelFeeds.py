import requests
import json
import config

class ChannelFeedsApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getFeedPosts(self, channelId=None, limit=10, cursor=False, comments=5):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts?api_version=5"
        queryString = ""

        queryString += '&limit=' + limit + '&cursor=' + cursor + '&comments=' + comments

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getFeedPost(self, channelId=None, postId=None, comments=5):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "?api_version=5"

        queryString = ""
        queryString += '&comments=' + comments

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def createFeedPost(self, channelId=None, conent=None, share=False):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts?api_version=5"

        data = {
            'content': content,
            'share': share,
        }

        req = requests.request('POST', url, headers=self.headers, data=data)
        return req.text

    def deleteFeedPost(self, channelId=None, postId=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "?api_version=5"

        req = requests.request('DELETE', url, headers=self.headers)
        return req.text

    def createReactionToFeedPost(self, channelId=None, postId=None, emoteValue=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "/reactions?api_version=5"

        queryString = ""
        queryString += '&emoteValue=' + emoteValue

        req = requests.request('POST', url, headers=self.headers)
        return req.text

    def deleteReactionToFeedPost(self, channelId=None, postId=None, emoteValue=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "/reactions?api_version=5"

        queryString = ""
        queryString += '&emoteValue=' + emoteValue

        req = requests.request('DELETE', url + queryString, headers=self.headers)
        return req.text

    def getFeedComments(self, channelId=None, postId=None, limit=10, cursor=False):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "/comments?api_version=5"

        queryString = ""
        queryString += '&limit=' + limit + '&cursor=' + cursor

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def createFeedComment(self, channelId=None, postId=None, conent=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "/comments?api_version=5"

        data = {
            'content': content,
        }

        req = requests.request('POST', url, headers=self.headers, data=data)
        return req.text

    def deleteFeedComment(self, channelId=None, postId=None, commentId=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + \
            "/comments/" + commentId + "?api_version=5"

        req = requests.request('DELETE', url, headers=self.headers)
        return req.text

    def createReactionToFeedComment(self, channelId=None, postId=None, commentId=None, emoteValue=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "/comments" \
            commentId + "/reactions?api_version=5"

        queryString = ""
        queryString += '&emoteValue=' + emoteValue

        req = requests.request('POST', url + queryString, headers=self.headers, data=data)

    def deleteReactionToFeedComment(self, channelId=None, postId=None, commentId=None, emoteValue=None):
        url = self.rootApiUrl + "/feed/" + channelId + "/posts/" + postId + "/comments" \
            commentId + "/reactions?api_version=5"

        queryString = ""
        queryString += '&emoteValue=' + emoteValue

        req = requests.request('DELETE', url + queryString, headers=self.headers, data=data)
