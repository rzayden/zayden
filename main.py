print("welcome to my teo reo quiz!")

#chances
chances = 1 
print("you will have", chances, "chance to answer correctly. \n")

#score
score = 0

#question 1
question_1 = print(" 1) what is red in teo reo?\n(a) whero\n(b) tino\n(c) panui\n(d) huarahi\n\n ")

answer_1 = "whero"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")

  
#question 2
question_2 = print(" 2) what is hi in teo reo?\n(a) teitei\n(b) harikoa\n(c) kia ora\n(d) hei\n\n ")
answer_1 = "c"
answer_1 = "kia ora"

for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")


#question 3
question_3 = print(" 3) what is greetings in teo reo?\n(a) ata pai\n(b) tena koutou\n(c) paru\n(d) paru\n\n ")

answer_1 = "tena koutou"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")


#question 4
question_4 = print(" 4) what is family in teo reo?\n(a) rongonui\n(b) kei hea\n(c) tere\n(d) whanau\n\n ")

answer_1 = "whanau"
for i in range(chances) :
    answer = input("answer: ")
    if (answer.lower() == answer_1):
       print("correct! Good Job. \n")
       score = score + 1
       break
else:
  print("incorrect!\n ")
  print("The correct answer is" , answer_1, "\n\n ")


#question 5
question_5 = print(" 5) what is good morning in teo reo?\n(a) ata pai\n(b) neke\n(c) tangata\n(d) moringa\n\n ")

answer_1 = "moringa"
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