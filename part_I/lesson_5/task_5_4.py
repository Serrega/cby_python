jewels = ('золото', 'алмазы', 'серебро', 'сапфиры', 'бронза',
          'рубины', 'платина', 'изумруды', 'палладий', 'аметисты')
for position in range(2):
    for index, jewel in enumerate(jewels[position::2], start=1):
        print(index, jewel)
    print()
