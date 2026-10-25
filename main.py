# Number Guessing Game

from random import randint # For have random number 
import os # For Some work with system
import json # For Save and Load data as a file
import time # For having date

#############

file = "hostory.json" # History File

# Saving history in the file
def save_data():
    with open(file,"w") as f :
        json.dump(history,f)

# Loading file datas in the list
def load_data():
    try :
        with open(file,"r") as f :
            return json.load(f)
    except :
        return []

# Deleting all data
def delete_data():
    if os.path.exists(file):
        os.remove(file)

#############
# Errors
errors = {
    "err_opt":"\n>> Error : Please choose number between options !\n",
    "err-dfc":"\n>> Error : Please choose difficulty from options !\n",
    "err-rnd":"\n>> Error : Please guese an number !\n",
}

# History List (When user run this file history list will update automaticly)
history = load_data()

############################################################### Funcions ###############################################################################################

# Clearing termminan func
def clear_term():
    os.system("cls")

# Main Game 
def game(d):
    clear_term()
    sps = "\n"+"-" * 20+"\n" # Just for better UI
    difficult = "" # We set this variable to a degree of sifficulty relative to the user's Inpot. 
    wins = 0 # Wins count
    loses = 0 # Loses Count
    bot = randint(0,(d * 10)+5) # Random number
    print("\t\t\tGame Started!\t\t\t\n")
    # Cheking user's input to set a difficulty
    if d == 1 :
        difficult = "Easy"
    elif d == 2 :
        difficult = "Normal"
    elif d == 3 :
        difficult = "Hard"
    elif d == 4 :
        difficult = "Impossible"
    # If user's input = 1 , round = 10 and must choose from (0,15)
    print(f"~ Difficulty : {difficult}, You have {d * 10} rounds !\n- Choose number between (0-{(d * 10) + 5}) !\n")
    for i in range(d * 10):
        print(f"\n~ Round {i+1}\n")
        user = input("Guese Number : ") # User guese
        if user.isnumeric():
            user = int(user)
            if user == bot :
                print(sps,f"\nYou Win :) Bot : {bot} | You : {user} !\n")
                wins += 1
                break
            elif user > bot :
                print(sps,f"\nYou lose :(\n- Decrease your number !\n")
                loses += 1
            elif user < bot :
                print(sps,f"\nYou lose :(\n- Incrase your number !\n")
                loses += 1
        else :
            print(errors["err-rnd"])

    # Result
    if wins == loses :
        print(f"\n>>> Match draw !\nWins : {wins} | Loses : {loses}\n")
    elif wins > loses :
        print(f"\n>>> Match Ended !\nWins : {wins} | Loses : {loses}\n")
    elif wins < loses :
        print(f"\n>>> Match Ended !\nWins : {wins} | Loses : {loses}\n")
    
    # Appending informations into list and save it to file
    history.append({
        "date":time.ctime(),
        "wins":wins,
        "loses":loses,
        "difficulty":difficult
    })

    save_data()

    input("\n~ Type any key to continue !\n")

def start_game():
    clear_term()
    # Options 
    while True :
        print("\t\tWelcome to Guessing number game !\t(0 For Quit)\t\n")
        difficult = input("Choose difficulty :\n1.Easy\n2.Normal\n3.Hard\n4.Impossible\n\n>> ")
        if difficult.isnumeric():
            if difficult == "0" : break
            elif 1 <= int(difficult) <= 4 :
                game(int(difficult))
            else :
                print(errors["err_opt"])
        else :
            print(errors["err-dfc"])

# History view
def show_history():
    clear_term()
    print("\t\tHistory of games !\t\t\n")
    if history != [] :
        for i,game in enumerate(history,1):
            print(f"\n{i}. ",game["difficulty"] ,"Game on",game["date"],"\n- Wins :",game["wins"] ,"| Loses :",{game["loses"]},"\n")
        q = input("Do you want to delete your History (Y/N) ? ") # Ask for deleting Data !
        q = q.replace(" ","").lower() # Making input simpler
        if q == "y" or q == "yes" or q == "yeah" or q == "yep" or q == "yup" or q == "bale" or q == "yeh":
            history.clear()
            delete_data()
            print("\n>> Hostory Was Deleted !\n")
        else :
            print("\n>> Hostory Wasen't Deleted !\n")
    else :
        print("\n>> History Was Empty .\n")

############################################################### Main ###################################################################################################

# Main func
def main():    
    while True :
        menu = input("\n1.Start\t2.Game History\t3.Quit\n- ")
        if menu.isnumeric() :
            if menu == "1" :
                start_game()
            elif menu == "2":
                show_history()
            elif menu == "3" : break
            else :
                print(errors["err_opt"])
        else :
            print(errors["err_opt"])
    clear_term()
    print("\nWe hope you enjoy playing !\n- Come back soon ;)\n")

if __name__ == "__main__":
    main()