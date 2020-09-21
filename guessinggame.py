import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer) #TODO: remove after testing
guess = 0 # initialise to any number that doesnt = answer
print("Please guess an answer between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("You got it!")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("Please guess lower")