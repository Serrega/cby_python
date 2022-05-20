while not ((num := (input('Enter a number: '))).isdigit() and 10 <= int(num) <= 20):
    print('Mistake! you entered a number out of range')
print('We work with number', num)
