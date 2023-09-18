import random

MINIMUM_RANGE = 1
MAXIMUM_RANGE = 10
ATTEMPTS = 5
RANDOM_NUMBER = random.randint(MINIMUM_RANGE, MAXIMUM_RANGE)


def get_users_number():
    """
    This function get users number.
    """
    while True:
        users_input = input('Guess a number between 1 and 10 (inclusive): ')
        try:
            users_number = int(users_input)
            if MINIMUM_RANGE <= users_number <= MAXIMUM_RANGE:
                return users_number
            else:
                print('Your number is out of range. Try to select different number.')
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def set_game_conditions():
    """
    This function checks the selected user number for game conditions.
    """
    for attempt in range(ATTEMPTS):
        users_number = get_users_number()
        if users_number == RANDOM_NUMBER:
            return f"Congratulations, you guessed right :)"
        elif users_number < RANDOM_NUMBER:
            print("It's too low. Try again!")
        else:
            print("It's too high. Try again!")

    return f"You have used all your attempts. Correct number was {RANDOM_NUMBER} :("


number_game = set_game_conditions()
print(number_game)
