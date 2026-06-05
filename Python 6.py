from datetime import datetime
current_time = datetime.now()

name = input ("Enter your name.")
mood = input ("How are you feeling today? (stressed/happy/sad/excited):").lower
energy = int(input("Rate your energy level from 1 to 10: "))
print("\nHellp", name + "!")
print("Current Date and Time:", current_time.strftime("%d-%m-%Y %H:%M:%S"))
print("\n ---Daily mood advice---")
if mood == "happy":
    if energy >= 7:
        print("Great, Use your positive energy to acheive something productive today")
    else:
        print("Enjoy your happiness and take some time to relax")
elif mood=="sad":
    if energy>= 5:
        print("Try doing something you enjoy or talk to a friend. It may lift your mood")
    else:
        print("Take some time to rest and be kind to your self.")


if mood == "stressed":
    if energy >= 5:
        print("Take sort breaks, stay organized, and focus on one task at a time")
    else:
        print("onsider resting, practicing deep breathing, or listening to calming music")
elif mood=="excited":
    if energy>= 7:
        print("antastic! Channel your excitement into achieving your goals")
    else:
        print("njoy the excitement, but remember to pace yourself.")

else:
    print("Stay positive and make the most out of your day!")

print("Have a wonderful day", name)