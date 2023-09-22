import random
import requests


class Game:
    pass





class NumberGuessingGame(Game):
    MINIMUM_RANGE = 1
    MAXIMUM_RANGE = 10
    ATTEMPTS = 5
    random_number = random.randint(MINIMUM_RANGE, MAXIMUM_RANGE)
    API_URL = f"http://numbersapi.com/{random_number}/trivia?fragment"
    hints_used = 0

    def get_hint(self):
        """
        This function get hint from API.
        """
        response = requests.get(NumberGuessingGame.API_URL)
        if response.status_code == 200:
            hint = response.text
        return hint if hint else "There is none hints for this number"

    def get_users_number(self):
        """
        This function gets the user's number.
        """
        while True:
            users_input = input('Guess a number between 1 and 10 (inclusive): ')
            if users_input == 'hint' and NumberGuessingGame.hints_used == 0:
                NumberGuessingGame.hints_used = 1
                print(self.get_hint())
            elif users_input == 'hint' and NumberGuessingGame.hints_used == 1:
                print('You have used hint already')
            else:
                try:
                    users_number = int(users_input)
                    if NumberGuessingGame.MINIMUM_RANGE <= users_number <= NumberGuessingGame.MAXIMUM_RANGE:
                        return users_number
                    else:
                        print('Your number is out of range. Try to select a different number.')
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def play_game(self):
        """
        This function checks the selected user number for game conditions.
        """
        for attempt in range(NumberGuessingGame.ATTEMPTS):
            users_number = self.get_users_number()
            if users_number == NumberGuessingGame.random_number:
                return f"Congratulations, you guessed right :)"
            elif users_number < NumberGuessingGame.random_number:
                print("It's too low. Try again!")
            else:
                print("It's too high. Try again!")

        return f"You have used all your attempts. Correct number was {NumberGuessingGame.random_number} :("


class ScissorsPaperRockGame(Game):
    options = ['scissors', 'paper', 'rock']
    API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

    def get_hint(self):
        for word in ScissorsPaperRockGame.options:
            api_url_for_word = ScissorsPaperRockGame.API_URL.format(word)
            response = requests.get(api_url_for_word)
            if response.status_code == 200:
                data = response.json()
                entry = data[0] if data else None
                if entry:
                    word = entry.get('word', 'No such word')
                    phonetic = entry.get('phonetic', 'No phonetic')
                    print(f"Word: {word}, Phonetic: {phonetic}")
            else:
                print(f"Failed to get data for word: {word}")

    def get_user_option(self):
        """
        this function asks the user to choose scissors, paper or stone.
        If the user entered everything correctly, the choice is saved.
        If not, it laughs at what a sucker the user is and asks to choose again.
        """
        while True:
            user_option = input('Choose some option (scissors, paper or rock): ').lower()
            if user_option == 'hint':
                print(self.get_hint())
            elif user_option in ScissorsPaperRockGame.options:
                return user_option
            else:
                print("You can't spell words right, loser")

    def get_random_option(self):
        """
        This function makes the choice for the computer
        """
        random_option = random.choice(ScissorsPaperRockGame.options)
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
        user_option = self.get_user_option()
        random_option = self.get_random_option()

        print(f"You chose {user_option}. Computer chose {random_option}.")

        winner = self.get_winner(user_option, random_option)
        print(winner)


class HangManGame(Game):
    NUMBER_OF_ATTEMPTS = 6
    hints_used = 0
    word_list = ['apple', 'computer', 'dog', 'banana', 'egg', 'independent', 'developer', 'wedding']
    word = random.choice(word_list)
    API_URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    def get_hint_from_api(self):
        """
        Request for api
        By this function we get definition(hints) for our word
        """
        response = requests.get(HangManGame.API_URL)
        if response.status_code == 200:
            data = response.json()
        entry = data[0] if data else None

        if entry:
            meanings = entry.get('meanings', [])
            if meanings:
                definitions = meanings[0].get('definitions', [])
                if definitions:
                    definition = definitions[0].get('definition', 'No hints')
                    return definition
        return 'No hints for word! '

    def get_word_of_game(self):
        """
        This function chooses word of list by random.
        Also create two lists with this spelled out word for the following use.
        """
        spelled_word = []
        hidden_spelled_word = []
        for letter in HangManGame.word:
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
            if users_letter == 'hint' and HangManGame.hints_used == 0:
                HangManGame.hints_used = 1
                print(self.get_hint_from_api())
            elif users_letter == 'hint' and HangManGame.hints_used == 1:
                print('You have used hint already')
            elif len(users_letter) == 1 and users_letter.isalpha():
                return users_letter
            else:
                print("You're an idiot! I told you to write one letter. ")

    def get_result(self):
        """
        In case if user used all chance input the letter this function will
        announce whether the user has won or not, giving them one last chance to guess the word or use hints

        """
        while True:
            print(
                "You have used all your attempts. Last chance, enter the correct word. You can also get a hint by simply writing: 'hint'. ")
            last_chans = input().lower()

            if last_chans.isalpha():
                break
            else:
                print("Don't use numbers. Only one word! ")
        if last_chans == HangManGame.word:
            return 'You are winner!'
        else:
            return f"You lost. Right word: {HangManGame.word}"

    def play_game(self):
        """
        In this function there are all rules of game
        """
        spelled_word, hidden_spelled_word = self.get_word_of_game()

        for attempt in range(HangManGame.NUMBER_OF_ATTEMPTS):
            if '_' not in hidden_spelled_word:
                return f"You are winner. It really was word: {HangManGame.word}"
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
