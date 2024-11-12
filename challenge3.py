list = ["r", "r", "g", "b", "g", "g", "b", "b", "g", "r"]
#red-5  blue-20  green-10
sum = 0

for x in list:
    if x == "r":
        sum = sum + 5
    elif x == "b":
        sum = sum + 20
    elif x == "g":
        sum = sum + 10

print(sum)