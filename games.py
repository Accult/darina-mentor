import random

import requests


class Game:
    OPTIONS = ["scissors", "paper", "rock"]
    API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

    def __init__(self):
        self.hints_used = 0

    def get_hint(self):
        """
        Here is API request which get hint from api
        """
        for word in self.OPTIONS:
            api_url_for_word = self.API_URL.format(word)
            response = requests.get(api_url_for_word)
            if response.ok:
                data = response.json()
                entry = data[0] if data else None
                if entry:
                    word = entry.get("word", "No such word")
                    phonetic = entry.get("phonetic", "No phonetic")
                    print(f"Word: {word}, Phonetic: {phonetic}")
            else:
                print(f"Failed to get data for word: {word}")

    def check_hints_used(self, users_input):
        if users_input == "hint" and self.hints_used == 0:
            self.hints_used = 1
            return self.get_hint()
        elif users_input == "hint" and self.hints_used == 1:
            return "You have used hint already! "


class NumberGuessingGame(Game):
    MINIMUM_RANGE = 1
    MAXIMUM_RANGE = 10
    ATTEMPTS = 5

    def __init__(self):
        self.random_number = random.randint(self.MINIMUM_RANGE, self.MAXIMUM_RANGE)
        self.hints_used = 0
        self.API_URL = f"http://numbersapi.com/{self.random_number}/trivia?fragment"

    def get_hint(self):
        """
        This function get hint from API.
        """

        response = requests.get(self.API_URL)
        if response.ok:
            hint = response.text
        return hint if hint else "There is none hints for this number"

    def get_users_number(self):
        """
        This function gets the user's number.
        """
        while True:
            users_input = input(f"Guess a number between {self.MINIMUM_RANGE} and {self.MAXIMUM_RANGE} (inclusive): ")
            if users_input == "hint":
                print(self.check_hints_used(users_input))
            else:
                try:
                    users_number = int(users_input)
                    if self.MINIMUM_RANGE <= users_number <= self.MAXIMUM_RANGE:
                        return users_number
                    else:
                        print("Your number is out of range. Try to select a different number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def play_game(self):
        """
        This function checks the selected user number for game conditions.
        """
        for attempt in range(self.ATTEMPTS):
            users_number = self.get_users_number()
            if users_number == self.random_number:
                return "Congratulations, you guessed right :)"
            elif users_number < self.random_number:
                print("It's too low. Try again!")
            else:
                print("It's too high. Try again!")

        return f"You have used all your attempts. Correct number was {self.random_number} :("


class ScissorsPaperRockGame(Game):
    OPTIONS = ["scissors", "paper", "rock"]
    API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

    def get_user_option(self):
        """
        this function asks the user to choose scissors, paper or stone.
        If the user entered everything correctly, the choice is saved.
        If not, it laughs at what a sucker the user is and asks to choose again.
        """
        while True:
            user_option = input("Choose some option (scissors, paper or rock): ").lower()
            if user_option == "hint":
                self.get_hint()
            elif user_option in self.OPTIONS:
                return user_option
            else:
                print("You can't spell words right, loser")

    def get_random_option(self):
        """
        This function makes the choice for the computer
        """
        random_option = random.choice(self.OPTIONS)
        return random_option

    @staticmethod
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

        if (
            (user_option == "rock" and random_option == "scissors")
            or (user_option == "paper" and random_option == "rock")
            or (user_option == "scissors" and random_option == "paper")
        ):
            return "Congratulations, you win!"

        else:
            return "You lost! Computers took over the world."

    def play_game(self):
        user_option = self.get_user_option()
        random_option = self.get_random_option()

        print(f"You chose {user_option}. Computer chose {random_option}.")

        winner = self.get_winner(user_option, random_option)
        print(winner)


class HangManGame(Game):
    NUMBER_OF_ATTEMPTS = 6
    WORD_LIST = [
        "apple",
        "computer",
        "dog",
        "banana",
        "egg",
        "independent",
        "developer",
        "wedding",
    ]

    def __init__(self):
        self.word = random.choice(self.WORD_LIST)
        self.API_URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{self.word}"
        self.hints_used = 0

    def get_hint(self):
        """
        Request for api
        By this function we get definition(hints) for our word
        """
        response = requests.get(self.API_URL)
        if response.ok:
            data = response.json()
        entry = data[0] if data else None

        if entry:
            meanings = entry.get("meanings", [])
            if meanings:
                definitions = meanings[0].get("definitions", [])
                if definitions:
                    definition = definitions[0].get("definition", "No hints")
                    return definition
        return "No hints for word! "

    def get_word_of_game(self):
        """
        This function chooses word of list by random.
        Also create two lists with this spelled out word for the following use.
        """
        spelled_word = []
        hidden_spelled_word = []
        for letter in self.word:
            spelled_word.append(letter)
            hidden_spelled_word.append("_")
        print("".join(hidden_spelled_word))
        return spelled_word, hidden_spelled_word

    def get_users_letter(self):
        """
        This function get users letter and check is this letter or number.
        """
        while True:
            users_input = input("Enter any letter: ").lower()
            if users_input == "hint":
                print(self.check_hints_used(users_input))
            elif len(users_input) == 1 and users_input.isalpha():
                users_letter = users_input
                return users_letter
            else:
                print("You're an idiot! I told you to write one letter. ")

    def get_result(self):
        """
        In case if user used all chance input the letter this function will
        announce whether the user has won or not, giving them one last chance to guess the word or use hints

        """
        while True:
            if self.hints_used == 0:
                print(
                    "You have used all your attempts. Last chance, enter the correct word. You can also get a hint by simply writing: 'hint'. "
                )
            else:
                print("You have used all your attempts. Last chance, enter the correct word.")
            last_chans = input().lower()
            if last_chans == "hint":
                self.hints_used = 1
                print(self.get_hint())
            elif last_chans.isalpha():
                break
            else:
                print("Don't use numbers. Only one word! ")

        if last_chans == self.word:
            return "You are winner!"
        else:
            return f"You lost. Right word: {self.word}"

    def play_game(self):
        """
        In this function there are all rules of game
        """
        spelled_word, hidden_spelled_word = self.get_word_of_game()
        for attempt in range(self.NUMBER_OF_ATTEMPTS):
            if "_" not in hidden_spelled_word:
                return f"You are winner. It really was word: {self.word}"
            users_letter = self.get_users_letter()
            for index, letter in enumerate(spelled_word):
                if letter == users_letter:
                    hidden_spelled_word[index] = spelled_word[index]
                else:
                    continue
            print("".join(hidden_spelled_word))

        if "_" in hidden_spelled_word:
            return self.get_result()


if __name__ == "__main__":
    while True:
        print()
        print("In any game you can use some hint just by writing 'hint' !")
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
