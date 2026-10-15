import random
'''
1 for snake
-1 for water
0 for gun

'''
computer = random.choice([-1,0,1])
youstr = input("Enter you choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"Snake",-1:"water" ,0:"Gun" }
you = youDict[youstr]

print(f" You Chose{reverseDict[you]}Computer Chose{reverseDict[computer]}")

if(computer == you):
    print("ita a draw")

else:
  if(computer ==-1 and you ==1):
    print("you Win!")

  elif(computer ==-1 and you ==0):
    print("You lose!") 

  if(computer ==1 and you ==-1):
    print("you Lose!")

  elif(computer ==1 and you ==0):
    print("You Win!") 

  if(computer ==0 and you ==-1):
    print("you win!")

  elif(computer ==-0 and you ==1):
    print("You lose!") 


  else: 
    print("something went wrong")