from ast import Raise
from random import randrange

import numpy as np
from Learning_Python.Adventure_Game.hero import Hero, Weapon
from Learning_Python.Adventure_Game.Monster import Attack, Monster
from Learning_Python.Adventure_Game.UI import UI


class Battle:
    """a pokemon type battle ensues"""

    def __init__(self, monsters: list([Monster]), UI: UI, hero: Hero) -> None:
        self.enemies = monsters
        self.UI = UI
        self.hero = hero

    def turn(self):
        """The battle turn, user takes one action and each enemy attacks once."""

        # Battle starts
        self.UI.battle_start(self.enemies)

        # loop game turns until user runs or one side is dead
        while True:
            # present current situation and ask user what to do
            self.UI.battle_situation(self.enemies, self.hero)
            choice = self.UI.battle_turn_choice()
            self.UI.choice_result(choice)

            # fight
            if choice == 1:
                # if fighting one enemy
                if len(self.enemies) == 1:
                    target = 0

                # choose target if fighting more than one enemy
                else:
                    target = self.UI.choose_target(self.enemies)

                # deal damage to target
                self.UI.hero_attack(self.enemies[target], hero=self.hero)
                self.enemies[target].health -= self.hero.damage()

            # use item
            if choice == 2:
                raise NotImplementedError

            # run away, ends the battle
            if choice == 3:
                break

            # pass the turn over to monsters
            if choice == 4:
                pass

            # each enemy attacks once
            for enemy in self.enemies:
                # choose random attack
                used_attack = enemy.attack()
                self.UI.monster_attack(enemy, used_attack)
                self.hero.health -= used_attack.damage


def main():
    """Test Code Here"""

    # Create a hero
    hero = Hero(name="Wizard", max_health=40)
    sword = Weapon(name="sword", damage=2)

    hero.pick_up_weapon(sword)

    # Monster Attacks
    bite = Attack(name="Bite", damage=randrange(3))
    kick = Attack(name="kick", damage=randrange(2, 4))
    scratch = Attack(name="scratch", damage=1)
    cuteness = Attack(
        name="cuteness", damage=np.random.choice(a=[-1, 10], p=[0.9, 0.1])
    )

    # Monsters
    Selma = Monster(
        name="Selma",
        monster_type="feline",
        max_health=9,
        attacks=[cuteness, scratch, bite],
    )

    ghost = Monster(
        name="Ghost", monster_type="undead", max_health=4, attacks=[scratch]
    )

    battle = Battle([Selma, ghost], hero=hero, UI=UI())
    battle.turn()


if __name__ == "__main__":
    main()
