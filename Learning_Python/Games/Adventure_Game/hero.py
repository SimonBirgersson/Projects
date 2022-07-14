from random import randrange


class Weapon:
    """weapon for character to hold"""

    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def __repr__(self) -> str:
        return f"{self.name} (DMG: +{self.damage})"


class Hero:
    """player character"""

    def __init__(self, name: str, max_health: int) -> None:
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.weapon = None

        # random character stats 3D6 each
        self.str = randrange(3, 18)
        self.int = randrange(3, 18)
        self.dex = randrange(3, 18)

    def __repr__(self) -> str:
        """character sheet for hero look into making justification modular"""

        output = "┌────────────────────────────────────────────┐\n"
        output += f"│Name : {self.name}".ljust(45) + "│\n"
        output += f"│Health: {self.health}/{self.max_health}".ljust(45) + "│\n"

        if self.weapon:
            output += f"│Weapon: {self.weapon}".ljust(45) + "│\n"

        output += f"│STR: {self.str}".ljust(45) + "│\n"
        output += f"│INT: {self.int}".ljust(45) + "│\n"
        output += f"│DEX: {self.dex}".ljust(45) + "│\n"
        output += "└────────────────────────────────────────────┘"

        return output

    def pick_up_weapon(self, weapon: Weapon) -> None:
        """Add weapon to heroes arsenal"""
        self.weapon = weapon

    def damage(self) -> int:
        """Calculate damage output"""
        if not self.weapon:
            return 1
        else:
            return 1 + self.weapon.damage


def main():
    """Test Code Here"""
    hero = Hero(name="Wizard", max_health=6)
    sword = Weapon(name="sword", damage=2)
    axe = Weapon(name="Axe", damage=5)

    hero.pick_up_weapon(axe)
    print(hero)


if __name__ == "__main__":
    main()
