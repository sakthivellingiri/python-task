import random

random_number = random.randint(1,100)
while True:
  try:
    user_number_gusse = int(input("Gusse the number between 1 to 100 : "))
    if random_number > user_number_gusse:
     print("Too Low!")
    elif random_number < user_number_gusse:
      print("Too High!")
    else:
      print("You gussed the number")
  except ValueError:
    print("Enter a valid input!")

