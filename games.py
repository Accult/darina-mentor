import random


class Game:
    def __init__(self):
        pass


class NumberGuessingGame(Game):
    def __init__(self):
        super().__init__()
        self.MINIMUM_RANGE = 1
        self.MAXIMUM_RANGE = 10
        self.ATTEMPTS = 5
        self.RANDOM_NUMBER = random.randint(self.MINIMUM_RANGE, self.MAXIMUM_RANGE)

    def get_users_number(self):
        """
        This function get users number.
        """
        while True:
            users_input = input('Guess a number between 1 and 10 (inclusive): ')
            try:
                users_number = int(users_input)
                if self.MINIMUM_RANGE <= users_number <= self.MAXIMUM_RANGE:
                    return users_number
                else:
                    print('Your number is out of range. Try to select different number.')
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_game(self):
        """
        This function checks the selected user number for game conditions.
        """
        for attempt in range(self.ATTEMPTS):
            users_number = self.get_users_number()
            if users_number == self.RANDOM_NUMBER:
                return f"Congratulations, you guessed right :)"
            elif users_number < self.RANDOM_NUMBER:
                print("It's too low. Try again!")
            else:
                print("It's too high. Try again!")

        return f"You have used all your attempts. Correct number was {self.RANDOM_NUMBER} :("


class ScissorsPaperRockGame(Game):
    def __init__(self):
        super().__init__()
        self.OPTIONS = ['scissors', 'paper', 'rock']

    def get_user_option(self):
        """
        this function asks the user to choose scissors, paper or stone.
        If the user entered everything correctly, the choice is saved.
        If not, it laughs at what a sucker the user is and asks to choose again.
        """
        while True:
            user_option = input('Choose some option (scissors, paper or rock): ').lower()
            if user_option in self.OPTIONS:
                return user_option
            else:
                print("You can't spell words right, loser")

    def get_random_option(self):
        """
        This function makes the choice for the computer
        """
        random_option = random.choice(self.OPTIONS)
        return random_option

    def get_winner(self, user_option, random_option):
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

    def play_game(self):
        while True:
            user_option = self.get_user_option()
            random_option = self.get_random_option()

            print(f"You chose {user_option}. Computer chose {random_option}.")

            winner = self.get_winner(user_option, random_option)
            print(winner)

            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break


class HangManGame(Game):
    def __init__(self):
        super().__init__()
        self.NUMBER_OF_ATTEMPTS = 6
        self.WORD_LIST = ['apple', 'computer', 'dog', 'banana', 'egg', 'independent', 'developer', 'wedding']
        self.WORD = random.choice(self.WORD_LIST)

    def get_word_of_game(self):
        """
        This function chooses word of list by random.
        Also create two lists with this spelled out word for the following use.
        """
        spelled_word = []
        hidden_spelled_word = []
        for letter in self.WORD:
            spelled_word.append(letter)
            hidden_spelled_word.append('_')
        print("".join(hidden_spelled_word))
        return spelled_word, hidden_spelled_word

    def get_users_letter(self):
        """
        This function get users letter and check is this letter or number.
        """
        while True:
            users_letter = input('Enter any letter: ').lower()
            if len(users_letter) == 1 and users_letter.isalpha():
                return users_letter
            else:
                print("You're an idiot! I told you to write one letter. ")

    def get_result(self):
        """
        In case if user used all chance input the letter this function will
        announce whether the user has won or not, giving them one last chance to guess the word

        """

        while True:
            last_chans = input('What do you think this word is: ').lower()
            if last_chans.isalpha():
                break
            else:
                print("Don't use numbers. Only one word! ")
        if last_chans == self.WORD:
            return 'You are winner!'
        else:
            return f"You lost. Right word: {self.WORD}"

    def play_game(self):
        """
        In this function there are all rules of game
        """
        spelled_word, hidden_spelled_word = self.get_word_of_game()

        for attempt in range(self.NUMBER_OF_ATTEMPTS):
            if '_' not in hidden_spelled_word:
                return f"You are winner. It really was word: {self.WORD}"
            users_letter = self.get_users_letter()
            for index, letter in enumerate(spelled_word):
                if letter == users_letter:
                    hidden_spelled_word[index] = spelled_word[index]
                else:
                    continue
            print("".join(hidden_spelled_word))

        if '_' in hidden_spelled_word:
            return self.get_result()


if __name__ == "__main__":
    while True:
        print()
        print("Choose a game:")
        print("1. Number Guessing Game")
        print("2. Rock-Paper-Scissors Game")
        print("3. Hangman Game")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            number_game = NumberGuessingGame()
            result = number_game.play_game()
            print(result)
        elif choice == "2":
            rps_game = ScissorsPaperRockGame()
            rps_game.play_game()
        elif choice == "3":
            hangman_game = HangManGame()
            result = hangman_game.play_game()
            print(result)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
