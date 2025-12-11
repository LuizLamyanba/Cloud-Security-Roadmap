import random
coinflip = []
streak = False
finalstreak = 0
numofstreak = 0

for exp in range(10000):
    for i in range(100):
        coinflip.append(random.randint(0,1))
    for i in range(len(coinflip)):
        if i == 0:
            pass
        elif coinflip[i] == coinflip[i-1]:
            numofstreak+=1
        else:
            numofstreak = 0
        if numofstreak == 6:
            finalstreak+=1
            streak = True
    coinflip = []
    numofstreak = 0
    streak = False

print("streak percentage = %s%% " %(finalstreak/100))
