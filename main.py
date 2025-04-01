# main.py
from Game import Game
from Opponent import Opponent

if __name__ == "__main__":
    game = Game()
    game.display_status()

    # Move the player
    game.player.move(10, 5)

    # Player shoots
    game.player.shoot()

    # Add an opponent and simulate collision
    opponent = Opponent(50, 50, "opponent_image")
    game.opponents.append(opponent)
    opponent.collide(game.player)

    # Remove the opponent and spawn the boss
    game.remove_opponent(opponent)

    # Simulate boss collision
    if game.boss:
        game.boss.collide(game.player)
        game.boss.collide(game.player)
        game.boss.collide(game.player)
        game.boss.collide(game.player)
        game.boss.collide(game.player)  # Defeat the boss

    # End the game
    game.end_game()
