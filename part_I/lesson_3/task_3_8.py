words = ['четырёхсотпятидесятисемимиллиметровое',
         'метоксихлордиэтиламинометилбутиламиноакридин',
         'автомотовелофототелерадиомонтёр',
         'автоэлектростеклоподъемники']
for word in words:
    print(word, word.count(word[0]) + word.count(word[-1]))