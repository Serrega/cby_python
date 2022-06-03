import pyfiglet


def my_digital_output(text: str):
    contur = '+-'*len(text) + '+\n'
    text = contur + ''.join(['|' + i for i in text]) + '|\n' + contur
    return text


result = pyfiglet.figlet_format("Pentester", font="digital")
print(result)

print(my_digital_output('Easy Task'))


def printing(text):
    first_line = "+-"*len(text) + "+"
    second_line = "|" + "|".join(text) + "|"
    return "\n".join((first_line, second_line, first_line))