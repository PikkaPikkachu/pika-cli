# -*- coding: utf-8 -*-
"""The hello command."""


from json import dumps

from .base import Base

pikachu_draw = '''
/\︿╱\ \n
\\0_ 0 /╱\╱
\▁︹_/
'''
class Hello(Base):
    """Say hello, world!"""
    
    def run(self):
        print 'Pika, pika ~'
        print pikachu_draw
        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
