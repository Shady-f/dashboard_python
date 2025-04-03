# rock >> paper >> sesor
import random

game_img = [rock,paper,seasor]
user_ch = int(input("Enter 0.rock 1.paper 2.sesor"))
computer_ch = random.randint(0,2)
print(f"user chose{game_img}")
print(f"Computerr chose {game_img} {computer_ch}")
if user_ch==0 or user_ch==1 or user_ch==2:
    if computer_ch==user_ch:
        print("draw")
    elif computer_ch == 0 and user_ch == 2:
        print("You Lose")
    elif computer_ch==2 and user_ch==0:
        print("You Win 😇😇")    
    elif computer_ch>user_ch:
        print("You Lose")
    elif user_ch>computer_ch:
        print("You Win 😇😇")  
   
else:
    print("Try again")             
        