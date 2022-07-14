from itertools import islice
from random import choice


class Die:
    """
    Object class of a die, can choose amount of sides upon initilization (=<20).

    """

    def __init__(self, n: int = 6) -> None:
        total_amount_of_sides = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
        }

        self.sides = dict(islice(total_amount_of_sides.items(), n))

    def __repr__(self) -> str:
        return f"This is a {len(self.sides)}-sided die."

    def roll(self, n: int = 1) -> list[str]:
        """
        Rolls the die
        """
        results = []
        for _ in range(n):
            results.append(choice(list(self.sides.values())))

        return results


def main():
    """
    excecutable part of script.
    """
    die = Die()
    print(die)


if __name__ == "__main__":
    main()
