#Text-based adventure game
answer=input("Do you want to play Adventure game?")

if answer=="yes":
    print("That's Really Great Lets Play it !")
    print()
    answer=input("Do you want to explore a cave or jungle?[cave/jungle]")

    if answer=="cave":
        print("You go into the cave and see a sleeping beer")
        print()
        answer=input("Do you want to fight or run?[fight/run]")
        if answer=="fight":
            print("Bears are really stronger! you Lose")

        elif answer=="run":
            print("You ran away! You win ")
        else:
            print("Invalid Option, you lose!")
    elif answer=="jungle":
        print("You meet tiger and you get attacked!!! you lost")
    else:
        print("Invalid Option, you lose!")


else:
    print("BUt this is awesome game!")
