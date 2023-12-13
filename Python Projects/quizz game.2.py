print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okey! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect")

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
   print('Correct!')
   score+=1
else:
   print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
    
answer = input("What does ROM stand for? ")
if answer.lower() == "Read Only Memory":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")


answer = input("What does ATM stand for? ")
if answer.lower() == "Auto Mated Teller Mechine":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer = input("What does NEWS stand for? ")
if answer.lower() == "North East West South":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions Correct!")
print("You got " + str((score / 7) * 100) + "%")




