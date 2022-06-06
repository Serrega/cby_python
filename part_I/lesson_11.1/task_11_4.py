def digit_text(fun):
    def printing(text):
        first_line = "+-" * len(text) + "+"
        second_line = "|" + "|".join(text) + "|"
        print("\n".join((first_line, second_line, first_line)))
    return printing


@digit_text
class Text:
    def __init__(self, text: str):
        self.text = text
        print(self.text)


if __name__ == '__main__':
    Text('Easy Task')
