import random

class CoinFlipGame:
  """
  A simple two-player game where players guess the outcome of a coin flip.
  """
  def __init__(self):
    self.player1_score = 0
    self.player2_score = 0

  def play_round(self):
    # Simulate coin flip (heads or tails)
    coin_flip = random.choice(["H", "T"])

    # Get player guesses
    player1_guess = input("Player 1, guess (H or T): ").upper()
    player2_guess = input("Player 2, guess (H or T): ").upper()

    # Update scores based on guesses and coin flip
    if player1_guess == coin_flip:
      self.player1_score += 1
      print("Player 1 scores!")
    elif player2_guess == coin_flip:
      self.player2_score += 1
      print("Player 2 scores!")
    else:
      print("No winner this round")

    print(f"Player 1 score: {self.player1_score}")
    print(f"Player 2 score: {self.player2_score}")

  def play_game(self, num_rounds):
    for _ in range(num_rounds):
      self.play_round()

    # Announce winner (if any)
    if self.player1_score > self.player2_score:
      print("Player 1 wins!")
    elif self.player1_score < self.player2_score:
      print("Player 2 wins!")
    else:
      print("It's a tie!")

# Example game with 3 rounds
game = CoinFlipGame()
game.play_game(3)
