items = {"plastic_bottle": False, "piece_of_wood": False, "glass_bottle": False}

from scenes2 import step_into_jungle

def beach():

    if items["plastic_bottle"] == True:
        print("Beach Startscene\n")
        options = ["1", "2"]
        userinput = ""
        while userinput not in options:
            print("1. Go left\n2. Go right")
            userinput = input(">")
            if userinput == "1":
                leftside()
            elif userinput == "2":
                rightside()
            else:
                print("This is not a valid option.")
    
    else:
        print("Beach Startscene\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options or 4:
            print("1. Get up and look around\n2. Go left\n3. Go right\n4. Keep laying")
            userinput = input(">")
            if userinput == "1":
                print("""You are trying to get up. Your arm hurts pretty much when you are moving it. 
After you managed to get on your feet. You get a better look of your surroundings. 
As far your eyes can see there is only water. Behind you lies a path that seems to lead into a little jungle. 
While you are look around on the beach, you see a platisc bottle in the sand.
What is your next action?\n""")
            
                print("1. Get the plastic bottle\n2. Go left\n3. Go right")
                userinput = input(">")
                if userinput == "1":
                    items["plastic_bottle"] = True
                    print("You received Plastic Bottle.\nWhat is your next action?\n")
                    print("1. Go left\n2. Go right")
                    userinput = input(">")
                    if userinput == "1":
                        leftside()
                    elif userinput =="2":
                        rightside()
                    else:
                        print("This is not a valid option.")

                elif userinput == "2":
                    leftside()
                elif userinput == "3":
                    rightside()
                else:
                    print("This is not a valid option.")
            elif userinput == "2":
                leftside()
            elif userinput == "3":
                rightside()
            elif userinput == "4":
                print("You feel the sun on your skin and the soft breeze from the wind. If your wound wouldnt hurt then this would be really comfortable and relaxing.\nWhat is your next action?\n")
            else:\
                print("This is not a valid option.")


def leftside():
    print("\nBeach left side\n")
    options = ["1", "2", "3", "4"]
    userinput = ""
    while userinput not in options or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back\n4. Take the path towards the vegetation")
        userinput = input(">")
        if userinput == "1":
            print("""You take a look around you and you see the beautiful beach and hear the sound of the ocean. The water is crystalclear and you feel like u wanna go swimming.
But the pain in your arm reminds you of your injury. A bit more far away u see some rocks at the beach and in the north it looks like some kind of vegetation.
What is your next step?\n""")

        elif userinput == "2":
            stoned_area()
        elif userinput == "3":
            beach()
        elif userinput =="4":
            step_into_jungle()
        else:
            print("This is not a valid option.")


def stoned_area():

    if items["piece_of_wood"] == True:
        print("\nRockybeach\n")
        options = ["1", "2"]
        userinput = ""
        print("Your options are:\n1. Go forward\n2. Go back")
        userinput = input(">")
        if userinput == "1":
            walkin_path_one()
        elif userinput == "2":
            leftside()
        else:
            print("This is not a valid option.")

    else:
        print("\nRockybeach\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options or 1:
            print("Your options are:\n1. Look around\n2. Go forward\n3. Go back\n4. Explore the rocks")
            userinput = input(">")
            if userinput == "1":
                print("""While you let your eyes wander around. You see then more and more stony the area becomes.
Around twenty meters from you, you see some huge rocks that are nearly as tall as you. If you wanna explore this area.
You need to be careful not to break your legs or anything else.\n""")
            elif userinput == "2":
                walkin_path_one()
            elif userinput == "3":
                leftside()
            elif userinput == "4":
                print("""You are taking off your shoes to get a better feeling with your feet. You are slowly walkin towards the rocks.
You are carefully climbing on the rocks and trying to hold the balance with ur hands gripping some edge of the rocks. 
As you slowly making your way through the rocks, you notice piece of wood that is laying between two rocks.
What is your next step?\n""")
                  
                print("1. Grab the piece of wood\n2. Go forward\n3. Go back")
                userinput = input(">")
                if userinput == "1":
                    items["piece_of_wood"] = True
                    print("You received Piece of wood.\nWhat is your next action?\n")
                    print("1. Go forward\n2. Go back")
                    userinput = input(">")
                    if userinput == "1":
                        walkin_path_one()
                    elif userinput =="2":
                        leftside()
                    else:
                        print("This is not a valid option.")
                elif userinput =="2":
                    walkin_path_one()
                elif userinput =="3":
                    leftside()
                else:
                    print("This is not a valid option.")
            
            else:
                print("This is not a valid option.")


def rightside():
    print("\nBeach right side\n")
    options = ["1", "2", "3", "4"]
    userinput = ""
    while userinput not in options or 4 or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back\n4. Sit down")
        userinput = input(">")
        if userinput == "1":
            print("""You take a look around you and you see the beautiful beach and hear the sound of the ocean. The water is crystalclear and you feel like u wanna go swimming. \n",
But the pain in your arm reminds you of your injury. A bit more far away u see some rocks at the beach and in the north it looks like some kind of vegetation.
What is your next step?\n""")
        elif userinput == "2":
            cliff_scene()
        elif userinput == "3":
            beach()
        elif userinput == "4":
            print("You are sitting down in the sand and make yourself comfortable. Its so nice feeling the sun on your skin. It surely would be nice to spend the day on the beach.\n What is your next step?\n")
        else:
            print("This is not a valid option.")

def cliff_scene():

    if items["glass_bottle"] == True:
        print("\nThe Cliffs\n")
        options = ["1", "2"]
        userinput = ""
        print("Your options are:\n1. Go forward\n2. Go back\n")
        userinput = input(">")
        if userinput == "1":
           walkin_path_two()
        elif userinput == "2":
           rightside()
        else:
            print("This is not a valid option.")

    else:
        print("\nThe Cliffs\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options or 1:
            print("Your options are:\n1. Sit down and look around\n2. Go forward\n3. Climb down\n4. Go back")
            userinput = input(">")
            if userinput == "1":
                print("""You find a comfy spot to sit down and gaze over the scenery that lies infront of you.
You wonder how fast the sandy beach on which you woke up got swapped with this enoumerous cliff that seems to have no end.
You let your eyes go till the edge and realize that its a long way down from the cliff till the water.
You better pay attention to your steps, cause you don't wanna end up as decoration on the ground.
While you let your eyes wander over the cliff, you spot something shiny. As you look closer you moticed that there is something stuck between the rocks.
Probably someone might accidentally dropped something there, which now reflects the sunlight during the daytime.\n""")
            elif userinput == "2":
                walkin_path_two()
            elif userinput == "3":
                print("""You decided to climb down the cliff to investiga what the shiny thing is that u spotted. 
First you look around for a path that alloaws you to climb down safely. Around five meters away from you, you see some small way
which seems to lead down the cliff. Carefully you go down, one step after another, always making sure your hands have something to hold on.
As you are getting closer, you see its a bottle probably made of glass. Finally you are close enough to grab the bottle and its indeed a glass bottle.
The bottle is totally empty but maybe it could be of some use anyway at some point. 
What do you wanna do?\n""")
                userinput = ""
                print("Your options are:\n1. Take the bottle with you\n2. Leave it you already have one")
                userinput = input(">")
                if userinput == "1":
                    items["glass_bottle"] = True
                    print("You receive a glass bottle! (<insert zelda sound of receiving an item>)\n What is your next move\n")
                    print("1. Go forward\n2. Go back")
                    userinput = input(">")
                    if userinput == "1":
                        walkin_path_two()
                    elif userinput =="2":
                        rightside()
                    else:
                        print("This is not a valid option.")
                else:
                    print("You leave the glass bottle where it is\n")

            elif userinput == "4":
                rightside()
            else:
                print("This is not a valid option.")

def walkin_path_one():
    print("\nWalk along the Beach\n")
    forward = 0
    backward = 1
    options = ["1", "2", "3"]
    userinput = ""
    while userinput not in options or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back")
        userinput = input(">")
        if userinput == "1":
            print("""Your eyes are wandering along the beach. As far your eyes can see, you see only water till the horizont. There is nothing much to see here
beside the sand and some shells on the beach. The trees in the jungle are so narrow that there is no path into it. 
Its probably the best to not stay too long in this burning sun.
What is your next step?\n""")
        elif userinput == "2":
            forward = forward +1
            backward = backward +1
        elif userinput == "3":
            forward = forward -1
            backward = backward -1
        else:
            print("This is not a valid option.")

        if backward == 0:
            stoned_area()
    
        if forward == 5:
            cliff_scene()

def walkin_path_two():
    print("\nWalk along the Beach\n")
    forward = 0
    backward = 1
    options = ["1", "2", "3"]
    userinput = ""
    while userinput not in options or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back")
        userinput = input(">")
        if userinput == "1":
            print("""Your eyes are wandering along the beach. As far your eyes can see, you see only water till the horizont. There is nothing much to see here
beside the sand and some shells on the beach. The trees in the jungle are so narrow that there is no path into it. 
Its probably the best to not stay too long in this burning sun.
What is your next step?\n""")
        elif userinput == "2":
            forward = forward +1
            backward = backward +1
        elif userinput == "3":
            forward = forward -1
            backward = backward -1
        else:
            print("This is not a valid option.")

        if backward == 0:
            cliff_scene()
            
        if forward == 5:
            stoned_area()
