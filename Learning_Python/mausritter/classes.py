# Mausritter class objects
class Mouse:
    """Player character"""

    def __init__(
        self, name: str, look: str, Str: int, Dex: int, Wil: int, Hp: int, Pip: int
    ) -> None:

        # Name and appearance
        self.name = name
        self.look = look

        # Stats
        self.STR = Str
        self.DEX = Dex
        self.WIL = Wil
        self.HP = Hp
        self.PIP = Pip

        # Starting gear
        self.starting_gear = ["Torch", "Ration", "Any weapon"]

        if 9 <= max([self.STR, self.DEX, self.WIL]) >= 7:
            self.starting_gear.append(random.choice([ml.Backgrounds[:, 3:4]]))

        elif max([self.STR, self.DEX, self.WIL]) < 7:
            self.starting_gear.append(random.choice([ml.Backgrounds[:, 3:4]]))
