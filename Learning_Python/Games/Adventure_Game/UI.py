from secrets import choice

from Learning_Python.Adventure_Game.hero import Hero
from Learning_Python.Adventure_Game.Monster import Attack, Monster


class UI:
    """Terminal UI for adventure game"""

    def __init__(self) -> None:
        pass

    def battle_start(self, enemies: list[Monster]) -> str:
        """Prompt at start of battle"""

        print(f"you are attacked by {len(enemies)} monsters:\n")
        for i in enemies:
            print(f"{i}\n")

    def battle_situation(self, monsters: list[Monster], hero: Hero):
        """present user with users current health and enemies current health"""

        output = "──────────────────────────────────────────────────────────\n"

        output += f"You:\n{hero.name} ({hero.health}/{hero.max_health} hp)\n"
        output += f"current weapon: {hero.weapon}\n\n"

        for i, enemy in enumerate(monsters):
            output += f"{i+1}. {enemy}\n"

        print(output)

    def battle_turn_choice(self) -> int:
        """
        turn prompt for player choices during combat turn

        returns choice as string
        """

        while True:
            print("┌─────────────────────────────┐")
            print("│  What do you choose to do?  │")
            print("│  1. Fight\t2. Item       │")
            print("│  3. Run\t4. Pass       │")
            print("└─────────────────────────────┘")

            choice = input()

            if choice is "1" or "2" or "3" or "4":
                return int(choice)
            else:
                print("Not a valid option.")
                continue

    def choice_result(self, choice: int) -> None:
        """The prompt for the users choice"""
        choices = {
            1: "you choose to fight!\n",
            2: "you chose to use an item.\n",
            3: "You chose to run, you got away safely.\n",
            4: "You chose to pass.\n",
        }

        print(choices[choice])

    def choose_target(self, monsters: list[Monster]) -> int:
        """user chooses which monster to attack"""
        print("Which enemy would you like to attack?\n")

        for i, enemy in enumerate(monsters):
            print(f"{i+1}. {enemy.name}")

        choice = input()
        while True:
            if choice is "1" or "2":
                return int(choice) - 1
            else:
                print("Not a valid choice.")

    def hero_attack(self, target: Monster, hero: Hero) -> None:
        """Prompt for attacking the chosen monster"""
        print(f"you attack {target.name} for {hero.damage()} damage!\n")

    def monster_attack(self, monster: Monster, attack: Attack):
        """prompt for what the monster does"""
        print(
            f"Monster {monster.name} used {attack.name}! it deals {attack.damage} damage.\n"
        )
