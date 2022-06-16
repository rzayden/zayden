#v1.3
#Zayden Kelsen
#17/6/22
# the code welcomes the user and tells the user it will have 1 chance to guess correctly
print("welcome to my teo reo quiz!")

#chances
chances = 1 
print("you will have", chances, "chance to answer correctly. \n")

#score
score = 0
#v1.2
#Zayden Kelsen
#17/6/22
# the code asks the user a question and if they get the question correct or incorrect the code will say good job or incorrect and it will tell them the answer
#question 1
question_1 = print(" 1) what is red in teo reo?\n(a) whero\n(b) tino\n(c) panui\n(d) huarahi\n\n ")

answer_1 = "a"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")
#v1.1
  #Zayden Kelsen
  #17/6/22
  #this code will ask the user a simple teo reo question and if the user gets it correct or worong the code will tell them
#question 2
question_2 = print(" 2) what is hi in teo reo?\n(a) teitei\n(b) harikoa\n(c) kia ora\n(d) hei\n\n ")

answer_1 = "c"

for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")
#v1.0
  #Zayden Kelsen
  #17/6/22
  # the code will ask the user a question and if the user gets the question right the code will say "correct! good job" and if the user gets the question wrong it will tell the user incorrect then the code will tell them the correct answer
#question 3
question_3 = print(" 3) what is greetings in teo reo?\n(a) ata pai\n(b) tena koutou\n(c) paru\n(d) tere\n\n ")

answer_1 = "b"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")
#v1.2
  #Zayden Kelsen
  #17/6/22
  # the user will get asked a question if the user gets it correct or incorrect the code will say correct or incorrect
#question 4
question_4 = print(" 4) what is family in teo reo?\n(a) rongonui\n(b) kei hea\n(c) tere\n(d) whanau\n\n ")

answer_1 = "d"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")
#v1.1
  #Zayden Kelsen
  #17/6/22
  # the code will give the user a question and the code will tell them if they got ir correct or incorrect

  
#question 5
question_1 = print(" 5) what is good morning in teo reo?\n(a) ata pai\n(b) neke\n(c) tangata\n(d) morena\n\n ")

answer_5 = "d"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")

print("Thanks for playing my teo reo quiz!")
