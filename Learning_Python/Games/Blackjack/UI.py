from typing import Protocol


class UI(Protocol):
    """
    Interface for interacting with the player in blackjack game
    """

    def introduction(self) -> None:
        raise NotImplementedError()

    def tutorial(self) -> None:
        raise NotImplementedError()

    def get_player_name(self) -> str:
        raise NotImplementedError()

    def player_choose_action(self) -> None:
        raise NotImplementedError()

    def house_choose_action(self) -> None:
        raise NotImplementedError()


def main():
    pass


if __name__ == "__main__":
    main()
