names = ('Ваня', 'Даня', 'Саня')
actions = ('учит', 'знает', 'выбирает')
languages = ('Python', 'PHP', 'C#')
for name in names:
    for act in actions:
        for lang in languages:
            print(name, act, lang)
