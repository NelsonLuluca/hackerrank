class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        scoreTotal = 0
        for i in range(len(self.scores)):
            scoreTotal += self.scores[i]
        scoreAverage = scoreTotal / len(self.scores)
        letter = 'T'
        if (scoreAverage >= 90 and scoreAverage <= 100):
            letter = 'O'
        elif (scoreAverage >= 80 and scoreAverage < 90):
            letter = 'E'
        elif (scoreAverage >= 70 and scoreAverage < 80):
            letter = 'A'
        elif (scoreAverage >= 55 and scoreAverage < 70):
            letter = 'P'
        elif (scoreAverage >= 40 and scoreAverage < 55):
            letter = 'D'
        else:
            letter = 'T'
        return letter

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
