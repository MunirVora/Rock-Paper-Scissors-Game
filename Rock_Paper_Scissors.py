import random

possible_choices = ["rock", "paper", "scissors"]

choice = "Y"

while choice == "Y" or choice == "y":

    computer_choice = random.choice(possible_choices)

    user_choice = input("Enter rock, paper or scissors : ")

    
    if user_choice == computer_choice:
        print("\nTie! Both selected the same.\n")
        print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("\n******* Great! You Win! *******\n")
            print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")

        elif computer_choice == "paper":
            print("\n******* Oops! You Lose! *******\n")
            print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")


    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("\n******* Oops! You Lose! *******\n")
            print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")

        elif computer_choice == "rock":
            print("\n******* Great! You Win! *******\n")
            print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")


    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("\n******* Oops! You Lose! *******\n")
            print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")

        elif computer_choice == "paper":
            print("\n******* Great! You Win! *******\n")
            print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")


    else:
        print("\n-------Invalid input.-------\n")
        print(f"Choices:\nComputer -> {computer_choice}\nYou -> {user_choice}")

        break

    while True:
        choice = input("\nWant play again? Press Y for Yes and N for No....")
        print()
        if choice == "Y" or choice == "y" or choice == "N" or choice == "n":
            break