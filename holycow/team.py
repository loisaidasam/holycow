

class Team(object):
    def __init__(self, results):
        self.id = results['id']
        self.name = results['name']
        self.color = results['color']
        self.abbreviation = results['abbreviation']
        self.location = results['location']
        self.links = results['links']
        self.venue = results['venues'][0]['name']

    def __unicode__(self):
        return u'%s (id=%s)' % (self.name, self.id)

    def __str__(self):
        return self.__unicode__()
