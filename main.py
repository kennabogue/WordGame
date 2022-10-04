from letters import scoreWord
import player 

def print_menu():
    print("\n------------- WORD GAME ------------- ")
    print("1. Start Game.")
    print("2. Exit.")

def rules():
    print("\n Letter Scoring:")
    player.letters.lettersScoring()

    print("\n------------- RULES ------------- ")
    print("Enter a word using your available letters.")
    print("Your words will be scored based on the letters you use. See scoring table above.")

def get_user_choice():
    while(True):
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Input not valid. Choose a number option.")
            continue
        else:
            break
    return choice

def playersJoin():
        addMore = True
        while(addMore):
            if len(player.players) < 4:
                player.addPlayer()
                player.displayLeaderboard()
                try:
                    confirm = str(input('Are these all your players? (y/n): ')).lower()
                    if confirm == 'n':
                        continue
                    elif confirm == 'y':
                        addMore = False
                except ValueError:
                    print("Input not valid. Enter y or n.")
                    continue
                else:
                    print("Input not valid. Enter y or n.")
            elif len(player.players) >= 4:
                player.displayLeaderboard()
                print("You have reached the maximum players.")
                break

def playWord(turn):
    while(True):
        try:
            word = str(input('Enter a word: '))
            for letter in word:
                letter = letter.upper()
                turn.letters.index(letter)
        except ValueError:
            print("Please enter one of your letters.")
            print(turn.letters)
        else:
            break
    for letter in word:
        letter = letter.upper()
        turn.letters.remove(letter)
    return word

def takeTurns():
    game = True
    while(game):
        for turn in player.players:
            player.displayPlayerTurn(turn)
            word = playWord(turn)
            turn.score += player.letters.scoreWord(word)
            player.letters.drawTiles(turn.letters)
            if len(turn.letters) < 1:
                game = False
        player.displayLeaderboard()
    for turn in player.players:
        score = 0
        for letter in turn.letters:
            score += scoreWord(letter)
        turn.score += score
        
def main():
    game_on = True
    while(game_on):
        print_menu()
        user_choice = get_user_choice()
        if(user_choice == 1):
            player.letters.letters = player.letters.newLetters
            player.players = []
            playersJoin()
            rules()
            takeTurns()
            player.displayWinner()
        elif(user_choice == 2):
            print("Bye Bye!!!")
            break

main()
    