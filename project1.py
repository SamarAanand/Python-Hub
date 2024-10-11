import random

def gamewin(comp, you):
    if you == comp:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "g":
        if you == "w":
            return False
        elif you == "s":
            return True
    elif comp == "w":
        if you == "g":
            return True
        elif you == "s":
            return False

print("compturn: snake(s), water(w), or gun(g)")
randno = random.randint(1, 3)

if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 3:
    comp = "g"

you = input("your turn: snake(s), water(w), or gun(g)? ")

a = gamewin(comp, you)

if a is None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")

print(f"Computer chose {comp}, and you chose {you}.")
