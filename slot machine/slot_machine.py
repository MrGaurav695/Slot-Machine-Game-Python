import random

# -------------------- CONSTANTS --------------------
SYMBOLS = ['A', 'B', 'C', 'D', 'E']
THREE_MATCH_MULTIPLIER = 10
TWO_MATCH_MULTIPLIER = 2


# -------------------- INPUT FUNCTIONS --------------------
def get_starting_balance():
    """Get a valid starting balance from the user."""
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))
            if balance <= 0:
                print("Balance must be a positive number.")
            else:
                return balance
        except ValueError:
            print("Please enter a valid number.")


def get_bet_amount(balance):
    """Get a valid bet amount within the available balance."""
    while True:
        try:
            bet = int(input("Enter your bet amount: $"))
            if bet <= 0 or bet > balance:
                print(f"Invalid bet. Enter a value between $1 and ${balance}.")
            else:
                return bet
        except ValueError:
            print("Please enter a valid number.")


# -------------------- GAME LOGIC --------------------
def spin_reels():
    """Return a list of three randomly selected symbols."""
    return [random.choice(SYMBOLS) for _ in range(3)]


def display_reels(reels):
    """Display the slot machine reels."""
    print(" | ".join(reels))


def calculate_payout(reels, bet):
    """
    Payout rules:
    - Three matching symbols: 10x bet
    - Two matching symbols: 2x bet
    - No match: 0
    """
    unique_symbols = set(reels)

    if len(unique_symbols) == 1:
        return bet * THREE_MATCH_MULTIPLIER
    elif len(unique_symbols) == 2:
        return bet * TWO_MATCH_MULTIPLIER
    else:
        return 0


# -------------------- MAIN GAME LOOP --------------------
def main():
    balance = get_starting_balance()

    print("\nWelcome to the Slot Machine Game.")
    print(f"Starting balance: ${balance}")

    while balance > 0:
        print(f"\nCurrent balance: ${balance}")
        bet = get_bet_amount(balance)

        reels = spin_reels()
        display_reels(reels)

        payout = calculate_payout(reels, bet)
        balance += payout - bet

        if payout > 0:
            print(f"You won ${payout}.")
        else:
            print("You lost this round.")

        if balance <= 0:
            print("You are out of money. Game over.")
            break

        choice = input("Play again? (y/n): ").lower()
        if choice != "y":
            print(f"You leave with ${balance}.")
            break


# -------------------- PROGRAM ENTRY --------------------
if __name__ == "__main__":
    main()
