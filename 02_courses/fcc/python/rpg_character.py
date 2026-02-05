full_dot = '●'
empty_dot = '○'

def create_character(name, str_stat=None, int_stat=None, cha_stat=None):
    if not isinstance(name, str):
        return "The character name should be a string."

    if name == "":
        return "The character should have a name."

    if len(name) > 10:
        return "The character name is too long."

    if " " in name:
        return "The character name should not contain spaces."

    stats = [str_stat, int_stat, cha_stat]

    if any(not isinstance(s, int) for s in stats):
        return "All stats should be integers."

    if any(s < 1 for s in stats):
        return "All stats should be no less than 1."

    if any(s > 4 for s in stats):
        return "All stats should be no more than 4."

    if sum(stats) != 7:
        return "The character should start with 7 points."

    def bar(value):
        return full_dot * value + empty_dot * (10 - value)

    return (
        f"{name}\n"
        f"STR {bar(str_stat)}\n"
        f"INT {bar(int_stat)}\n"
        f"CHA {bar(cha_stat)}"
    )