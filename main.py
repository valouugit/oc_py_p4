from controller.tournamentsmanager import TournamentManager


def main():
    try:
        tm = TournamentManager()
        tm.show_dashboard()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
