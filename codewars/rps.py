def rps(p1, p2):
    if p1 == p2:
        return "draw"
    elif p1 == "rock":
        if p2 == "scissors":
            return "P1 Won"
        elif p2 == "paper":
            return "P2 Won"
    elif p1 == "paper":
        if p2 == "scissors":
            return "P2 Won"
        elif p2 == "rock":
            return "P1 Won"
    elif p1 == "scissors":
        if p2 == "rock":
            return "P2 Won"
        elif p2 == "paper":
            return "P1 Won"



print(rps("rock", "scissors"))
print(rps("rock", "paper"))
print(rps("rock", "rock"))
print(rps("paper", "rock"))
print(rps("scissors", "rock"))
