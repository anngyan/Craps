import random

rollingCount = 0

minimum = 1
maximum = 6

firstDice = random.randint(minimum, maximum)
secondDice = random.randint(minimum, maximum)
summ = firstDice + secondDice
print(f"The sum of dice is {firstDice} + {secondDice} = {firstDice + secondDice}")

rollingCount += 1
if summ == 7 or summ == 11:
    print("You won")
elif summ == 2 or summ == 12 or summ == 3:
    print("The casino wins")
elif summ == 4 or summ == 5 or summ == 6 or summ == 8 or summ == 9 or summ == 10:
    summ1 = summ
    print(f"Now your goal number is {summ1}")
    while summ != 7 or summ != summ1:
        firstDice = random.randint(minimum, maximum)
        secondDice = random.randint(minimum, maximum)
        summ = firstDice + secondDice
        print(f"The sum of dice is {firstDice} + {secondDice} = {firstDice + secondDice}")
        if summ == summ1:
            print("You won")
            break
        elif summ == 7:
            print("You lose")
            break