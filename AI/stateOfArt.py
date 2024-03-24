import random

class RockPaperScissors:
  """
  A simple two-player Rock-Paper-Scissors game.
  """
  def __init__(self):
    self.player1_score = 0
    self.player2_score = 0
    self.options = ["Rock", "Paper", "Scissors"]

  def play_round(self):
    # Player 1 chooses an option (action)
    player1_choice = random.choice(self.options)
    print(f"Player 1 chooses: {player1_choice}")

    # Simulate Player 2's choice (also an action)
    player2_choice = random.choice(self.options)
    print(f"Player 2 chooses: {player2_choice}")

    # Determine winner and update scores (reward) based on the game rules
    # (This is a simplified version without ties)
    if player1_choice == "Rock":
      if player2_choice == "Scissors":
        self.player1_score += 1
        print("Player 1 wins!")
      else:
        self.player2_score += 1
        print("Player 2 wins!")
    elif player1_choice == "Paper":
      if player2_choice == "Rock":
        self.player1_score += 1
        print("Player 1 wins!")
      else:
        self.player2_score += 1
        print("Player 2 wins!")
    elif player1_choice == "Scissors":
      if player2_choice == "Paper":
        self.player1_score += 1
        print("Player 1 wins!")
      else:
        self.player2_score += 1
        print("Player 2 wins!")

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

# Example game with 5 rounds
game = RockPaperScissors()
game.play_game(20)
