import re


if __name__ == '__main__':
    text = '''Примеры расширений файлов:
    wald.jpeg
    wow.mp4
    book.txt
    forest.png
    fox.tiff
    wood.pdf
    hub.gif
    small.zip
    sound.mp3
    '''
    res = re.findall(r'(\w+[.])(jpeg|png|tiff|gif)', text)
    for pic in res:
        print(''.join(pic))

    res = re.findall(r'\w+.jpeg|\w+.png|\w+.tiff|\w+.gif', text)
    print(*res, sep='\n')

