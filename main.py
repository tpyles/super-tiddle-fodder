import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Meals
breakfast = ["eggs and bacon", "english muffins and jam", "cereal", "oatmeal and raisins"]
lunch = ["sandwich", "pasta", "steak"]
dinner = ["more steak", "fish", "more pasta"]


# Dates
day = random.randrange(1, 100)


running = True

while running:

    print("\n")
    print(bcolors.OKBLUE + "=============================================================================" +
          bcolors.ENDC)
    print(bcolors.BOLD + bcolors.OKGREEN + "WELCOME TO RANDOM MEAL! RUN TO SEE YOUR FOOD FOR THE DAY" + bcolors.ENDC)
    print("\n")

    if day >= 45:
        print("Breakfast today is " + breakfast[0] + ". Sounds good right!?")
    elif day <= 45:
        print("Breakfast today is " + breakfast[1] or breakfast[3] + "." "Sounds good right!?")
        if breakfast[1]:
            print(bcolors.BOLD + bcolors.FAIL + "Lucky you! randomly I gift you with some OJ!" + bcolors.ENDC)
    if day >= 25:
        print("Lunch is " + lunch[1] + " ohhhh snap!")
    elif day <= 25:
        print("Lunch today is " + lunch[2] + " ahhhh yea!")
    if day <= 68:
        print("and dinner is going to be....." + dinner[2] + "\n")
    elif day >= 68:
        print("and dinner is going to be....." + dinner[1] + "\n" + "\n")

    print(bcolors.BOLD + bcolors.OKGREEN + "ENJOY YOUR MEAL!" + bcolors.ENDC)
    print(bcolors.BOLD + bcolors.OKBLUE + "========================================================================="
                                          "====" + bcolors.ENDC)
    running = False

