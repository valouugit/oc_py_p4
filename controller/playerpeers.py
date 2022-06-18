from typing import List

from model.player import Player
from model.tournament import Tournament


class PlayerPeers:
    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament
        self.offset = 0

    def _gen_peers_with_position(self) -> List[tuple]:
        peers = []
        sorted_players = sorted(
            self.tournament.players,
            key=lambda p: p.position
        )
        for peer in range(0, int(len(sorted_players) / 2)):
            peers.append(
                (
                    sorted_players[peer],
                    sorted_players[int(len(sorted_players) / 2 + peer)],
                )
            )
        return peers

    def _gen_peers_with_score(self) -> List[tuple]:
        sorted_players = []
        for player in self.tournament.players:
            sorted_players.append([player, self._get_player_score(player)])
        sorted_players.sort(key=lambda p: p[1], reverse=True)
        self._sort_by_position_score_equal(sorted_players)
        peers = []
        for i in range(0, int(len(sorted_players) / 2)):
            p2_index = 1
            while True:
                if self._check_players_already_play(
                    sorted_players[0][0], sorted_players[p2_index][0]
                ):
                    p2_index += 1
                    if len(sorted_players) - 1 < p2_index:
                        p2_index = len(sorted_players) - 1
                        break
                else:
                    break
            peers.append((sorted_players[0][0], sorted_players[p2_index][0]))
            sorted_players.remove(sorted_players[p2_index])
            sorted_players.remove(sorted_players[0])
        return peers

    def _get_player_score(self, player: Player) -> int:
        score = 0
        for round in self.tournament.rounds:
            for match in round.match:
                for m_player, m_score in match:
                    if player == m_player:
                        score += m_score
        return score

    def _sort_by_position_score_equal(self, players: List):
        finish = False
        while not finish:
            finish = True
            for n_player in range(0, len(players) - 1):
                if players[n_player][1] == players[n_player + 1][1]:
                    if (
                        players[n_player][0].position
                        > players[n_player + 1][0].position
                    ):
                        p_temp = players[n_player + 1]
                        players[n_player + 1] = players[n_player]
                        players[n_player] = p_temp
                        finish = False
                        break

    def _check_players_already_play(self, player1: Player, player2: Player):
        for round in self.tournament.rounds:
            for match in round.match:
                if match[0][0] == player1 or match[0][0] == player2:
                    if match[1][0] == player1 or match[1][0] == player2:
                        return True
        return False

    def getNextPeers(self) -> List[tuple]:
        self.offset += 1
        if self.offset == 1:
            return self._gen_peers_with_position()
        else:
            return self._gen_peers_with_score()
