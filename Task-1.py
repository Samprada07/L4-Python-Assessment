import random

#INITIALIZING LIST
CONSTANTS1 = ["Grouper", "Walleye", "Carp", "Sturgeon","Scad", "Surmullet",
             "Tengra", "Magur", "Anchovy", "Bullhead", "Flounder"]
CONSTANTS2 = ["Zebra", "Giraffe", "Koala", "Kangaroo", "Panda", "Racoon", "Jackal"]
CONSTANTS3 = ["Vulture", "Eagle", "Peacock", "Kiwi", "Ostrich", "Sparrow", "Parrot"]

print("Password Generator")
print("==================\n")
# iteration until required input is entered
while True:
#HANDLING EXCEPTION WHEN WRONG INFORMATION IS ENTERED BY USER
    try:
        choice = int(input("How many passwords are needed?:  "))
        if choice > 0 and choice < 24:
            print("\n")
            for i in range(choice):
                #selects random single value from each list
                rand_const_1 = random.choice(CONSTANTS1)
                rand_const_2 = random.choice(CONSTANTS2)
                rand_const_3 = random.choice(CONSTANTS3)
                CONSTANTS = []
                #random single value append to list constants
                CONSTANTS.append(rand_const_1)
                CONSTANTS.append(rand_const_2)
                CONSTANTS.append(rand_const_3)
                random.shuffle(CONSTANTS) #shuffling from selected elements
                joined = "".join(CONSTANTS) #selected elements are joined to become string
                print(str(i+1) + " --> " + joined) #REQUIRED OUTPUT
            break
        else:
            print("Please enter a value between 1 and 24. ")
    except:
        print("Please enter a number.")

        