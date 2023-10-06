# I write an essay and it goes through revision process:
# read it over
# get feedback from professor
# apply changes to the essay
# revise again until the essay is satisfactory

grade = 0
goal_grade = 100

class Essay:
    def __init__(self, grade) -> None:
        self.grade = grade
        self.goal_grade = 100
    
    def isComplete(self):
        print(self.grade >= self.goal_grade)
        return self.grade >= self.goal_grade


def revise(essay):
    read(essay)
    recieve_feedback_on(essay)
    apply_changes_to(essay)
    if not essay.isComplete():
        revise(essay)

def read(essay): 
    essay.grade += 1

def recieve_feedback_on(essay): 
    essay.grade += 1

def apply_changes_to(essay): 
    essay.grade += 1


my_essay1 = Essay(0)
print(revise(my_essay1))