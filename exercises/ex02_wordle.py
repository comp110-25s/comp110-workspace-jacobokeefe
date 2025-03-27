"""Wordle"""

__author__ = "730574207"


def contains_char(search_string: str, single_char: str) -> bool:
    """
    Return True is the single character is found in the
    search string. Return False if otherwise.
    """
    assert len(single_char) == 1
    index: int = 0

    while index < len(search_string):
        if search_string[index] == single_char:
            return True
        index = index + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """
    Compare the guess with secret word and return a
    string of emojis. Use green for letter in right
    spot, yellow if in the secret but wrong position,
    and white if not in secret. Guess and secret same
    length.
    """
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result: str = ""
    index: int = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret, guess[index]):
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        index = index + 1
    return result


def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False

    while turn <= 6 and not win:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn = turn + 1

    if not win:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
