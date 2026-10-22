# function
def listen():
    # sound
    print("What sound did you hear? ")
    sound = input()

    print(f"That was a loud {sound}!")


listen()


# new code
def identify():
    print("What lies before us? ")
    response = input()

    if response == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


identify()


# new code
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("Not sure about that plan")


escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")


# cross bridge
def cross_bridge(steps):
    for step in range(steps):
        print("Crossed step")
    if steps > 5:
        print("The bridge is collapsing")
    else:
        print("We must keep going!")


cross_bridge(3)
cross_bridge(6)


# new code
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)


# new code
def display_ladder(steps):
    for step in range(steps):
        print("| |\n*** ")
    print("| |")


def create_ladder():
    print("How many steps remain? ")
    steps = int(input())
    display_ladder(steps)


create_ladder()


# new code
def sum_weights(person_weight, inventory_weight):
    total_weight = person_weight + inventory_weight
    return total_weight


def calc_avg_weights(person_weight, inventory_weight):
    avg_weight = sum_weights(person_weight, inventory_weight) / 2
    return avg_weight


def run():
    print("What is the weight of the person? ")
    person_weight = float(input())
    print("What is the weight of the inventory? ")
    inventory_weight = float(input())

    print("What would you like to calculate (sum or average)? ")
    action = input()

    if action == "sum":
        answer = sum_weights(person_weight, inventory_weight)
        print(f"The sum of the weight is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weights(person_weight, inventory_weight)
        print(f"The average of the weight is {answer:.2f}")
    else:
        print("I'm not sure what you would like me to do")


run()


# new code
print("Please provide a word: ")
word = input()

def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"|{word}|")
    print("-" * num_dashes)


def display_lower_case(word):
    print(word.lower())


def display_upper_case(word):
    print(word.upper())


def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")

def display_repeated(word):
    print("How many times would you like to repeat?")
    repetitions = int(input())

    for repetitions in range(repetitions):
        if (repetitions%2==0):
            print(display_lower_case(word))
        else:
            print(display_upper_case(word))

def run():
    print("What would you like to do with this word? ")
    print("[1] Display in a box")
    print("[2] Display a lower-case")
    print("[3] Display a upper-case")
    print("[4] Display a mirrored")
    print("[5] Display a repeated")
    print("[6] Quit")

    response=int(input())
    if response == 1:
        display_box(word)
    elif response == 2:
        display_lower_case(word)
    elif response == 3:
        display_upper_case(word)
    elif response == 4:
        display_mirrored(word)
    elif response == 5:
        display_repeated(word)
    else:
        print("Unknown option")

run()

# new code
import random

print("please enter a minimum value: ")
min = int(input())
print("please enter a maximum value: ")
max = int(input())

random_num = random.randrange(min, max)
print(f"I'm thinking of a number between {min} and {max}.")
print("can you guess what it is? ")

guessed_correctly = False
while not guessed_correctly:
    print("Please enter a number: ")
    guess = int(input())

    if guess == random_num:
        print("Congratulations! You guessed the number!")
        guessed_correctly = True
    elif guess < random_num:
        print("Guess higher!")
    else:
        print("Guess lower!")
print("Game over")
