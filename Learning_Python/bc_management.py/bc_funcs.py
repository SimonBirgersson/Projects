from datetime import datetime


class Member:
    """current member of beer club"""

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

        self.cheap_beers = 0  # 20:-
        self.expensive_beers = 0  # 30:-

        self.debt = 0

    def __repr__(self) -> str:
        # {datetime.today().strftime('%Y-%m-%d')}\n
        return f"Name: {self.name}\nEmail: {self.email}\nCurrent debt: {self.debt}:-\nTotal consumed beers: {self.cheap_beers+self.expensive_beers}\n\n"

    def tally(self, beers_20sek: int, beers_30sek: int, extra: int = 0):
        """compile current debt"""

        # add consumed amount of beer
        self.cheap_beers += beers_20sek
        self.expensive_beers += beers_30sek

        # calc current debt
        self.debt = self.cheap_beers * 20 + self.expensive_beers * 30 + extra


def main():
    """this runs when the script runs"""

    # List of inital members
    members = [
        ("Simon Birgersson", "simon.w.birgersson@biochemistry.lu.se"),
        ("Mathias Wiemann", "mathias.wiemann@biochemistry.lu.se"),
    ]

    # initiate Member objects
    BC = []
    for i, member in enumerate(members):
        print(type(member))
        BC.append(Member(name=member[0], email=member[1]))


if __name__ == "__main__":
    main()
