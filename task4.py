import random

print("===== ROCK PAPER SCISSORS =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        user_choice = "Rock"
    elif choice == "2":
        user_choice = "Paper"
    elif choice == "3":
        user_choice = "Scissors"
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
        continue

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: You Lose!")
        computer_score += 1

    print("\nScore:")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        print("Final Score:")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        break