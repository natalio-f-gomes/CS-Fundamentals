class Quizz:
    def __init__(self):

        self.prompt = {"What is 1+1:": "2",
                  "What is 1+3:": "4",
                  "What is 1+5:": "6",
                  "What is 1+7:": "8",}
        self.questions = [x for x in self.prompt.keys()]
        self.answers = [x for x in self.prompt.values()]
        self.score = 0
    def Menu(self):
        while True:
            user_input=input("""
            1 - Play Game
            2 - Add Questions and answers
            3 - Exit
            """)
            if user_input == "1":
                self.Game()
            elif user_input == "2":
                num = int(input("How many questions or answers would you like to input: "))
                self.addQuestions(num)
            elif user_input == "3":
                break;
            else:
                self.Menu()

    def Game(self):
        for question, answer in zip(self.questions, self.answers):
            user_input = input(question + ": ")
            if(user_input==answer):
                self.score+=1
        print("Your Score was: ", self.score, "out of ",len(self.answers))


    def addQuestions(self,num):
        for i in range(num):
            question = input("Enter a question")
            answer = input("Enter the answer for the question: ")
            self.prompt[question] = answer


