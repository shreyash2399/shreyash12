print("Welcome to quiz game with computer")

playing=input("Do you want to play the quiz game? ")

# if playing == 'yes':
#     print("Okay lets play")

# else: 
#     print("Quit")
if playing.lower() != "yes":
    quit()

print("Okay,Let's play the game")
score=0

a= input("What does stand for cpu: ")
if a.lower() == 'central processing unit':
    print("Correct")
    score+=1
else:
    print("Incorrect")

a= input("What does stand for gpu: ")
if a.lower() == 'graphics processing unit':
    print("Correct")
    score+=1
else:
    print("Incorrect")

a= input("What does stand for ram: ")
if a.lower() == 'random access memory':
    print("Correct")
    score+=1
else:
    print("Incorrect")

a= input("What does stand for psu: ")
if a.lower() == 'power supply':
    print("Correct")
    score+=1
else:
    print("Incorrect")

print ("You got " + str(score) + " questions correct" )
