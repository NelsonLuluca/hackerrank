from datetime import date

line1=raw_input().strip().split(' ')
line2=raw_input().strip().split(' ')

actualDay = line1[0]
actualMonth = line1[1]
actualYear = line1[2]

expectedDay = line2[0]
expectedMonth = line2[1]
expectedYear = line2[2]

actualString = "%s/%s/%s" % (actualDay, actualMonth, actualYear)
expectedString = "%s/%s/%s" % (expectedDay, expectedMonth, expectedYear)

e_date = date(int(expectedYear), int(expectedMonth), int(expectedDay))
a_date = date(int(actualYear), int(actualMonth), int(actualDay))

daysLate = 0
if a_date > e_date:
    #print("You are late")
    #print("ACT: %s" % a_date)
    #print("EXP: %s" % e_date)
    dayDiff = a_date - e_date
    daysLate = dayDiff.days
else:
    #print("NOT LATE")

monthsLate = 0
if int(actualMonth) > int(expectedMonth):
    monthsLate = int(actualMonth) - int(expectedMonth)

#print("DAYS LATE: %d" % daysLate)

fine = 0
#if actualYear > expectedYear:
#    fine = 10000
#elif actualMonth > expectedMonth:
if actualYear == expectedYear:
    if actualMonth == expectedMonth:
        fine = 15 * daysLate
    else:
        fine = 500 * monthsLate
else:
    if actualYear > expectedYear:
        fine = 10000

print(fine)


