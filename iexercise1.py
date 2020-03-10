total = 0
count = 0
error = "Invalid input"

while True:
    line = input('Enter number: ')
    if line == 'done':
        print (total, count, total/count)
        break
    else:
        try:
            total += float(line)
            count += 1
        except:
            print (error)
            continue
