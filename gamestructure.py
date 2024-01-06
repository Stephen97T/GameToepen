class Pile:
    cards = None

    def __init__(self):
        self.cards = []
        self.trump = None

    def add(self, card, trump):
        self.cards.append(card)
        self.trump = trump

    def clear(self):
        self.cards = []

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None


class Player:
    hand = None
    flipKey = None
    snapKey = None
    name = None

    def __init__(
        self, name, playKey, toepKey, vuilewasKey, peakKey, foldKey, callKey
    ):
        self.hand = []
        self.toep_points = 0
        self.playKey = playKey
        self.toepKey = toepKey
        self.vuilewasKey = vuilewasKey
        self.peakKey = peakKey
        self.foldKey = foldKey
        self.callKey = callKey
        self.name = name
        self.PlayerPile = Pile()

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)
