word_1 = input('input first word: ')
if set(word_2 := input('input second word: ')) == set(word_1):
    print(f'words "{word_1}" and "{word_2}" are consist of the same letters')
else:
    print('these words aren\'t consist of the same letters')

