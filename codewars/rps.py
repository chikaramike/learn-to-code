def rps(p1, p2):
    if p1 == p2:
        print("draw")
    elif p1 == "rock":
        if p2 == "scissors":
            print("P1 Won")
        elif p2 == "paper":
            print("P2 Won")
    elif p1 == "paper":
        if p2 == "scissors":
            print("P2 Won")
        elif p2 == "rock":
            print("P1 Won")
    elif p1 == "scissors":
        if p2 == "rock":
            print("P2 Won")
        elif p2 == "paper":
            print("P1 Won")



rps("rock", "scissors")
rps("rock", "paper")
rps("rock", "rock")
rps("paper", "rock")
rps("scissors", "rock")
