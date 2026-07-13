import random # random module
jackpot = random.randint(1,50) # random number 
guess = int(input("Pick a number between 1 and 50 : "))
counter = 1
while guess != jackpot :
    if guess<jackpot :
        print("Nopee , higher")
        counter+=1
        guess = int(input("Guess again :"))
        continue
    elif guess>jackpot :
        print("Nopee , lower")
        counter+=1
        guess = int(input("Guess again :"))
        continue
print("Yess , you got it")
print("Attempts :",counter)
        