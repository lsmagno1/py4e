errormessage = "Error, please enter numeric input"

def computepay(hours, rate):

    hours = hours
    try:
        float(hours)>=0
    except:
        print(errormessage)

    rate = rate
    try:
        float(rate)>=0
    except:
        print(errormessage)

    hours = float(hours)
    rate = float(rate)

    if hours > 40:
        overtime = hours - 40
    else :
        overtime = 0

    overtimepay = 0.5 * rate * overtime
    pay = hours * rate + overtimepay

    print('Pay:' + str(pay))

computepay(45,10)
