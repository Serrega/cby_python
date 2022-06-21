import re

if __name__ == '__main__':
    text = 'Московское время 10:36:06'
    res = re.search(r'(\d+:){2}\d+', text)
    print(res.group())

