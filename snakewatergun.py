import random
"""
snake = 1
gun= 0
water = -1

"""
print("---SNAKE WATER GUN GAME---")
print("---CHOOSE NOW---hangmahan")
choices = ["snake","gun","water"]
computer_choice = random.choice(choices)
choice2 = (input("Enter choice:")).lower()

yourDict = {"snake":1 , "gun":0, "water":-1}

me = yourDict[choice2]

print(f"computer choosed: {computer_choice}")

if(computer_choice==choice2):
    print("draw") 

elif(computer_choice==1 and me==-1) or (computer_choice==0 and me==1) or(computer_choice==-1 and me==0):
    print("you won")
else:
    print("you loose")






