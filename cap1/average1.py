# Ask for user to insert numbers
# Print the numbers, the amount of numbers, the sum, the min and max and the mean value

numbers = []
total = 0

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
    except ValueError as err:
        print(err)

if numbers:
    print(numbers)
    print('count:', len(numbers), 'sum:', sum(numbers), 'lowest:',
    min(numbers), 'highest:', max(numbers), 'mean:', sum(numbers) // len(numbers))