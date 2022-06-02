print(" This is a Rock Paper Scissors Game")
print("Instructions")
possible_options = ["R", "P", "S"]
print( ' "R" for "rock"' )
print( ' "P" for "paper"' )
print( ' "S" for "scissors"' )


import random

while  True:
    user = input("Enter a choice R, P, S : ")
    computer = random.choice(possible_options)
    print(f"\nYou chose {user}, computer chose {computer}.\n")


    if user == computer:
        print( "It\'s a tie!")
    elif ((user == "R") and (computer == "P")):
        print("computer wins,you lose")
    elif ((user == "P") and (computer == "R")):
        print("Big Ups, you win!")
    elif ((user == "R") and (computer == "S")):
        print("Rock smashes scissors,you win!")   
    elif ((user == "S") and (computer == "R")):
        print("computer wins,you lose")   
    elif ((user == "P") and (computer == "S")):
        print("computer wins,you lose") 
    elif ((user == "S") and (computer == "P")):
        print("scissors cuts paper,you win")
    elif user != computer:
        print("Invalid input")
    else:
        print("user")

    play_again = input("Enter y to continue or n to break : ")

    if play_again == "y":
            continue
    else:
        break


        
