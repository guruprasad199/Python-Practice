import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True



print("comp's turn Enter the Gun(g) snake(s) and water(w) : ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Enter the Gun(g) snake(s) and water(w) : ")






a = gameWin(comp, you)

print(f"com chooes the {comp}")
print(f"you chooes the {you}")



if a == None:
    print("game is tie")
elif a :
    print("you win")



