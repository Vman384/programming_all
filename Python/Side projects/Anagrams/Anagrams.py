letters = 'rpekod'
possiblewords = []


def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    for word in english_words:
        if len(word) <= 6:
            x = 0
            y = word
            for i in letters:
                if i in word:
                    x +=1
                    word = list(word)
                    word.remove(i)
            if x == 3 and len(y) == 3:
                possiblewords.append(y)
            elif x == 4 and len(y) == 4:
                possiblewords.append(y)
            elif x == 5 and len(y) == 5:
                possiblewords.append(y)
            elif x == 6 and len(y) == 6:
                possiblewords.append(y)
possiblewords = set(possiblewords)
possiblewords = sorted(list(possiblewords), key=len)
possiblewords.reverse()
print(possiblewords)
