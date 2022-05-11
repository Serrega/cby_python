target_dict = {'o': 3, 'd': 7, 'k': 5, 'w': 2, 'e': 6, 'g': 1, 'y': 4}
print(''.join(list(target_dict.keys())[::2]))
print('sum target_dict values is:', sum(target_dict.values()))
print('sorted list target_dict values is:', sorted(target_dict.values()))
print('sum of third values is:', sum((list(target_dict.values()))[::3]))
