from colorama import Fore
from transliterate import translit


class Film:
    def __init__(self, movie, name, surname):
        self.movie = movie
        self.name = name
        self.surname = surname
        self.show_creds()

    def show_creds(self):
        print(
            f"\t{Fore.RED}{self.movie}{Fore.RESET} -  в главной роли {Fore.GREEN}{self.name} {self.surname}{Fore.RESET}")


class FilmWorld(Film):
    def show_creds(self):
        self.movie = translit(self.movie, reversed=True)
        self.name = translit(self.name, reversed=True)
        self.surname = translit(self.surname, reversed=True)
        super().show_creds()


if __name__ == '__main__':
    films_rus = {'Бриллиантовая рука': ('Юрий', 'Никулин'),
                 'Сталкер': ('Александр', 'Кайдановский'),
                 'Соляриc': ('Донатас', 'Банионис'),
                 'Гадкие лебеди': ('Григорий', 'Гладий'),
                 'Свадьба в Малиновке': ('Владимир', 'Самойлов'),
                 'Убить дракона': ('Александр', 'Абдулов'),
                 'Город Зеро': ('Леонид', 'Филатов'),
                 'Бакенбарды': ('Виктор', 'Сухоруков'),
                 'Стиляги': ('Антон', 'Шагин')}
    films_world = {'Бойцовский клуб': ('Эдвард', 'Нортон'),
                   'Тропик рака': ('Рип', 'Торн'),
                   'Имена людей': ('Жак', 'Гамблен'),
                   'Соседи сверху': ('Хавьер', 'Камара'),
                   'Не смотри вниз': ('Антонелла', 'Коста'),
                   'Мир дикого запада': ('Юл', 'Бриннер'),
                   'Из машины': ('Донал', 'Глисон'),
                   'Город женщин': ('Марчелло', 'Мастроянни'),
                   'Омерзительная восмерка': ('Курт', 'Рассел'),
                   'Сало, или 120 дней Содома': ('Паоло', 'Боначелли')}
    for title, data in films_rus.items():
        Film(title, *data)
    print()
    for title, data in films_world.items():
        FilmWorld(title, *data)


