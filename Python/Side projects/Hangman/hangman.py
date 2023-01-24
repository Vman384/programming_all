import random
import string


def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return list(valid_words)


def game():
    word = list(random.choice(load_words()))
    NumberOfGuesses = 6
    table = []
    guessed = []
    y = len(word)
    for _ in word:
        table.append('_')
    while y > 0 and NumberOfGuesses > 0:
        while True:
            guess = input("guess a letter: ")
            guess = guess.lower()
            if len(guess) != 1:
                print('can only guess one letter at a time')
            else:
                if guess in table or guess in guessed:
                    print('you have already selected this letter')
                else:
                    if guess not in set(string.ascii_lowercase):
                        print('you can only guess a letter')
                    else:
                        break
        if guess in word:
            for index, _ in enumerate(word):
                if _ == guess:
                    table[index] = guess
                    y -= 1
        else:
            guessed.append(guess)
            NumberOfGuesses -= 1
        print("INCORRECT LETTERS")
        for i in guessed:
            print(i, end='')
        print('')
        for i in table:
            print(i, end='')
        print('')
    if y == 0:
        print('Congrats you guess the word')
    else:
        word=''.join(word)
        print(f'Better luck next time the word was {word}')


game()
