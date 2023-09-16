import random

amount_of_attempt = 6
words_list = ['apple', 'computer', 'dog', 'banana', 'egg', 'independent']
word = random.choice(words_list)


def get_word_of_game():
    spelled_word = []
    hidden_spelled_word = []
    for letter in word:
        spelled_word.append(letter)
        hidden_spelled_word.append('_')
    print("".join(hidden_spelled_word))
    return spelled_word, hidden_spelled_word


def get_users_letter():
    while True:
        users_letter = input('Enter any letter: ').lower()
        if len(users_letter) == 1 and users_letter.isalpha():
            return users_letter
        else:
            print("You're an idiot! I told you to write one letter. ")


def set_terms_of_game():
    spelled_word, hidden_spelled_word = get_word_of_game()
    for attempt in range(amount_of_attempt):
        users_letter = get_users_letter()
        for index, letter in enumerate(spelled_word):
            if letter == users_letter:
                hidden_spelled_word[index] = spelled_word[index]
            else:
                continue
        print("".join(hidden_spelled_word))


print(set_terms_of_game())
