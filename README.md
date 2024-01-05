# GameToepen
# Toepen Game with Pygame

## Overview

Toepen is a traditional Dutch card game played with a standard deck of 32 cards. It is a trick-taking game where players bid on the number of tricks they anticipate winning. This project implements a digital version of the Toepen game using Python and the Pygame library.

## Game Mechanics

### 1. **Bidding System:**

Players take turns bidding on the number of tricks they believe they can win in the current round. Bids are made in a clockwise order, starting from the player to the left of the dealer.

### 2. **Trump Suit:**

The player with the highest bid gets to choose the trump suit for the round. The trump suit is a special suit that can beat cards of other suits, regardless of their rank.

### 3. **Trick-taking Gameplay:**

- The player to the left of the dealer leads the first trick by playing a card.
- Other players must follow suit if possible; otherwise, they can play a trump card.
- The player with the highest-ranking card (trump or leading suit) wins the trick.
- The winner of a trick leads the next one.

### 4. **Scoring System:**

- Points are awarded based on the bid and the number of tricks won.
- If a team fulfills their bid, they earn points equal to the bid multiplied by 10.
- Special combinations like "pit" or "mars" may also earn additional points.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/yourusername/toepen-game.git1](https://github.com/Stephen97T/GameToepen.git)https://github.com/Stephen97T/GameToepen.git
