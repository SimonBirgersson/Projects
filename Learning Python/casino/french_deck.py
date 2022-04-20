# function for cards, deck etc. 220418
from random import shuffle


class Card(object):
    """
    class for one card of a french deck, with suit, rank, and value for blackjack, ace high by default.
    """

    # this is the value of each card in blackjack, assumes aces high for now.
    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    def __init__(self, suit, rank) -> None:
        self.rank = rank
        self.suit = suit
        self.value = self.card_values[self.rank]

    def __repr__(self):
        return f"{self.suit}{self.rank}"


def show_hand(cards: list[Card], return_string=True, number_of_cards: int = None):
    """
    Colorful way of showing the cards in your hand
    """

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    if number_of_cards:

        cards = cards[:number_of_cards]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == "10":  # ten is the only one who's rank is 2 char long
            space = ""  # if we write "10" on the card that line will be 1 char to long
        else:
            space = " "  # no "10", we use a blank space to will the void

        # add the individual card on a line by line basis
        lines[0].append("┌─────────┐")
        lines[1].append(
            f"│{card.suit}{card.rank}{space}      │"
        )  # use two {} one for char, one for space or char
        lines[2].append("│         │")
        lines[3].append("│         │")
        lines[4].append(f"│    {card.suit}    │")
        lines[5].append("│         │")
        lines[6].append("│         │")
        lines[7].append(f"│      {space}{card.rank}{card.suit}│")
        lines[8].append("└─────────┘")

    result = []
    for index, line in enumerate(lines):
        result.append("".join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return "\n".join(result)
    else:
        return result


class Deck(object):
    """object containing card objects, allows for drawing shuffling etc."""

    def generate_deck(self, n):
        """
        one of each card in a french deck, generate dict of 1 shuffled deck by default.
        """

        # creates empty dictionary
        cards = {}

        # for each possible rank of card, x 4 x number of decks
        for i, rank in enumerate(
            ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4 * n
        ):
            # change suit every fourteen cards
            if i < 12 * n:
                suit = "♠"
            elif 13 * n <= i < 26 * n:
                suit = "♡"
            elif 26 * n <= i < 39 * n:
                suit = "♢"
            elif 39 * n <= i:
                suit = "♣"

            # generates the card object
            cards[i] = Card(suit, rank)
        # return each of the cards in a dictionary
        return cards

    def shuffle(self) -> None:
        """shuffles the order of the deck, and stores it in self.deck"""

        # fetches a list of the keys for each card object in the deck
        key_list = list(self.deck.keys())

        # randomize the order of the list
        shuffle(key_list)

        # generate a dictionary of the shuffled deck
        shuffled_deck = dict()

        # for each card
        for key in key_list:
            # create the shuffled deck, card by card
            shuffled_deck[key] = self.deck[key]

        # this is the deck moving forward
        self.deck = shuffled_deck

    def draw(self, amount):
        """
        draw n cards from the top of the deck, returns list of card objects
        """

        # create empty list of cards to draw
        cards = []

        # check if there is enough cards to draw
        if amount > len(self.deck):
            return print("Not enough cards to draw left in the deck!")

        # for each draw:
        for _ in range(amount):

            # add the top card of the deck to the list of cards to draw
            cards.append(self.deck[list(self.deck.keys())[0]])

            # remove the top card from the deck
            del self.deck[list(self.deck.keys())[0]]

        # return the list of card objects
        return cards

    # starting variables for the deck
    def __init__(self, shuffled: bool = True, amount_of_decks: int = 1) -> None:
        self.deck = self.generate_deck(n=amount_of_decks)  # create deck.
        if shuffled:
            self.shuffle()  # shuffle it initially

    # how the deck is presented when called:
    def __repr__(self) -> str:

        # shows the contents if it has any cards in it
        if self.deck:
            return f"{[self.deck[i] for i in self.deck]}"
        # otherwise just show this message
        else:
            return "Deck is empty..."

    # how the length of the deck is represented
    def __len__(self) -> int:
        return len(self.deck)


class Hand(object):
    """group or cards from hand"""

    def __init__(
        self,
        deck: Deck,
        size: int = 2,
    ) -> None:

        self.cards: list[Card] = deck.draw(size)
        self.deck: Deck = deck
        self.value = sum([self.cards[i].value for i in range(len(self.cards))])

    def draw(self, amount: int):
        """
        Draw amount of cards from the deck and add it to your hand.
        """

        # check if there is enough cards to draw
        if amount > len(self.deck):
            return print("Not enough cards to draw left in the deck!")

        self.cards = self.cards + self.deck.draw(amount)

    def __repr__(self) -> str:
        return show_hand(self.cards)


def main():
    """
    actual function
    """
    deck = Deck()  # create deck
    print(len(deck))

    hand = Hand(deck=deck)  # create hand of 2 from deck
    print(show_hand(hand.cards))
    print(len(deck))
    print(hand.value)


if __name__ == "__main__":
    main()
