import random

# Define a simple card game with a deck of cards
class CardGame:
    def __init__(self):
        self.deck = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] * 4
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

# Define a simple AI player for the card game
class AIPlayer:
    def __init__(self):
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def play_card(self):
        if self.hand:
            return self.hand.pop(0)
        else:
            return None

# Define a simple human player for the card game
class HumanPlayer:
    def __init__(self):
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def play_card(self):
        if self.hand:
            print("Your current hand:", self.hand)
            choice = input("Enter the index of the card you want to play (0 for the first card): ")
            if choice.isdigit() and 0 <= int(choice) < len(self.hand):
                return self.hand.pop(int(choice))
            else:
                print("Invalid input. Please try again.")
                return self.play_card()
        else:
            print("You have no cards left.")
            return None

# Determine the winner of the game
def determine_winner(ai_hand, human_hand):
    if len(ai_hand) > len(human_hand):
        return "AI"
    elif len(human_hand) > len(ai_hand):
        return "Human"
    else:
        return "It's a tie"

# Main function to simulate the card game
def play_card_game():
    game = CardGame()
    ai_player = AIPlayer()
    human_player = HumanPlayer()

    # Deal cards to players
    for _ in range(5):
        ai_player.receive_card(game.deal_card())
        human_player.receive_card(game.deal_card())

    print("Game starts!")
    while True:
        # AI player's turn
        ai_card = ai_player.play_card()
        if ai_card is None:  # Skip AI's turn if it has no cards left
            print("AI has no cards left.")
        else:
            print("AI plays:", ai_card)

        # Human player's turn
        human_card = human_player.play_card()
        if human_card is None:  # Skip human's turn if they have no cards left
            print("You have no cards left.")
        else:
            print("You play:", human_card)

        # End game if either player runs out of cards
        if ai_card is None or human_card is None:
            break

    # Determine the winner
    winner = determine_winner(ai_player.hand, human_player.hand)
    print("Game over!")
    print("Winner:", winner)

# Start the card game simulation
if __name__ == "__main__":
    play_card_game()
