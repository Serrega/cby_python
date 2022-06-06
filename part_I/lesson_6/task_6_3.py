input_text = input('Input text: ')
word = 'predator'
result = lambda x: 'больше' if len(input_text) > len(word) else 'меньше'
print('Это слово', result(input_text), 'чем', word)
