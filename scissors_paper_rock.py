import random

OPTIONS = ['scissors', 'paper', 'rock']


def get_user_option():
    """
    this function asks the user to choose scissors, paper or stone.
    If the user entered everything correctly, the choice is saved.
    If not, it laughs at what a sucker the user is and asks to choose again.
    """
    while True:
        user_option = input('Choose some option (scissors, paper or rock): ').lower()
        if user_option in OPTIONS:
            return user_option
        else:
            print("You can't spell words right, loser")


def get_random_option():
    """
    This function makes the choice for the computer
    """
    random_option = random.choice(OPTIONS)
    return random_option


def get_winner(user_option, random_option):
    """
    This function determine winner.
    Task said that rock wins against scissors,
    paper wins against rock,
    scissors wins against paper.
    So, in all other situations you lose
    """
    if user_option == random_option:
        return "Tie-up! We can play again :)"

    if (user_option == "rock" and random_option == "scissors") or (
            user_option == "paper" and random_option == "rock") or (
            user_option == "scissors" and random_option == "paper"):
        return "Congratulations, you win!"

    else:
        return "You lost! Computers took over the world."


def play_game():
    while True:
        user_option = get_user_option()
        random_option = get_random_option()

        print(f"You chose {user_option}. Computer chose {random_option}.")

        winner = get_winner(user_option, random_option)
        print(winner)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break


print(play_game())
