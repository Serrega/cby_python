targets = ["7 раз отмерь, 1 раз отрежь.",
           "Не имей 100 рублей, а имей 100 друзей.", "1 за всех и все за 1."]
for line in targets:
    summa = 0
    for word in line[:-1].split(' '):
        if word.isdigit():
            summa += int(word)
    print(line, summa)
