hours = int(input('Enter Hours:'))
rate = int(input('Enter Rate:'))

if hours > 40:
    overtime = float(hours) - 40
else :
    overtime = 0

overtimepay = 0.5 * float(rate) * overtime
pay = float(hours) * float(rate) + overtimepay

print('Pay:' + str(pay))
