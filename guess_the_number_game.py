import random


def chose_random_number():
    """
    The function generates number between 1 and 10(includes) and give user five chans to guess this number
    Also add to every fail attempt a little tip: is this to high or to low
    """
    random_number = random.randint(1, 10)
    for attempt in range(5):
        user_number = int(input('Guess a number between 1 and 10 includes: '))
        if user_number == random_number:
            return f"Congratulations, you guessed right :)"
        elif user_number < random_number:
            print("It's too low. Try again!")
        elif user_number > random_number:
            print("It's too high. Try again!")
    return f"You have used all your attempts. Correct number was {random_number} :("


start = chose_random_number()
print(start)
