import requests
import json
import config

class TeamsApi:
    def __init__(self, rootApiUrl):
        self.rootApiUrl = rootApiUrl
        self.headers = headers = {
            'Client-ID': config.twitchClientID
        }

    def getAllTeams(self, limit=25, offset=0):
        url = self.rootApiUrl + "teams"
        queryString = ""

        if limit is not None:
            queryString += '?limit=' + limit
        if offset is not None:
            queryString += '?offset=' + offset

        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text

    def getTeam(self, team_name=''):
        url = self.rootApiUrl + "teams/%s" % team_name
        queryString = ""
        req = requests.request('GET', url + queryString, headers=self.headers)
        return req.text
