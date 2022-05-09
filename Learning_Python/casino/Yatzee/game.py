from dice import Die
from rules import Rules
from ui import UI


class Game:
    """
    These is where the game happens.
    """

    def __init__(
        self,
        dice: Die,
        rules: Rules,
        ui: UI,
        max_rerolls: int = 2,
        number_of_dice: int = 5,
    ) -> None:

        # get access to methods from within these classes
        self.dice = dice
        self.rules = rules
        self.ui = ui

        # if you want to change the rules for some reason.
        self.max_turn_count = max_rerolls
        self.n_dice = number_of_dice

    def turn(self) -> list[str]:
        """
        this is the game turn
        """
        results = self.dice.roll(n=self.n_dice)

        # initilize turn count before start of loop
        turn_count = 0
        while True:
            # messages at beginning of turn
            self.ui.roll_message(results)
            self.ui.turn_option(count=turn_count)

            option = input()

            # if the choice is keep, the turn ends.
            if option == "1":
                print("nice!")
                break

            # the user can reroll any dice up to two times
            elif option == "2":

                results = self.rules.reroll(
                    results=results, choice=self.ui.reroll_choice(), die=self.dice
                )

                # checks if the round is over, otherwise return to top of loop.
                turn_count = turn_count + 1
                if turn_count >= self.max_turn_count:
                    break
                else:
                    continue
            else:
                print("Wrong option")
                continue

        # the turn is over and the user needs to deposit their results into the chart.
        self.ui.end_of_turn_message(results=results)
        return results


def main():
    """
    excecutable part of script.
    """

    game = Game(dice=Die(n=6), rules=Rules(), ui=UI())

    results = game.turn()


if __name__ == "__main__":
    main()
