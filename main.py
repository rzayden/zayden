print("welcome to my teo reo quiz!")

#chances
chances = 1 
print("you will have", chances, "chance to answer correctly. \n")

#score
score = 0

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

