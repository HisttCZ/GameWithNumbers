import random

print("Welcome in game with numbers")
print("Wanna see rules?")
rulesshow=input()

if rulesshow=="Yes":
    print("Game generate number,who you must guess.")

print("Chosse difficulty:(Eazy,medium,hard)")
diff=input()
pocet=5

if diff == "hard":
    pocet=30
elif diff == "medium":
    pocet=15
n=random.randint(1,pocet)
print("How many atteps you want:")
att=int(input())
for i in range(att):
    print("Write number:")
    guestnum=int(input())
    

    if guestnum==n:
        print("Right number!")
        break
    

    else:
        print("Bad number!")
        if guestnum<n:
            print("Number is bigger")
            
        if guestnum>n:
            print("Number is less")
