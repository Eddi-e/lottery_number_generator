import random
ballList = []
for x in range(0,7):
    numCheck = True
    while numCheck == True:
        number = random.randint(1,49)
        if number in ballList:
        else:
            numCheck = False
    ballList.append(number)
print (ballList)
        