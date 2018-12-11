"""The play command."""


from json import dumps

from .base import Base


class Play(Base):
    """Play with Pikachu!"""

    def run(self):
        print 'Swirling & twirling ~'
        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
