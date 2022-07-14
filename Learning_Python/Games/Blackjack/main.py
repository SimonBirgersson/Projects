from Learning_Python.casino.french_deck import Deck, Hand

from CLI import CLI
from game import Game
from rules import Rules


def main():
    """
    Here is where the game is assembled.
    """
    deck = Deck()
    game = Game(ui=CLI(), rules=Rules(), deck=deck)
    game.start_up()

    while True:
        result = game.turn(hand=Hand(deck), house_hand=Hand(deck), deck=deck)

        if game.end_of_game(result) is True:
            break


if __name__ == "__main__":
    main()
