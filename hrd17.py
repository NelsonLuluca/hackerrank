

#Write your code here

class Calculator:
    def power(self, n, p):
        try:
            assert (n >= 0 and p >= 0)
            return pow(n,p)
        except:
            raise Exception('n and p should be non-negative')




myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e    
    