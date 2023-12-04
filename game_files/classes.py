class Game:
    players = []
    def __init__(self, game_name, player1, player2):
        self.game_name = game_name
        self.player1_name = player1
        self.player2_name = player2
        self.babymaker()

    def babymaker(self):
        self.players.append(Player(self.player1_name))
        self.players.append(Player(self.player2_name))





class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        print(self.player_name)


game1 = Game("peli1", "ville", "joel")

