def are_you_playing_banjo(name):
    name_letters = list(name.lower())
    if name_letters[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"