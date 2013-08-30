holycow
=======
A python wrapper for the ESPN API. [Holy cow!](http://en.wikipedia.org/wiki/Phil_Rizzuto)

http://developer.espn.com/docs

NOTE: Still a work-in-progress. Better exception handling to come...

Requirements
-----------------
- Python 2.6 to 2.7
- requests

Installation
------------
1) Install the required dependencies using your favorite installer (pip, easy_install)

    pip install -r requirements.txt

2) Use Git to clone the repository from Github
and install it manually:

    git clone https://github.com/mguarascio/holycow.git
    python setup.py install

Examples
--------
    # Initialize API
    >>> from holycow import Api
    >>> api = Api('your_api_key', Api.RESOURCE_SPORTS_BASEBALL_MLB)

    # Get all teams 
    >>> [team.name for team in api.teams()]
    [u'Orioles', u'Red Sox', u'Angels', u'White Sox', u'Indians', u'Tigers', u'Royals', u'Brewers', u'Twins', u'Yankees', u'Athletics', u'Mariners', u'Rangers', u'Blue Jays', u'Braves', u'Cubs', u'Reds', u'Astros', u'Dodgers', u'Nationals', u'Mets', u'Phillies', u'Pirates', u'Cardinals', u'Padres', u'Giants', u'Rockies', u'Marlins', u'Diamondbacks', u'Rays']
 
    # Get a specific team's data
    >>> team = api.team(abbr='NYY')
    >>> print ''.join([team.location, ' ', team.name, ': ', team.venue])
    New York Yankees: Yankee Stadium

    # Get all top news 
    >>> topnews = api.news()
    >>> print [news.headline for news in topnews]
    [u'Orioles promote Kevin Gausman ', u'Brandon Phillips gets moved up', u'David Price ready for some football ', u'Pads recall Robbie Erlin from Tucson', u'Royals call up Duffy, Hochevar', u'Matt Harvey consulted Roy Halladay', u'Yasiel Puig pulled from game', u'Ryan Raburn lands on DL', u'Suit vs. Curt Schilling can proceed', u"MLB's unfair frequent-flier plans"]
    
    # Get team-specific news
    >>> news = api.team_news('NYY')
    >>> print [story.links['web'] for story in news]
    [{u'href': u'http://espn.go.com/mlb/story/_/id/9614100/long-mlb-umpire-frank-pulli-dies-78?ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/mlb/story/_/id/9567010/despite-biogenesis-how-peds-work-unknown-espn-magazine?ex_cid=espnapi_public'}, {u'href': u'http://scores.espn.go.com/mlb/recap?gameId=330828114&ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/new-york/mlb/story/_/id/9610056/new-york-yankees-sit-robinson-cano-eduardo-nunez-mark-reynolds-starts-second-base?ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/new-york/mlb/story/_/id/9607561/new-york-yankees-robinson-cano-catch-lucky-break?ex_cid=espnapi_public'}, {u'href': u'http://scores.espn.go.com/mlb/recap?gameId=330827114&ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/new-york/mlb/story/_/id/9606909/robinson-cano-new-york-yankees-exits-game-being-hit-pitch-hand?ex_cid=espnapi_public'}, {u'href': u'http://scores.espn.go.com/mlb/recap?gameId=330826114&ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/new-york/mlb/story/_/id/9602941/derek-jeter-returns-lineup-new-york-yankees?ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/mlb/story/_/id/9601244/ichiro-suzuki-hitter-grown-seeds-sown-far-away?ex_cid=espnapi_public'}]
    
    # Get athlete data
    >>> athlete = api.athlete(2352)
    >>> athlete.full_name
    u'Mark Whiten'

    # TODO: get this going...
    # Get a specific game score (requires event_id)
    #score = api.event_score('330330101')
    #print ''.join([score.score, ' ', score.status])
    # {u'Mets': 1, u'Orioles': 7} FINAL
