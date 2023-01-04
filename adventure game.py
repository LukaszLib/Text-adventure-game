name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are at a crossroads, do you want to go left or right? ")

if answer == "left":
    answer = input("You come to a river, do you want to walk around or swim across? Type 'walk' to walk around or 'swim' to swim across: ")

    if answer == "swim":
        print("You are eaten by a crocodile.")
    elif answer == "walk":
        print("You have walked for many miles and have died of thirst.")
    else:
        print("That is not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? Type 'cross' to cross the bridge or 'back' to go back: ")

    if answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you want to talk to them? Type 'yes' to talk to them or 'no' to ignore them: ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they kill you.")
        else:
            print("That is not a valid option. You lose.")

    elif answer == "back":
        print("You go back and lose.")
    else:
        print("That is not a valid option. You lose.")

else:
    print("That is not a valid option. You lose.")

print("Thank you for playing!")
