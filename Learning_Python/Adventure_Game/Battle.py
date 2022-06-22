from random import randrange

Monster import Attack, Monster


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
