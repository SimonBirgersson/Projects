from Learning_Python.casino.french_deck import Deck, Hand

from CLI import CLI
from rules import Rules


class Game:
    """
    This is where the game goes
    """

    def __init__(self, ui: CLI, rules: Rules, deck: Deck):
        self.ui = ui
        self.rules = rules
        self.deck = deck

    def start_up(self):
        """
        Intro, name choice and main menu.
        """

        # intro message
        self.ui.introduction()

        # get player name
        # player_name = self.ui.get_player_name()

        # loop main menu until player wishes to start the game.
        while True:
            choice = self.ui.main_menu()
            if choice == "start":
                break
            elif choice == "tutorial":
                self.ui.tutorial()
                continue
            elif choice == "guestbook":
                raise NotImplementedError

    def turn(
        self,
        hand: Hand,
        house_hand: Hand,
        deck: Deck,
        player_name: str = "you",
        house_name: str = "house",
    ) -> tuple([str, bool]):
        """
        let the player choose what to do on their turn, and do it.
        """
        stand = False

        while True:

            if stand is False:
                choice = self.ui.player_turn_message(hand)

                if choice == "hit":
                    hand = self.rules.hit(hand, deck)

                    self.ui.action_message(option=choice, name=player_name, hand=hand)

                    if self.rules.check_bust(hand):
                        self.ui.bust_message()
                        win = False
                        return (player_name, win)

                    elif self.rules.check_win(hand):
                        self.ui.blackjack_message()
                        win = True
                        return (player_name, win)

                    else:
                        pass

                if choice == "stand":
                    self.ui.action_message(option=choice, name=player_name, hand=hand)

                    if self.rules.check_bust(hand):
                        self.ui.bust_message()
                        win = False
                        return (player_name, win)

                    elif self.rules.check_win(hand):
                        self.ui.blackjack_message()
                        win = True
                        return (player_name, win)

                    else:
                        stand = True

                if choice == "split":
                    self.ui.action_message(option=choice, name=player_name, hand=hand)
                    self.rules.split()

                if choice == "double":
                    self.ui.action_message(option=choice, name=player_name, hand=hand)
                    self.rules.double()

            # House should have some basic behaviour that it follows.

            self.ui.house_turn_message(house_hand)
            if house_hand.value < 17:
                house_hand = self.rules.hit(house_hand, deck)

                self.ui.action_message(option="hit", name=house_name, hand=house_hand)

                if self.rules.check_bust(house_hand):
                    self.ui.bust_message()

                    win = False
                    return (house_name, win)

                elif self.rules.check_win(house_hand):
                    self.ui.blackjack_message()

                    win = True
                    return (house_name, win)

                else:
                    continue

            if house_hand.value >= 17:
                self.ui.action_message(option="stand", name=house_name, hand=house_hand)

                if self.rules.check_bust(house_hand):
                    self.ui.bust_message()

                    win = False
                    return (house_name, win)

                elif self.rules.check_win(house_hand):
                    self.ui.blackjack_message()

                    win = True
                    return (house_name, win)

                elif stand is True:
                    self.ui.compare_message(
                        player_name=player_name,
                        house_name=house_name,
                        player_hand=hand,
                        house_hand=house_hand,
                    )
                    return (
                        "player",
                        self.rules.compare_hands(hand1=hand, hand2=house_hand),
                    )
                else:
                    continue

    def end_of_game(self, win: tuple([str, bool])) -> bool:
        """
        If somebody won, end the game.
        """
        self.ui.winner_message(win)

        while True:
            choice = self.ui.replay_message()
            if choice == "yes":
                print("nice choice!")
                return False

            elif choice == "no":
                print("thank you for playing.")
                return True

            elif choice == "guestbook":
                raise NotImplementedError
                # continue after signing name into .txt file with date and result
            else:
                print("not a valid option")
                continue


def main():
    """
    just testing
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
