# Gave function param items so it can take in the items dict as a param
def step_into_jungle(items):
    # Put everything inside of a while True loop so any later scenes can return here
    while True:
        if items["piece_of_wood"] == True:
            print("\nThe Path to the inside of the island\n")
            userinput = ""
            print("Your options are:\n1. Continue walkin forward\n2. Look around\n3. Go to the beach\n4. Drop the piece of wood")
            if userinput == "1":
                crossroad()
            elif userinput == "2":
                print("random text for now")
            elif userinput == "3":
                return
            elif userinput =="4":
                items["piece_of_wood"] = False
                print("You dropped the Piece of wood on the ground. Now you feel lighter.\nWhat is your next action?\n")
            else:
                print("This is not a valid option.")
        else:
            print("\nThe Path to the inside of the island\n")
            options = ["1", "2", "3"]
            userinput = ""
            while userinput not in options or 1:
                print("Your options are:\n1. Look around\n2. Continue walkin forward\n3. Go to the beach\n")
                userinput = input(">")
                if userinput == "1":
                    print("""You take a look around you and you see the beautiful beach and hear the sound of the ocean. The water is crystalclear and you feel like u wanna go swimming.
    But the pain in your arm reminds you of your injury. A bit more far away u see some rocks at the beach and in the north it looks like some kind of vegetation.
    What is your next step?\n""")

                elif userinput == "2":
                    walkin_path_three()
                elif userinput == "3":
                    return
                elif userinput =="4":
                    items["piece_of_wood"] = False
                    print("You dropped the Piece of wood on the ground. Now you feel lighter.\nWhat is your next action?\n")
                else:
                    print("This is not a valid option.")
