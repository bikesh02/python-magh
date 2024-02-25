import random
while True:
    random_number= random.randint(1, 10)
    user_input=int(input("Enter a number between 1 to 10:"))
    if user_input==random_number:
        print("Congratulations. you guessed the correct number.")
    else:
<<<<<<< HEAD
        print(f"Sorry, the correct number was {random_number}. try again!")
=======
        print(f"Sorry, the correct number was {random_number}. try again!")
>>>>>>> 511807b58d846ed3c5722f5d27886c9f62a325a4
