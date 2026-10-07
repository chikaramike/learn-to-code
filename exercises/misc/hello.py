num = 246
output = ""

for digit in str(num):
    output += str(int(digit) ** 2)

print(output)