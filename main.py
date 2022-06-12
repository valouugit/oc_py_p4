from datetime import datetime
from controller.playerpeers import PlayerPeers
from controller.tournamentsmanager import TournamentManager
from model.player import Player
from model.round import Round
from model.timer import Timer
from model.tournament import Tournament
from rich import inspect

from view.dashboard import Dashboard


def main():
    try:
        tm = TournamentManager()
        tm.show_dashboard()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
