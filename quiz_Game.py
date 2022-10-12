print("Welcome to this computer quiz! ")
playing = input("Do you want to continue? " "Yes or No :")

if playing != "yes" :
    quit()

print("Oky, let's go!")
score = 0

answer = input("What is the acronym of central processing unit? ")
if answer.upper() == "CPU":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
#//////////////////////////////////////////////////////////////////////////////////////////////    
answer = input("What is the acronym of graphing processing unit? ")
if answer.upper() == "GPU":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
#//////////////////////////////////////////////////////////////////////////////////////////////    
answer = input("What is the acronym of random acces memory? ")
if answer.upper() == "RAM":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
#//////////////////////////////////////////////////////////////////////////////////////////////    
answer = input("What is the acronym of power supply? ")
if answer.upper() == "PGU":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("your score is: " + str(score))
print("your score in porcentage is: "+ str((score/4)*100)+"%")