
import sys

#lines = sys.stdin.readlines

i = 4
d = 4.0
s = 'HackerRank '

mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())


theTip = mealCost * (tipPercent / 100.00)
theTax = mealCost * (taxPercent / 100.00)

print ("Meal Cost: %.2f" % mealCost)
print ("TIP: %d Amount %.2f" % (tipPercent, theTip))
print ("TAX: %d Amount %.2f" % (taxPercent, theTax))

total_cost = int(round(mealCost + tipPercent + tax_percent))


print ("Total: %d" % round(mealCost + theTip + theTax))


       
