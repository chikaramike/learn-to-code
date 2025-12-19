def rps(p1, p2):
    if p1 == "rock" and p2 == "scissors":
        print("P1 Won")
    elif p1 == "rock" and p2 == "paper":
        print("P1 Lost")
    elif p1 == p2:
        print("Draw")

rps("rock", "scissors")
rps("rock", "paper")
rps("rock", "rock")
