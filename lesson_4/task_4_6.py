months = 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
         'August', 'September', 'October', 'November', 'December'
if 0 <= (season := int(input('input number of month: ')) - 1) <= 11:
    if 2 <= season <= 4:
        print('Spring', months[season])
    elif 5 <= season <= 7:
        print('Summer', months[season])
    elif 8 <= season <= 10:
        print('Fall', months[season])
    else:
        print('Winter', months[season])
else:
    print('input number from 1 to 12')
