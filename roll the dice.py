import random

print("\nWelcome to the world of game : 👤")
print("=" * 37)

player_score = 0
computer_score = 0

while True:
    options = range(1, 7)
    player = None

    while player not in options:
        player = int(input("Enter your choice (1-6): "))

    computer_choice = random.choice(options)
    print(f"Computer: {computer_choice}")
    print(f"Player: {player}")

    player_score += player
    computer_score += computer_choice

    play_again = input("Play again? (y/n): ").lower()

    if play_again == "n":
        print()
        if player_score > computer_score:
            print("❤" * 30)
            print(f"You win the match!\nYour score: {player_score}\nComputer score: {computer_score}")
            print()
        elif player_score == computer_score:
            print(f"Oh no! The match is tied.\nYour score: {player_score}\nComputer score: {computer_score}")
            print()
        else:
            print(f"You lose the match.\nYour score: {player_score}\nComputer score: {computer_score}")
            print()
        break
