import random
print("➖"*35)
print("🏏 WELCOME TO CRICKET.PY 🏏".center(50))
print("➖"*35)
print("### Try not to score same runs as Computer Generates! ###")
name = input("Enter Player Name -> ")

while True:
    total = 0
    print(f"\nWelcome, {name}! Let's start the game!\n")

    while True:
        comp = random.randint(0, 6)

        try:
            score = int(input("Enter runs (0-6) -> "))
            if score < 0 or score > 6:
                print("❌Invalid input! Please enter a number between 0 and 6.")
                continue
        except ValueError:
            print("❌Invalid input! Please enter a valid number.")
            continue

        print("➖"*11)
        print(f"🖥️  Computer: {comp} | 🧍 You: {score}")
        print("➖"*11)

        if comp == score:
            print("\n\t\t\t---GAME OVER!---\t\t\t")
            print("\n\n\n💥 OUT! You matched the computer!")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            break

        total += score
        print(f"Score so far: {total}\n")

    print(f"{name}, you have scored: {total} runs!\n")

    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("Thanks for playing Cricket.PY!")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        break
