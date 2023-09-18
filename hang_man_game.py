import random

number_of_attempts = 6
words_list = ['apple', 'computer', 'dog', 'banana', 'egg', 'independent', 'developer', 'wedding']
word = random.choice(words_list)


def get_word_of_game():
    """
    This function chooses word of list by random.
    Also create two lists with this spelled out word for the following use.
    """
    spelled_word = []
    hidden_spelled_word = []
    for letter in word:
        spelled_word.append(letter)
        hidden_spelled_word.append('_')
    print("".join(hidden_spelled_word))
    return spelled_word, hidden_spelled_word


def get_users_letter():
    """
    This function get users letter and check is this letter or number.
    """
    while True:
        users_letter = input('Enter any letter: ').lower()
        if len(users_letter) == 1 and users_letter.isalpha():
            return users_letter
        else:
            print("You're an idiot! I told you to write one letter. ")


def get_result():
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
    if last_chans == word:
        return 'You are winner!'
    else:
        return f"You lost. Right word: {word}"


def set_terms_of_game():
    """
    In this function there are all rules of game
    """
    spelled_word, hidden_spelled_word = get_word_of_game()

    for attempt in range(number_of_attempts):
        if '_' not in hidden_spelled_word:
            return f"You are winner. It really was word: {word}"
        users_letter = get_users_letter()
        for index, letter in enumerate(spelled_word):
            if letter == users_letter:
                hidden_spelled_word[index] = spelled_word[index]
            else:
                continue
        print("".join(hidden_spelled_word))

    if '_' in hidden_spelled_word:
        return get_result()


print(set_terms_of_game())
