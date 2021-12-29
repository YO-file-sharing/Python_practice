from random import *

NUM = randint(1,100)
print(NUM)
while True:
    while True:
        a = input("Please enter a number.\n")
        if a.isdigit() == True:
            b = input("""The number is \"{}\" ,right ?\nPlease answer with \'yes\' or \'no\'.\n""".format(a))
            if b.lower() == "yes":
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
