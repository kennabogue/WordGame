import random
from re import A

# letters and points
letters = {'A' : {'quantity': 9, 'score': 1},
            'B': {'quantity': 2, 'score': 3},
            'C': {'quantity': 2, 'score': 3},     
            'D': {'quantity': 4, 'score': 2},
            'E': {'quantity': 12, 'score': 1},
            'F': {'quantity': 2, 'score': 4},
            'G': {'quantity': 3, 'score': 2},
            'H': {'quantity': 2, 'score': 4},
            'I': {'quantity': 9, 'score': 1},
            'J': {'quantity': 1, 'score': 8},
            'K': {'quantity': 1, 'score': 5},
            'L': {'quantity': 4, 'score': 1},
            'M': {'quantity': 2, 'score': 3},
            'M': {'quantity': 6, 'score': 4},
            'O': {'quantity': 8, 'score': 1}, 
            'P': {'quantity': 2, 'score': 3},
            'Q': {'quantity': 1, 'score': 10},
            'R': {'quantity': 6, 'score': 1},
            'S': {'quantity': 4, 'score': 1},
            'T': {'quantity': 6, 'score': 1},
            'U': {'quantity': 4, 'score': 1},
            'V': {'quantity': 2, 'score': 4},
            'W': {'quantity': 2, 'score': 4},
            'X': {'quantity': 1, 'score': 8},
            'Y': {'quantity': 2, 'score': 4},
            'Z': {'quantity': 1, 'score': 10}}

newLetters = letters

def lettersScoring():
    print('LETTER    SCORE')
    print('----------------')
    for letter in letters:
        score = letters[letter]['score']
        print(f'   {letter}        {score}')

def lettersRemaining():
    lettersAvailable = []
    for letter in letters:
        if letters[letter]['quantity'] > 0:
            lettersAvailable.append(letter)
    return lettersAvailable

def remainingCount():
    count = 0
    for letter in letters:
        count += letters[letter]['quantity']
    return count

def drawTiles(playerLetters):
    drawAmount = 7 - len(playerLetters)
    remainingAmount = remainingCount()
    if remainingAmount < drawAmount:
        drawAmount = remainingAmount
    if drawAmount > 0:
        for letter in range(drawAmount):
            remainingAmount = remainingCount()
            lettersLeft = lettersRemaining()
            count = len(lettersLeft)
            if remainingAmount > 1:
                letter = lettersLeft[random.randrange(0,count-1)]
            elif remainingAmount == 1:
                letter = lettersLeft[0]
            else:
                break
            playerLetters.append(letter)
            letters[letter]['quantity'] -= 1
    return playerLetters

def scoreWord(word):
    point_total = 0
    for letter in word:
        point_total += letters[letter.upper()]['score']
    return point_total