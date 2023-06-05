import session

# Introduce game setting and ask/save user name
def introduction():
    print(
    "Welcome to the Survival Game!\n"
    "サバイバルゲームへようこそ\n"
    "First of all, lets start with entering your name.\n"
    )
    session.session["username"] = input("My name is ")
    print(
    "Very well, " + session.session["username"] + " let your journey begin.\n\n"
    "Beach Startscene\n\n"
    "You wake up and you cant remember where you are or how you got there. You try to remember what happened but the moment you try, your head starts hurting really bad. You look around and you notice that you are on a beach. According to the sun its probably early afternoon. When you take a look at yourself, you noticed that your clothes are damaged and you are injured on your left arm and blood keeps dripping out of the wound.\n"
    "What are you going to do?\n"
    )
    return