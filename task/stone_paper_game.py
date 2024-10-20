import random

choices = ("r", "p", "s")
emojis = {"r":"💎", "p":"📃", "s":"✂️"}

while True:
 user_choice = input("Rock, Paper, Scissors (r/p/s) ").lower()
 if user_choice not in choices:
  print("Invalid input")
  continue

 computer_choice = random.choice(choices)
 print(f"computer choice {emojis[computer_choice]}")
 print(f"user choice choice {emojis[user_choice]}")

 if user_choice == computer_choice:
  print("Tie!")
 elif ((user_choice == "p" and computer_choice == "r") or 
      (user_choice == "r" and computer_choice == "s") or
      (user_choice == "s" and computer_choice == "p")
      ):
    print("You win")
 else:
  print("you lose!")

 user_continue = input("Need to continue (y/n) ").lower()
 if user_continue == "n":
  break

