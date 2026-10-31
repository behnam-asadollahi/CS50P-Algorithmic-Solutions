def main():
    target = 67
    guess = ask()
    attempts = 1

    while guess != target:
        if guess > target:
            print("Too High!")
        else:
            print("Too Low!")

        guess = ask()
        attempts += 1

    print("Good job!", f"You won with {attempts} attempts!")


def ask():
    try:
        guess = int(input("Make your guess: "))
        return guess
    except ValueError:
        print("Please enter a valid integer.")
        return ask()


main()