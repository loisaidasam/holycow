
import json
import logging

import requests

from athlete import Athlete
from team import Team
from news import News
from scores import EventScore


logger = logging.getLogger(__name__)


class Api(object):
    RESOURCE_SPORTS_BASEBALL_MLB = 'sports/baseball/mlb'
    RESOURCE_SPORTS_FOOTBALL_NFL = 'sports/football/nfl'
    RESOURCES = (
        RESOURCE_SPORTS_BASEBALL_MLB,
        RESOURCE_SPORTS_FOOTBALL_NFL,
    )

    TEAM_IDS = {
        RESOURCE_SPORTS_BASEBALL_MLB: {
            'BAL': 1,
            'BOS': 2,
            'LAA': 3,
            'CHW': 4,
            'CLE': 5,
            'DET': 6,
            'KC': 7,
            'MIL': 8,
            'MIN': 9,
            'NYY': 10,
            'OAK': 11,
            'SEA': 12,
            'TEX': 13,
            'TOR': 14,
            'ATL': 15,
            'CHC': 16,
            'CIN': 17,
            'HOU': 18,
            'LAD': 19,
            'WSH': 20,
            'NYM': 21,
            'PHI': 22,
            'PIT': 23,
            'STL': 24,
            'SD': 25,
            'SF': 26,
            'COL': 27,
            'MIA': 28,
            'ARI': 29,
            'TB': 30
        },
        RESOURCE_SPORTS_FOOTBALL_NFL: {
            'ATL': 1,
            'BUF': 2,
            'CHI': 3,
            'CIN': 4,
            'CLE': 5,
            'DAL': 6,
            'DEN': 7,
            'DET': 8,
            'GB': 9,
            'TEN': 10,
            'IND': 11,
            'KC': 12,
            'OAK': 13,
            'STL': 14,
            'MIA': 15,
            'MIN': 16,
            'NE': 17,
            'NO': 18,
            'NYG': 19,
            'NYJ': 20,
            'PHI': 21,
            'ARI': 22,
            'PIT': 23,
            'SD': 24,
            'SF': 25,
            'SEA': 26,
            'TB': 27,
            'WSH': 28,
            'CAR': 29,
            'JAC': 30,
            'BAL': 33,
            'HOU': 34,
        }
    }

    def __init__(self, api_key, resource,
                 urlroot='http://api.espn.com', version='v1'):
        self.api_key = api_key
        self.urlroot = urlroot
        self.version = version
        if not resource in Api.RESOURCES:
            raise ValueError("Invalid resource")
        self.resource = resource
        self.enables = ['venues']

    def _request(self, method):
        url = ''.join([self.urlroot, '/',
                       self.version, '/',
                       self.resource, '/',
                       method,
                       '?apikey=', self.api_key,
                       '&enable=', ','.join(self.enables)])
        logger.debug("Making request to %s" % url)
        r = requests.get(url)
        response = json.loads(r.text)
        return response

    def teams(self):
        ''' Return all teams as a list of Team objects'''
        method = 'teams'
        response = self._request(method)
        teams = []
        data = response['sports'][0]['leagues'][0]
        for raw_team in data['teams']:
            teams.append(Team(raw_team))
        return teams

    def team(self, abbr=None, id=None):
        ''' Lookup a team by abbreviation, or by id e.g. API.team(abbr='NYY') or API.team(id=1) '''
        team_id = id
        if abbr and abbr in Api.TEAM_IDS[self.resource]:
            team_id = Api.TEAM_IDS[self.resource][abbr]
        if team_id is None:
            raise ValueError("Invalid id or abbr: [abbr] = " + abbr + ", [id] = " + id)
        method = ''.join(['teams/', str(team_id)])
        response = self._request(method)
        data = response['sports'][0]['leagues'][0]
        return Team(data['teams'][0])

    def athlete(self, id):
        method = 'athletes/%s' % id
        response = self._request(method)
        return Athlete(response['sports'][0]['leagues'][0]['athletes'][0])

    def news(self):
        ''' Top news '''
        method = 'news'
        response = self._request(method)
        news = []
        for raw_news in response['headlines']:
            news.append(News(raw_news))
        return news

    def team_news(self, abbr=None, id=None):
        ''' News for a specific team '''
        team_id = id
        if abbr and abbr in Api.TEAM_IDS[self.resource]:
            team_id = Api.TEAM_IDS[self.resource][abbr]
        if team_id is None:
            raise ValueError("Invalid id or abbr: [abbr] = " + abbr + ", [id] = " + id)
        method = 'teams/%s/news' % team_id
        response = self._request(method)
        news = []
        for raw_news in response['headlines']:
            news.append(News(raw_news))
        return news

    def event_score(self, event_id):
        ''' Scores data for a given eventid '''
        method = ''.join(['events/', str(event_id)])
        response = self._request(method)
        scores = []
        data = response['sports'][0]['leagues'][0]['events'][0]
        for raw_scores in data['competitions']:
            scores.append(EventScore(raw_scores))
        return scores[0]
