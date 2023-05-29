from scenes import *

# moved items from scenes.py into global scope of main
items = {"plastic_bottle": False, "piece_of_wood": False, "glass_bottle": False}

# Moved everything into main function
def main():
    print("Welcome to the Survival Game!\nサバイバルゲームへようこそ")
    print("First of all, lets start with entering your name.")
    name = input("My name is ")
    print("\nVery well, " +name+ " let your journey begin.\n")

    print("Beach Startscene\n")
    print("""You wake up and you cant remember where you are or how you got there.
    You try to remember what happened but the moment you try, your head starts hurting really bad.
    You look around and you notice that you are on a beach. According to the sun its probably early afternoon.
    When you take a look at yourself, you noticed that your clothes are damaged and you are injured 
    on your left arm and blood keeps dripping out of the wound.\nWhat are you going to do?\n""")      

    # Beach now takes a parameter which here is the items dict. Has to take it as a parameter
    beach(items)

# Using if __name__ to detect when the file is being run directly as opposed to being imported
if __name__ == '__main__':
    # Run main function
    main()
