from random import *

NUM = randint(1,10)
# print(NUM)
while True:
    while True:
        a = input("Please enter a number between 1 and 10.\n")
        if a.isdigit() == True:
            b = input("""The number is \"{}\" ,right ?\n
Please answer with \'yes\' or \'no\'.\n""".format(a))
            if b.lower() == "yes" or b.lower() == "y":
                # print("Thank you !")
                break
            else:
                pass
        else:
            print("Please do not enter whithout a number !!!\n")

    if int(a) == NUM:
        print("Conratulations !")
        break
    else:
        print("Sorry , Please try again.\n")
