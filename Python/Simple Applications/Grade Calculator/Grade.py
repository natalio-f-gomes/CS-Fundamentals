class Grade:
    def __init__(self, midterm, final, quiz, lab):
        self.midterm = midterm
        self.final = final
        self.quiz = quiz
        self.lab = lab

    def grades_weight(self):
        self.m_weight = (self.midterm / 100) * 25
        self.f_weight = (self.final / 100) * 25
        self.q_weight = (self.quiz / 120) * 10
        self.l_weight = (self.lab / 130) * 40
        overall = self.m_weight + self.f_weight + self.q_weight + self.l_weight
        '''return f"Midterm: {self.m_weight}"
        return f"Final: {self.f_weight}"
        return f"Quiz: {self.q_weight}"
        return f"Lab Projects: {self.lab}"'''
        return f"Overall Grade is : {overall: .2f}"
