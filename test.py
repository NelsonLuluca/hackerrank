
from collections import deque

dq = deque()
sq = deque()

sq.appendleft('b')
sq.appendleft('o')
sq.appendleft('y')

dq.extend('b')
dq.extend('o')
dq.extend('y')

print("stack")
print(sq)

print('queue')
print(dq)

print("element1 %s %s" % (sq.popleft(), dq.popleft()))
print("element2 %s %s" % (sq.popleft(), dq.popleft()))
print("element3 %s %s" % (sq.popleft(), dq.popleft()))