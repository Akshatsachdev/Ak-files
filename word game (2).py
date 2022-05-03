import random
Game="Welcome to the WORD GAME"
gameover="GAME OVER"
print(Game.center(150,"*"))
name=input("Please Enter your Name:")

sport=("cricket","football","vollyball","hockey","kabbadi","badminton","shuttlehock","golf","baseball")
charnames=("otis","meave","jack","eric","adam","milborn","hannahbaker","rio","smith","samuel","tokyo")
cars=("ford","ferrori","wolkwogan","bmw","benz","audi","lambhogini","tata")
bikes=("ducati","honda","tvs","duke","royalenfield","bajaj","himalayan","thunderbird","yamaha")
print("WARNING:",name,",You Have only 16 gessess to find the word,"
      "otherwise the man will dead,so play the game carefully","so Good luck",name)
temp1=list(charnames)
temp2=list(sport)
temp3=list(cars)
temp4=list(bikes)
sports=random.choice(temp1)
names=random.choice(temp2)
car=random.choice(temp3)
bike=random.choice(temp4)
list1=[sports,names,car,bike]
word=random.choice(list1)

if word in temp1:
    print("Hint-1:The character name in netflix series's")
elif word in temp2:
        print("Hint-1:One of the sport name")
elif word in temp3:
        print("Hint-1:one of  Car Brand Names ")
else:
    if word in temp4:
        print("Hint-1:One of  Bike Brand Names")
print("Hint-2:The word's length  :  ",len(word))
guesses=""
trails=16
while trails>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed=+1
    if failed==0:
        print("********************YOU WIN********************")
        print("The word is:",word)
        break
    guess=input("Enter a character:")
    guesses=guesses+guess
    if guess not in word:
        trails=trails-1
        print("You Lose")
    
        print ("you have ",+trails,"guesses")
        if trails==15:
                print(
                         
                         "\n=======\n")
        elif trails==14:
                 print(        
                         "\n      \n"
                         "\n      \n"
                         "\n|      \n"
                          "\n======\n")
        elif trails==13:
                 print(     
                         "\n|      \n"
                         "\n|      \n"
                         "\n|      \n"
                         "\n=======\n")
        elif trails==12:
                 print(   "\n__\n"
                        " \n|      \n"
                         "\n|      \n "      
                         "\n|      \n"
                         "\n|      \n"
                         "\n|     \n"
                          "\n======\n" )
        elif trails==11:
                 print(   "\n______\n"
                        " \n|      \n"
                         "\n|      \n "      
                         "\n|      \n"
                         "\n|      \n"
                         "\n|      \n"
                          "\n=======\n")
        elif trails==10:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      \n"
                         "\n|      \n"
                         "\n|      \n"
                          "\n=======\n")
        elif trails==9:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     \n"
                         "\n|      \n"
                          "\n=======\n")
                 
        elif trails==8:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|      | \n"
                         "\n|     \n"
                          "\n=======\n")
        elif trails==7:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|      |\ \n"
                         "\n|      \n"
                          "\n=======\n")
        elif trails==6:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     /|\ \n"
                         "\n|       \n"
                          "\n=======\n")
        elif trails==5:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     /|\ \n"
                         "\n|       \n"
                          "\n=======\n")
        elif trails==4:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     /|\ \n"
                         "\n|       \n"
                          "\n=======\n")
        elif trails==3:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     /|\ \n"
                         "\n|     /  \n"
                          "\n=======\n")
        elif trails==2:
                 print(   "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     /|\ \n"
                         "\n|     /  \n"
                          "\n=======\n")
         
                
        else:      
    
          if trails==0:
              print("you lose")
              print(      "\n______\n"
                        " \n|      |\n"
                         "\n|      |\n "      
                         "\n|      o\n"
                         "\n|     /|\ \n"
                         "\n|     / \ \n"
                          "\n=======\n")
              print("Better luck Next Time",name)
              print(gameover.center(150,"*"))
if trails==0:
      finish=input("do you finish the game:")
      print(finish)
