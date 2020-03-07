errormessage = "Error, please enter numeric input"

hours = input('Enter Hours:')
try:
    float(hours)>=0
except:
    print(errormessage)
    hours = input('Enter Hours:')

rate = input('Enter Rate:')
try:
    float(rate)>=0
except:
    print(errormessage)
    rate = input('Enter Rate:')

hours = float(hours)
rate = float(rate)

if hours > 40:
    overtime = hours - 40
else :
    overtime = 0

overtimepay = 0.5 * rate * overtime
pay = hours * rate + overtimepay

print('Pay:' + str(pay))
