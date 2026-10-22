#function
def listen():

    #sound
    print("What sound did you hear? ")
    sound=input()

    print(f"That was a loud {sound}!")
listen()

#new code
def identify():

    print("What lies before us? ")
    response=input()

    if response=="a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")
identify()

#new code
def escape_by(plan):
    if plan=="jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan=="running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan=="cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("Not sure about that plan")
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

