class UI:
    """
    Messages for the end user goes here.
    """

    def __init__(self) -> None:
        pass

    def roll_message(self, result) -> None:
        """
        The message that the user gets after rolling one or more dice.
        """
        # start of message
        print("---------------------------------------")
        if len(result) == 1:
            print("You rolled 1 die and got:")
        else:
            print(f"You rolled {len(result)} dice and got:")
        for i, _ in enumerate(result):
            print(f"{i+1}: {result[i]}")
        print("---------------------------------------")
        # end of message

    def turn_option(self, count: int):
        """
        Choices for the user to do:
        """
        return print(
            f"Turn {count+1}: What would you like to do?\n 1. keep \n 2. reroll some dice"
        )

    def reroll_choice(self) -> list[int]:
        """
        explains how to menu the rerolling
        """
        print(
            "please enter the number of the dice you whish to re-roll seperated by commas.\n (for instance '1,2,3'"
        )
        return list(int(i) for i in input().split(sep=","))

    def end_of_turn_message(self, results):
        """
        after the turn is over.
        """

        print("It's the end of the turn and you have:")
        self.roll_message(result=results)
        print("Where would you like to put your results?")
