import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, isBoring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.tournament_score = 0

players = []

n = int(input("How many players?"))

for i in range(n):
    print(f"For the {i + 1}th player") 
    name = input("What's the name?")
    age = int(input("What's the age?"))
    elo = float(input("What's the elo?"))
    tenacity = int(input("What's the tenacity?"))
    isBoring = input("Yes or No").lower() == "yes" 

    player = ChessPlayer(name, age, elo, tenacity, isBoring)
    players.append(player)

def simulate_match(player1, player2):
    elo_diff = abs(player1.elo - player2.elo)
    
    if elo_diff > 100:
        if player1.elo > player2.elo:
            player1.tournament_score += 1
        else:
            player2.tournament_score += 1
    elif 50 <= elo_diff <= 100:
        if player1.elo > player2.elo:
            if player2.tenacity * random.randint(1, 10) > player1.tenacity:
                player2.tournament_score += 1
            else:
                player1.tournament_score += 1
        elif player2.elo > player1.elo:
            if player1.tenacity * random.randint(1, 10) > player2.tenacity:
                player1.tournament_score += 1
            else:
                player2.tournament_score += 1
    elif elo_diff < 50:
        if player1.tenacity > player2.tenacity:
            player1.tournament_score += 1
        else:
            player2.tournament_score += 1
    elif player1.isBoring and elo_diff<100:
        player1.tournament_score+=0.5
        if player2.isBoring and elo_diff<100:
            player2.tournament_score+=0.5

for i in range(n):
    for j in range(i + 1, n):
        print(f"Match between {players[i].name} (Black) and {players[j].name} (White)")
        result_black = simulate_match(players[i], players[j])
        #print(f"Result: {result_black}")
        
        print(f"Match between {players[j].name} (Black) and {players[i].name} (White)")
        result_white = simulate_match(players[j], players[i])
       # print(f"Result: {result_white}")


print("Names \t Score\t ")
for player in players:
    print(f"{player.name}\t {player.tournament_score}\t")
