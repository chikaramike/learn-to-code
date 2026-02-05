full_dot = '●'
empty_dot = '○'

 # 1. You should have a function named create_character.

def create_character(n):
    print(f"You entered {n}")

# 2. When create_character is called with a first argument that is not a string it should return The character name should be a string.
    if not isinstance(n, str):
        return "The character name should be a string."

# 3. When create_character is called with a first argument that is an empty string, it should return The character should have a name.
    if n == "":
        return "The character should have a name."
    
# 4. When create_character is called with a first argument that is longer than 10 characters it should return The character name is too long.
# 5. The create_character function should not say that the character is too long when it's not longer than 10 characters.

    if len(n) > 10:
        return "The character name is too long."

# 6. When create_character is called with a first argument that contains a space it should return The character name should not contain spaces.
    if " " in n:
        return "The character name should not contain spaces."
# 7. When create_character is called with a second, third or fourth argument that is not an integer it should return All stats should be integers.

    if 
        return "All stats should be integers."

# 8. When create_character is called with a second, third or fourth argument that is lower than 1 it should return All stats should be no less than 1.

    if :
        return "All stats should be no less than 1."
# 9. When create_character is called with a second, third or fourth argument that is higher than 4 it should return All stats should be no more than 4.

    if :
        return "All stats should be no more than 4."
# 10. When create_character is called with a second, third or fourth argument that do not sum to 7 it should return The character should start with 7 points.
    if :
        return "The character should start with 7 points."
    
# 11. create_character('ren', 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.
# 12. When create_character is called with valid values it should output the character stats as required.

    return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.


create_character("test")
print(create_character(5))
print(create_character(""))
print(create_character("12345678910"))
print(create_character("1 810"))






