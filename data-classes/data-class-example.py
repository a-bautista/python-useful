from collections import namedtuple
from dataclasses import dataclass, field
from math import asin, cos, radians, sin, sqrt 
from typing import List
from pympler import asizeof

def main():
    
    
    # A named tuple is the previous to the data class
    NamedTupleCard = namedtuple('NameTupleCard', ['rank','suit'])
    
    # Set the NamedTupleCard
    queen_of_hearts = NamedTupleCard('Q','Hearts')
    print(queen_of_hearts.rank)
    
    # Initialize a data class
    @dataclass
    class Position:
        name: str
        lon: float
        lat: float

    pos = Position('Oslo',10.8, 59.9)
    print(f'{pos.name} is at {pos.lat} N, {pos.lon} E')

    '''What's the benefit of a data class? 
    A data class is a regular Python class except for the fact that a class has model methods like .__init__(),
    .__repr__(), .__eq__() whereas a data class does not require these mandatory methods.'''


    class PositionSetStandardValues:
        def __init__(self, name, lon, lat):
            self.name = name
            self.lon  = lon
            self.lat  = lat

    @dataclass
    class PositionSetStandardValues:
        name: str
        lon: float = 0.0
        lat: float = 0.0

        

    @dataclass
    class PlayingCard:
        rank: str
        suit: str

    @dataclass
    class Deck:
        cards: List[PlayingCard]

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = '\u2660 \u2663 \u2665 \u2666'.split() #UTF-8 icons

    def make_french_deck():
        return [PlayingCard(r, s) for s in SUITS for r in RANKS]

    #print(Deck())

    @dataclass
    class Deck:

        cards: List[PlayingCard] = field(default_factory=make_french_deck)
        def __repr__(self):
            cards = ', '.join(f'{c!s}' for c in self.cards)
            return f'{self.__class__.__name__}({cards})'

    print(Deck())
    # The field specifier is used to customize each data class individually,
    # that is, we can have multiple decks of different symbols.

    # Inheritance with data classes

    @dataclass
    class Capital(Position):
        country: str
    
    Capital('Oslo', 10.8, 59.9, 'Norway')

    # Re-ordering inheritance with data classes

    @dataclass
    class Position:
        name: str
        lon: float = 0.0
        lat: float = 0.0

    @dataclass
    class Capital(Position):
        country: str = 'Unknown'
        lat : float = 40.0

    # the data class looks for name, lon, lat and country
    # and Berlin is contained in name
    Capital('Berlin', country='Germany') 

    # Optimizing data classes

    # you can use slots for classes to make them faster and use less memory

    @dataclass
    class SlotPosition:
        __slot__ = ['name', 'lon', 'lat']
        name: str
        lon: float
        lat: float


    @dataclass
    class SimplePosition:
        name: str
        lon: float
        lat: float

    simple = SimplePosition('London', -0.1, 51.5)
    slot = SlotPosition('Madrid', -3.7, 40.4)
    print(asizeof.asizesof(simple, slot))


if __name__ == "__main__":
    main()

