from enum import Enum
import pygame
from cards import Deck
from gamestructure import Player


class GameState(Enum):
    START = 0
    VUILEWAS = 1
    PLAYING = 2
    ENDROUND = 3
    ENDED = 4
    ARMOE = 5


class ToepEngine:
    deck = None
    player1 = None
    player2 = None
    state = None
    currentPlayer = None
    result = None

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(
            "Player 1",
            pygame.K_q,
            pygame.K_w,
            pygame.K_e,
            pygame.K_r,
            pygame.K_t,
            pygame.K_y,
        )
        self.player2 = Player(
            "Player 2",
            pygame.K_a,
            pygame.K_s,
            pygame.K_d,
            pygame.K_f,
            pygame.K_g,
            pygame.K_h,
        )
        self.deal()
        self.currentPlayer = self.player1
        self.startPlayer = self.player1
        self.state = GameState.PLAYING
        self.toep_points = 1
        self.last_toep = None
        self.last_card = 0

    def deal(self):
        num_cards = 4
        for card in range(0, num_cards):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)

    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def winRound(self, winner, loser):
        self.state = GameState.ENDROUND
        winner.toep_points += 0
        loser.toep_points += self.toep_points
        self.toep_points = 1
        self.pile_player1.clear()
        self.pile_player1.clear()
        self.deck = Deck()
        self.deck.shuffle()

    def winner_loser(self):
        trump = self.player1.PlayerPile.trump
        cardplayer2 = self.player2.PlayerPile.peek()
        winorlose = self.player1.PlayerPile.peek().greater(trump, cardplayer2)
        if winorlose:
            winner, loser = (self.player1, self.player2)
        else:
            loser, winner = (self.player1, self.player2)
        return winner, loser

    def play(self, key):
        if self.last_card == 2:
            winner, loser = self.winner_loser()
            self.result = {
                "winner": {"name": winner.name, "points": winner.toep_points},
                "loser": {"name": loser.name, "points": loser.toep_points},
            }
            self.state == GameState.ENDED
            self.last_card == 0

        if key == self.currentPlayer.playKey:
            if self.currentPlayer == self.startPlayer:
                trump = True
            else:
                trump = False
            self.currentPlayer.PlayerPile.add(
                self.currentPlayer.play(), trump
            )
            if not self.currentPlayer.hand:
                self.last_card += 1
            self.switchPlayer()

        if self.state == GameState.ENDED:
            return
