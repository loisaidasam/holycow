'''

The ESPN API currently only support getting all players, or player by id.
I'll have to implement a way to search by player's team or player name until
that API is available to the public.
'''

class Athlete(object):
    ''' Stub for player class '''
    def __init__(self, results):
        self.id = results.get('id')
        self.first_name = results.get('firstName')
        self.last_name = results.get('lastName')
        self.full_name = results.get('fullName')
        self.display_name = results.get('displayName')
        self.links = results.get('links', [])
