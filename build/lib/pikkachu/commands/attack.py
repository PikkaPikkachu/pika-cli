from json import dumps
import random
from .base import Base
from pyfiglet import Figlet


l = ["electrocute", "thunderbolt", "thundershock", "thunder wave", "wild charge"
        "thunder", "charge beam", "electro ball", "tail whip", "thunder punch"]

class Attack(Base):
    """Pikachu, show your moves!"""

    def run(self):
        f = Figlet(font='slant')
        print f.renderText(l[random.randint(0,len(l)-1)])
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        #print "Pikachu has opted for ", l[random.randint(0,len(l)-1)], " attack"
