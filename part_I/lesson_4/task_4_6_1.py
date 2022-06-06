months = 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
         'August', 'September', 'October', 'November', 'December'
if 2 <= (season := int(input('input number of month: ')) - 1) <= 4:
    print('Spring', months[season])
elif 5 <= season <= 7:
    print('Summer', months[season])
elif 8 <= season <= 10:
    print('Fall', months[season])
elif 0 <= season <= 1 or season == 11:
    print('Winter', months[season])
else:
    print('input number from 1 to 12')
