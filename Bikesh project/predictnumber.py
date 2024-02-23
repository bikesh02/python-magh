import random
while True:
    random_number= random.randint(1, 2)
    user_input=int(input("Enter a number between 1 to 2:"))
    if user_input==random_number:
        print("Congratulations. you guessed the correct number.")
    else:
        print(f"Sorry, the correct number was {random_number}. try again!")
