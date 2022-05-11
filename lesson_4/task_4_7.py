ours, minutes = input('input time in format oo:mm ').split(':')
time_in_minutes = int(ours)*60 + int(minutes)
if 360 <= time_in_minutes <= 1080:
    sun_angle = (time_in_minutes - 360)/4
    print('sun angle is: ', sun_angle, ' degrees')
else:
    print('Sun is under of skyline')
