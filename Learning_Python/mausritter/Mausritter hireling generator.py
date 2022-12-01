# Mausritter hireling generator
import random

import pandas as pd

import mouse_lists as ml


def roll_dice(sides: int, n: int) -> list:
    """roll dice, return results"""

    # generate empty list of values
    result = []

    # for each die roll:
    for _ in range(n):
        # roll a random integer between 1 and total amount of sides, add to list
        result.append(random.randint(1, sides))

    # return list of die rolls
    return result


def hireling_profession(settlement_size: int = 3) -> int:
    """
    take a job from list of jobs randomly depending on size of mouse settlement, smaller settlements have less advanced professionals.

    1: small settlement, village
    2: medium settle

    0. "Torchbearer",
    1. "Labourer",
    2. "Tunnel Digger",
    3. "Armourer / Blacksmith",
    4. "Local Guide",
    5. "Mouse-at-arms",
    6. "Scholar",
    7. "Knight",
    8. "Interpreter",

    """

    # if small settlement
    if settlement_size == 1:
        # get job up to "local guide"
        i = random.randint(0, 4)

    # if medium settlement
    elif settlement_size == 2:
        # get job up to Mouse-at-arms
        i = random.randint(0, 5)

    # if larger settlement
    else:
        # get any profession
        i = random.randint(0, len(ml.job))

    # return index for job, number of sides to the die for amount of available ones, and daily wage
    return i


def generate_hireling(profession: int = hireling_profession()) -> None:
    """generates [NUMBER] of hirelings with job in "profession", random stats, names, and look."""

    # depending on type of job, different amounts of available hirelings can be found
    amount = roll_dice(sides=ml.Number[profession], n=1)

    # for each found hireling
    for i in range(amount[0]):

        # first make one hireling
        if i == 0:
            # create hireling with random stats
            hireling = pd.DataFrame(
                {
                    "Name": [
                        f"{random.choice(ml.first_name)} {random.choice(ml.last_name)}"
                    ],
                    "Look": [
                        f"{ml.coat_pattern[i]}, {ml.coat_color[i]}, and {ml.physical_detail[i]}"
                    ],
                    "Disposition": [random.choice(ml.Birthsign)],
                    "Job": [ml.job[profession]],
                    "Wage/day [pips]": [ml.Wage[profession]],
                    "HP": [sum(roll_dice(6, 1))],
                    "STR": [sum(roll_dice(6, 2))],
                    "DEX": [sum(roll_dice(6, 2))],
                    "WIL": [sum(roll_dice(6, 2))],
                },
            )
        else:
            # then add more hirelings to df according to amount
            hireling = pd.concat(
                [
                    hireling,
                    pd.DataFrame(
                        {
                            "Name": [
                                f"{random.choice(ml.first_name)} {random.choice(ml.last_name)}"
                            ],
                            "Look": [
                                f"{random.choice(ml.coat_pattern)}, {random.choice(ml.coat_color)}, and {random.choice(ml.physical_detail)}"
                            ],
                            "Disposition": [random.choice(ml.Birthsign)],
                            "Job": [ml.job[profession]],
                            "Wage/day [pips]": [ml.Wage[profession]],
                            "HP": [sum(roll_dice(6, 1))],
                            "STR": [sum(roll_dice(6, 2))],
                            "DEX": [sum(roll_dice(6, 2))],
                            "WIL": [sum(roll_dice(6, 2))],
                        }
                    ),
                ],
            )

    # print all generated hirelings
    print(hireling.T)


if __name__ == "__main__":
    """
    0. "Torchbearer",
    1. "Labourer",
    2. "Tunnel Digger",
    3. "Armourer / Blacksmith",
    4. "Local Guide",
    5. "Mouse-at-arms",
    6. "Scholar",
    7. "Knight",
    8. "Interpreter",
    """
    generate_hireling()
