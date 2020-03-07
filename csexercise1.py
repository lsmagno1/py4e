hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))

if hours > 40:
    overtime = hours - 40
else :
    overtime = 0

overtimepay = 0.5 * rate * overtime
pay = hours * rate + overtimepay

print('Pay:' + str(pay))
