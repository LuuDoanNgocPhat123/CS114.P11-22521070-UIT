online_players = set()

while True:
    line = input()
    
    if line == "0":
        break
    
    a, b = map(int, line.split())
    
    if a == 1:
        online_players.add(b)
    elif a == 2:
        if b in online_players:
            print(1)
        else:
            print(0)
    elif a == 3:
        online_players.discard(b)
