import letters

class Player:
    def __init__(self, name, score, letters, words):
        self.name = name
        self.score = score
        self.letters = letters
        self.words = words

players = []

def addPlayer():
    name = str(input("\nEnter Name: \n"))
    newPlayer = Player(name, score=0, letters=letters.drawTiles([]), words = [])
    players.append(newPlayer)
    return players

def displayPlayerTurn(player):
    print(f"\n-----------{player.name.upper()}'s TURN-----------")
    print(f'\n SCORE: {player.score}')
    print(f'\n LETTERS: {player.letters}')

def displayLeaderboard():
    print(f"\n-----------LEADERBOARD-----------")
    players.sort(key=lambda x: x.score, reverse=True)
    for player in players:
        print(f'{player.name}: {player.score}')

def displayWinner():
    print(f"\n-----------FINAL SCORE-----------")
    for player in players:
        print(f'{player.name}: {player.score}')

    print(f"Congrats, {players[0].name}. You are the winner!!")
