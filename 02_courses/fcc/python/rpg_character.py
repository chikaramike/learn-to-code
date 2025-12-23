full_dot = '●'
empty_dot = '○'

name = input("Enter a name: ")
def create_character(n):
    if len(n) > 10:
        return 'Too Long'
 
cha = create_character(name)
print(cha)


#def create_character(name, strength, intelligence, charisma):
#   print('test')
#    if name != str:
#        return "The character name should be a string"
#    if len(name) > 10:
#        return "The character name is too long"


