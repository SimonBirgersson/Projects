from Learning_Python.casino.french_deck import Deck, Hand, draw


# rules of blackjack
class Rules:
    """
    List of game actions possbile when playing the game.
    """

    def hit(self, hand: Hand, deck: Deck):
        """
        To 'Hit' is to ask for another card.
        """
        return draw(hand=hand, deck=deck, amount=1)

    def stand(self):
        """
        To 'Stand' is to hold your total and end your turn.
        """
        raise NotImplementedError

    def double(self):
        """
        Doubling is like a hit, only the bet is doubled and you only get one more card.
        """
        raise NotImplementedError

    def split(self) -> list[Hand]:
        """
        Split can be done when you have two of the same card - the pair is split into two hands.

        Splitting also doubles the bet, because each new hand is worth the original bet.

        You can only double/split on the first move, or first move of a hand created by a split.

        You cannot play on two aces after they are split.
        """
        raise NotImplementedError

    def check_win(self, hand: Hand) -> bool:
        """
        Check if the player has blackjack
        """
        return bool(hand.value == 21)

    def check_bust(self, hand: Hand) -> bool:
        """
        check if the player busts.
        """
        return bool(hand.value > 21)

    def compare_hands(self, hand1: Hand, hand2: Hand) -> bool:
        """compare two hands in the game, returns True if hand 1 is strictly higher than hand2."""
        return bool(hand1.value > hand2.value)
