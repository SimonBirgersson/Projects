from dataclasses import dataclass, field, fields
from importlib.metadata import metadata
from math import asin, cos, radians, sin, sqrt
from os import system
from random import sample
from typing import List

system("clear")

# Simple example of a dataclass
@dataclass  # this is called decorator
class Enzyme:  # the decrator makes this class a data class
    """It would be nice to store data from assays like this, sort of like matlab structures"""

    # these are fields, with type hints
    name: str
    abs: list
    dil_factor: float = 1.0  # default value


BpMan5A = Enzyme("BpMan5A", [0.5, 0.6, 0.55])
# print(BpMan5A)

# positional data
@dataclass
class Position:
    """Class of positional data, with name of the place, longitude, and latitude."""

    name: str
    # field() allows for modifications beyind default value, for instance add metadata
    lon: float = field(default=0.0, metadata={"unit": "degrees"})
    lat: float = field(default=0.0, metadata={"unit": "degrees"})

    # you can add methods to your dataclass, this calculates the distance to another position
    def distance_to(self, other):
        """Calculates the distance to another position in km by the haverine formula"""
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )
        return 2 * r * asin(sqrt(h))


# examples applications of position class
oslo = Position("Oslo", 10.8, 59.9)
vancouver = Position("Vancouver", -123.1, 49.3)

# calculate distance between oslo and vancouver
print(f"The distance between oslo and vancouver is {oslo.distance_to(vancouver)} km.")

# fields() function can fetch metadata
lat_unit = fields(Position)[2].metadata["unit"]  # returns "degrees"


# deck of cards example

# you can add parameters to the decorator, this class is a single playing card
@dataclass(order=True)  # allows comparison between instances of cards
class PlayingCard:
    """Supported decorator parameters:
    init: Add .__init__() method? (Default is True.)
    repr: Add .__repr__() method? (Default is True.)
    eq: Add .__eq__() method? (Default is True.)
    order: Add ordering methods? (Default is False.)
    unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
    frozen: If True, assigning to fields raise an exception. (Default is False.)"""

    # these fields make the card suit and rank
    rank: str
    suit: str

    # field that sorts the cards according to value
    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit)

    # user friendly representation of the card, f-string of rank and suit
    def __str__(self):
        return f"{self.suit}{self.rank}"


RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # ranks
SUITS = "♣ ♢ ♡ ♠".split()  # unicode symbols


# function for making a complete deck with RANKS and SUITS
def make_french_deck():
    """generate a french deck."""
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


# Deck of cards class
@dataclass
class Deck:
    """Deck of cards"""

    # type of cards are lists of playing cards with default value = french deck
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    # user friendly representation of each card
    def __repr__(self):
        cards = ", ".join(
            f"{c!s}" for c in self.cards
        )  # forces string representation of each playing card
        return f"{self.__class__.__name__}({cards})"


# shows sorted deck of cards
print(Deck(sorted(make_french_deck())))

# draw a reandom poker hand
print(Deck(sample(make_french_deck(), k=5)))


""""The field() specifier is used to customize each field of a data class individually. You will see some other examples later. For reference, these are the parameters field() supports:

default: Default value of the field
default_factory: Function that returns the initial value of the field
init: Use field in .__init__() method? (Default is True.)
repr: Use field in repr of the object? (Default is True.)
compare: Include the field in comparisons? (Default is True.)
hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
metadata: A mapping with information about the field"""
