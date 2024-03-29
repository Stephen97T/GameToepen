import pygame
from toepengine import ToepEngine, GameState

gameEngine = ToepEngine()

pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Toepen")


cardBack = pygame.image.load("images/BACK.jpg")
cardBack = pygame.transform.scale(cardBack, (int(238 * 0.8), int(332 * 0.8)))


def renderGame(window):
    window.fill((15, 0, 169))
    font = pygame.font.SysFont("comicsans", 60, True)

    window.blit(cardBack, (100, 200))
    window.blit(cardBack, (700, 200))

    text = font.render(
        str(len(gameEngine.player1.hand)) + " cards", True, (255, 255, 255)
    )
    window.blit(text, (100, 500))

    text = font.render(
        str(len(gameEngine.player2.hand)) + " cards", True, (255, 255, 255)
    )
    window.blit(text, (700, 500))

    topCard1 = gameEngine.player1.PlayerPile.peek()
    if topCard1 is not None:
        window.blit(topCard1.image, (100, 180))

    topCard2 = gameEngine.player2.PlayerPile.peek()
    if topCard2 is not None:
        window.blit(topCard2.image, (700, 180))

    if gameEngine.state == GameState.PLAYING:
        text = font.render(
            gameEngine.currentPlayer.name + " to flip", True, (255, 255, 255)
        )
        window.blit(text, (20, 50))

    if gameEngine.state == GameState.ENDROUND:
        result = gameEngine.result
        message = (
            result["winner"]["name"]
            + " is the winner"
            + " with "
            + result["winner"]["points"]
            + " points."
            + result["loser"]["name"]
            + " is the loser"
            + " with "
            + result["loser"]["points"]
            + " points."
        )
        text = font.render(message, True, (255, 255, 255))
        window.blit(text, (20, 50))

    if gameEngine.state == GameState.ENDED:
        result = gameEngine.result
        message = "Game Over! " + result["winner"]["name"] + " wins!"
        text = font.render(message, True, (255, 255, 255))
        window.blit(text, (20, 50))


run = True
while run:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = event.key

    gameEngine.play(key)
    renderGame(window)
    pygame.display.update()

    if gameEngine.state == GameState.ENDROUND:
        pygame.time.delay(3000)
        gameEngine.state = GameState.PLAYING
