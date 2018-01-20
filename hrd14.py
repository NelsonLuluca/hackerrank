
class Difference:
    def __init__(self, a):
        self.__elements = a


# Add your code here
    def computeDifference(self):
        theMax = 1
        for i in range(len(self.__elements)):
            if (self.__elements[i] > theMax):
                theMax = self.__elements[i]
        self.maximumDifference = 0
        for i in range(len(self.__elements)):
            currDiff = theMax - self.__elements[i]
            if (currDiff > self.maximumDifference):
                self.maximumDifference = currDiff


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference