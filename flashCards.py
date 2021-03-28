#Creating the card class - each card has a question, answer, and an optional alternate answer
class Card:
	question = ""
	answer = ""
	altAnswer = ""
	
	def __init__(self,q,a):
		self.question = q
		self.answer = a
	def __init__(self,q,a,aa):
		self.question = q
		self.answer = a
		self.altAnswer = aa
		
	def changeQuestion(self,q):
		self.question = q
	
	def changeAnswer(self,a):
		self.answer = a
		
	def changeAltAnswer(self,aa):
		self.altAnswer = aa
		
#--------------------------------------------------------------------------------------------------------------

#Creating president deck

#Special 3 cases for list elements than don't end in -th, then loop
numPres = 46
presidentQuestions = [""]*(numPres+1)
presidentQuestions[0] = "" #start all arrays at 1, to make searching easier
presidentQuestions[1] = "Who was the 1st president? "
presidentQuestions[2] = "Who was the 2nd president? "
presidentQuestions[3] = "Who was the 3rd president? "
for i in range(4,numPres+1):
	presidentQuestions[i] = "Who was the "+str(i)+"th president? "

presidentAnswers = ["","George Washington","John Adams","Thomas Jefferson","James Madison","James Monroe","John Adams","Andrew Jackson","Martin Van Buren","William Harrison","John Tyler",
"James Polk","Zachary Taylor","Millard Fillmore","Franklin Pierce","James Buchanan","Abraham Lincoln","Andrew Johnson","Ulysses Grant","Rutherford Hayes","James Garfield","Chester Arthur",
"Grover Cleveland","Benjamin Harrison","Grover Cleveland","William McKinley","Theodore Roosevelt","William Taft","Woodrow Wilson","Warren Harding","Calvin Coolidge","Herbert Hoover",
"Franklin Roosevelt","Harry Truman","Dwight Eisenhower","John Kennedy","Lyndon Johnson","Richard Nixon","Gerald Ford","Jimmy Carter","Ronald Reagan","George Bush","Bill Clinton",
"George Bush","Barack Obama","Donald Trump","Joe Biden"]

presidentAltAnswers = ["","Washington","Adams","Jefferson","Madison","Monroe","Adams","Jackson","Van Buren","Harrison","Tyler","Polk","Taylor","Fillmore","Pierce","Buchanan","Lincoln",
"Johnson","Grant","Hayes","Garfield","Arthur","Cleveland","Harrison","Cleveland","McKinley","Roosevelt","Taft","Wilson","Harding","Coolidge","Hoover","Roosevelt","Truman","Eisenhower",
"Kennedy","Johnson","Nixon","Ford","Carter","Reagan","Bush","Clinton","Bush","Obama","Trump","Biden"]

presidentCards = [Card("","","")] * len(presidentQuestions)

#Create president cards - from 1=George Washington to 46=Joe Biden
for i in range(1,numPres+1):
	presidentCards[i] = Card(presidentQuestions[i], presidentAnswers[i], presidentAltAnswers[i])
	
#--------------------------------------------------------------------------------------------------------------

#Ask questions in random order, keeping score
correctNum = 0
askedNum = 0
lastResponse = -1
response = ""
while response.lower().strip() != "quit":
	#generate random question number, ask user, check if correct
	import random
	questionNum = random.randint(1,len(presidentQuestions)-1) 
	#prevent same question twice consecutively
	while questionNum == lastResponse:
		questionNum = random.randint(1,len(presidentQuestions)-1) 
	lastResponse = questionNum
	
	userResponse = input(presidentCards[questionNum].question)
	
	if userResponse.lower().strip() == presidentCards[questionNum].answer.lower() or userResponse.lower().strip() == presidentCards[questionNum].altAnswer.lower(): 
		askedNum += 1
		correctNum += 1
		percentGrade = 100.00*(correctNum/askedNum)
		print("Correct! Grade so far: " + str(correctNum) + "/" + str(askedNum) + " (" + str(round(percentGrade,2)) + "%)" + "\n")
	#quit
	elif userResponse.lower().strip() == "quit":
		percentGrade = 100.00*(correctNum/askedNum)
		print("Final grade: " + str(correctNum) + "/" + str(askedNum) + " (" + str(round(percentGrade,2)) + "%)")
		break
	#incorrect answer
	else:
		askedNum += 1
		percentGrade = 100.00*(correctNum/askedNum)
		print("Incorrect! The correct answer is " + presidentCards[questionNum].answer + 
		".\n Grade so far: " + str(correctNum) + "/" + str(askedNum) + " (" + str(round(percentGrade,2)) + "%)""\n")