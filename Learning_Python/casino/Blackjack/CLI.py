from datetime import date

from Learning_Python.casino.french_deck import Card, Deck, Hand, show_hand


class CLI:
    """
    Interface for interacting with the player in blackjack game
    """

    def __init__(self, player_name: str = "you", cpu_name: str = "house") -> None:
        self.player_name = player_name
        self.cpu_name = cpu_name

    def introduction(self) -> None:
        """
        intro to the game. prints logo in .txt file for some flair
        """
        with open(
            "/Users/simon/Documents/Projects/Learning_Python/casino/Blackjack/logo.txt",
            "r",
            encoding="utf-8",
        ) as file:
            print(file.read())
        print("\n\n Hello and welcome to Blackjack! press any key to continue...")
        _ = input()

    def main_menu(self) -> str:
        """
        Let the player look at tutorial or start the game.
        """
        print(
            "MAIN MENU: What would you like to do? \n\n 1. start the game  \n\n 2. tutorial \n\n 3. look at the guestbook"
        )
        # dict with options
        option = {1: "start", 2: "tutorial", 3: "guestbook"}

        # loops until proper choice is presented by user
        while True:
            choice = input()

            # looks for these inputs, then breaks the loop:
            if choice in ("1", "2", "3"):
                break

            # other wise prints this
            print("Not an appropriate choice.")

        # return the str from earlier dict
        return option[int(choice)]

    def tutorial(self) -> None:
        """
        Does the user want a tutorial?
        """
        # prints this huge thing
        return print(
            "\n\nBasic Blackjack Rules:\n------------------------\n"
            "The goal of blackjack is to beat the dealer's hand without going over 21.\n\n"
            "Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.\n\n"
            "Each player starts with two cards, one of the dealer's cards is hidden until the end.\n\n"
            "To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\n\n"
            "If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\n\n"
            "If you are dealt 21 from the start (Ace & 10), you got a blackjack.\n\n"
            "Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.\n\n"
            "Dealer will hit until his/her cards total 17 or higher.\n\n"
            "Doubling is like a hit, only the bet is doubled and you only get one more card.\n\n"
            "Split can be done when you have two of the same card - the pair is split into two hands.\n\n"
            "Splitting also doubles the bet, because each new hand is worth the original bet.\n\n"
            "You can only double/split on the first move, or first move of a hand created by a split.\n\n"
            "You cannot play on two aces after they are split.\n\n"
            "You can double on a hand resulting from a split, tripling or quadrupling you bet.\n\n"
        )

    def get_player_name(self) -> str:
        """
        get the name of the player.
        """

        # records the text entered into the command line
        print("What is your name? enter below:")
        return input()

    def player_turn_message(self, hand: Hand) -> str:
        """
        Player choice for the turn
        """
        # shows the user its current hand
        print("\nIt's your turn and your hand is:")
        print(show_hand(hand.cards))
        print(
            "What would you like to do? \n\n 1. hit \n 2. stand \n 3. split \n 4. double"
        )
        # dict with choices
        option = {1: "hit", 2: "stand", 3: "split", 4: "double"}
        while True:
            choice = input()
            # check for proper responses
            if choice in ("1", "2", "3", "4"):
                break

            print("Not an appropriate choice.")
        return option[int(choice)]

    def action_message(self, option: str, name: str, hand: Hand) -> None:
        """
        returns the appropriate message based on "option"
        """
        # returns the appropriate message based on "option"
        if option == "hit":
            if name == "house":
                return print(f"{name} hits!")  # if hit
            else:
                return print(f"{name} hit. new hand is worth {hand.value}")  # new hand
        elif option == "stand":
            if name == "house":

                # dont tell user value of house hand
                return print(f"{name} choose to stand...")
            else:
                return print(f"{name} choose to stand with a hand worth {hand.value}:")
        elif option == "split":
            return print(f"{name} split their hand and gets:")
        elif option == "double":
            return print(f"{name} double the bet!")
        else:
            raise KeyError

    def house_turn_message(self, hand: Hand) -> None:
        """
        House message during their turn.
        """
        print("\nIt's the house's turn and its hand is:")

        # don't show entire hand for house
        print(show_hand(hand.cards, number_of_cards=1))

    def blackjack_message(
        self,
    ) -> None:
        """
        Announce the winner of the game
        """
        return print(f"BlackJack!")

    def bust_message(self) -> None:
        """
        Announce game loss
        """
        return print(f"Bust!")

    def compare_message(
        self, player_name: str, house_name: str, player_hand: Hand, house_hand: Hand
    ) -> None:
        """
        if both parties chose to stand whoever is closest to 21 wins...
        """
        return print(
            f"{player_name} got a hand of {player_hand.value} and {house_name} got {house_hand.value}."
        )

    def winner_message(self, win: tuple([str, bool])) -> None:
        """
        tells who won or who lost.
        """
        if win[1] is True:
            return print(f"{win[0]} won the game.")
        else:
            return print(f"{win[0]} lost the game.")

    def replay_message(self) -> str:
        """
        Would you like to play again?
        """
        print(
            "Would you like to play again? \n\n 1. yes \n\n 2. no (quit the game) \n\n 3. sign the guest book."
        )
        option = {1: "yes", 2: "no", 3: "guestbook"}
        while True:
            choice = input()
            if choice in ("1", "2", "3"):
                break
            print("Not an appropriate choice.")
        return option[int(choice)]

    def guest_book_entry(self, win: tuple([str, bool])) -> str:
        """
        the line that gets entered into the guest book.
        """
        return f"{win[0]}   {win[1]}    {date.today()}\n\n"


def main():
    """
    Just testing
    """
    ui = CLI()
    ui.introduction()


if __name__ == "__main__":
    main()
