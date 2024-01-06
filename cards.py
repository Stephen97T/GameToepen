from enum import Enum
import pygame
import random


class Suits(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3


class Card:
    suit = None
    value = None
    image = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load(
            "images/" + self.suit.name + "-" + str(self.value) + ".jpg"
        )
        self.image = pygame.transform.scale(
            self.image, (int(238 * 0.8), int(332 * 0.8))
        )

    def greater(self, trump, othercard):
        if trump:
            if self.suit == othercard.suit:
                if self.value > othercard.value:
                    result = True
                else:
                    result = False
            else:
                result = True
        else:
            if self.suit == othercard.suit:
                if self.value > othercard.value:
                    result = True
                else:
                    result = False
            else:
                result = False
        return result


class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(3, 11):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def length(self):
        return len(self.cards)
