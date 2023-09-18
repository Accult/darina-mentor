import random

minimum_range = 1
maximum_range = 10


def choose_random_number():
    """
    The function generates number between 1 and 10(includes) and gives user five chans to guess this number
    Also add to every failed attempt a little tip: is this to high or to low
    """
    random_number = random.randint(1, 10)
    for attempt in range(5):
        while True:
            user_choice = input('Guess a number between 1 and 10 (inclusive): ')
            try:
                user_number = int(user_choice)
                if 1 <= user_number <= 10:
                    break
                else:
                    print('Your number is out of range. Try to select different number.')
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if user_number == random_number:
            return f"Congratulations, you guessed right :)"
        elif user_number < random_number:
            print("It's too low. Try again!")
        else:
            print("It's too high. Try again!")
    return f"You have used all your attempts. Correct number was {random_number} :("


number_game = choose_random_number()
print(number_game)
