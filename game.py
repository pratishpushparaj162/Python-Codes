import random

def game(a, b):
    if a == b:
        return None
    elif a == "s":
        if b == "p":
            return 0
        elif b == "k":
            return 1
    elif a == "p":
         if b == "s":
            return 0
         elif b == "k":
            return 1
    elif a == "k":
         if b == "p":
            return 0
         elif b == "s":
            return 1


randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    a = "s"
elif randNo == 2:
    a = "p"
elif randNo == 3:
    a = "k"
print("Comp Turn: Stone(S) Paper(p) or Scissors(k)?")
b = input("Player's Turn: Stone(s) Paper(p) Scissors(k)? ")
z = game(a, b)
print(f"Computer chose {a}")
print(f"Your chose {b}")

if z == None:
    print("The game is a tie!")
elif z:
    print("You Win!")
else:
    print("You Lose!")
