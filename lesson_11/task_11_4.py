from colorama import Back


class ColorMe:
    _colours = {'1)': 'Green',
                '2)': 'Blue',
                '3)': 'Red',
                '4)': 'Purple'}
    __back = (Back.RESET, Back.GREEN, Back.BLUE, Back.RED, Back.MAGENTA)

    def menu(self):
        for ind, color_name in self._colours.items():
            print(ind, color_name)

    def print_string(self, color_num, text):
        print(self.__back[color_num] + text + self.__back[0])


p = ColorMe()
p.menu()
color = int(input('\nEnter colour: '))
string = input('Enter string: ')
p.print_string(color, string)



