line = input('Enter a number: ')
number = float(line)
minimum = number
maximum = number

while True:
    line = input('Enter a number: ')
    if line == 'done':
        break

    number = float(line)
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print ('Maximum: ' + str(maximum))
print ('Minimum: ' + str(minimum))
