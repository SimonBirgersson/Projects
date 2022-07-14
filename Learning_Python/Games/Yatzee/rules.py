from unicodedata import category

from dice import Die


class Rules:
    """
    Rules for the game of Yatzee.

    """

    def __init__(self) -> None:
        pass

    def get_value(self, result: list[str]) -> list[int]:
        """
        Gets the value in int for dice roll.
        """
        value = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "twenty": 20,
        }
        return list(value[i] for i in result)

    def reroll(self, results: list[str], choice: list[int], die: Die) -> list[str]:
        """
        Let the user reroll what ever dice they want.
        """
        for i in choice:
            # ugly solution to getting just the new string in the list.
            results[i - 1] = die.roll(n=1)[0]
        return results


class ScoreSheet:
    """
    The chart where you track all of your results
    """

    def __init__(self, categories: list[str]) -> None:
        self.cat = categories


def main():
    """
    excecutable part of script.
    """
    cat = [
        "Aces",
        "Twos",
        "Threes",
        "Fours",
        "Fives",
        "Sixes",
        "Total Score",
        "Bonus (upper)",
        "3 of a kind",
        "4 of a kind",
        "Full House",
        "Small straight",
        "Large straight",
        "Yahtzee",
        "Chance",
        "Grand Total",
    ]


if __name__ == "__main__":
    main()
