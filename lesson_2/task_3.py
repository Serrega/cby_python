num_of_devices = 1000
lost_devices_per_day = -2
add_devices_per_day = 3
days = 30

new_num_device_without_added = num_of_devices + lost_devices_per_day*days
print("num of divices after", days, " days without added: ",
      new_num_device_without_added)

new_num_device_with_added = new_num_device_without_added + \
                            add_devices_per_day*days
print("num of divices after", days, " days with added: ",
      new_num_device_with_added)

