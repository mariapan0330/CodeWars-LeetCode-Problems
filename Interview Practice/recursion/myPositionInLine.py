# RECURSION:
# 1. What is the least amount of work I can do?
# 2. When would the process be complete?

def getMyPositionInLine(person):
    if person.nextInLine == None:
        return 1
    return 1 + getMyPositionInLine(person.nextInLine)


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.nextInLine = None

p1 = Person('p1!')
p2 = Person('p2!')
p3 = Person('p3!')
p4 = Person('p4!')
p5 = Person('p5!')
p6 = Person('p6!')
p7 = Person('p7!')
p8 = Person('p8!')

p1.nextInLine = p2
p2.nextInLine = p3
p3.nextInLine = p4
p4.nextInLine = p5
p5.nextInLine = p6
p6.nextInLine = p7
p7.nextInLine = p8

# print(p1.nextInLine.name)
print(getMyPositionInLine(p3))