with open ("Day1.txt") as r:
    data = r.read().split()

# dial starting position
dial = 50

# amount of times dial has hit 0
count = 0

# seperate direction and turn amount
pairs = [(s[0], int(s[1:])) for s in data]

for instruction in pairs:
    direction = instruction[0]
    amount = instruction[1]
    
    if direction == "R":
        count += (dial + amount) // 100
        dial = (dial + amount) % 100
    else:
        if dial == 0:
            count += amount // 100
        elif amount >= dial:
            count += (amount - dial) // 100 + 1
        dial = (dial - amount) % 100

# for this input your answer should be 5963
print (count)

