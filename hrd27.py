def doSolution(n, k, a):
    print str(n) + " " + str(k)
    print " ".join(map(str, a))

numTests = 5
print numTests
doSolution(4, 3, [-1, 0, 4, 2])
doSolution(5, 2, [0, -1, 2, 1, 4])
doSolution(7, 6, [2, 0, -1, 1, 1, 1, 1])
doSolution(3, 1, [-1, 0, 4])
doSolution(6, 4, [0, -1, 1, 4, 5, 6])