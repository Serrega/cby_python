man_speed = 4*1000/3600
auto_speed = 30
auto_time = 10*60
current_man_time = 2*3600

town_distance = auto_speed * auto_time
man_time = town_distance / man_speed
left_man_time_in_minutes = (man_time - current_man_time)/3600

print("time left for man:", left_man_time_in_minutes, " hours")

