from random import randrange

import numpy as np


class Attack:
    """a type of attack that a character can do"""

    def __init__(
        self,
        name: str,
        damage,
        status_effect: dict = None,
        attack_chance: float = 1.0,
    ) -> None:

        self.name = name
        self.damage = damage
        self.status_effect = status_effect
        self.chance = attack_chance


class Monster:
    """General monster class"""

    def __init__(
        self,
        name: str,
        monster_type: str,
        max_health: int,
        attacks: list[Attack] = None,
    ) -> None:
        self.name = name
        self.type = monster_type
        self.max_health = max_health
        self.health = max_health
        self.attacks = attacks

    def __repr__(self) -> str:
        """Printable call for class object"""
        return f"{self.name}:\n{self.type} Monster ({self.health}/{self.max_health} hp)"

    def attack(self) -> Attack:
        """The monster attacks!"""
        # used_attack = np.random.choice(self.attacks, self.attacks.chance)
        used_attack = np.random.choice(a=self.attacks)

        return used_attack


def main():
    """Test Code Here"""
    bite = Attack(name="Bite", damage=randrange(3))
    kick = Attack(name="kick", damage=randrange(2, 4))

    zombie = Monster(
        name="Zombie", monster_type="Undead", max_health=3, attacks=[bite, kick]
    )

    attack = zombie.attack()
    print(f"Monster {zombie.name} used {attack.name}! it deals {attack.damage} damage.")


if __name__ == "__main__":
    main()
