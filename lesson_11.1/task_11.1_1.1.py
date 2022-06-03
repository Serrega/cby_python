import ast
from colorama import Fore
from transliterate import translit


class Film:
    def __init__(self, num_films: int):
        self.num = num_films
        self.films = self.create_dict()

    def __repr__(self) -> str:
        return str(self.films)

    def create_dict(self) -> dict:
        dict_films = {}
        for _ in range(self.num):
            title = input(f'введите название фильма: ')
            data = (input('имя актера: '), input('фамилия актера: '))
            dict_films[title] = data
        return dict_films

    def print_param(self, films):
        for title, (name, surname) in ast.literal_eval(films).items():
            print(f"\t{Fore.RED}{title}{Fore.RESET} -  в главной роли "
                  f"{Fore.GREEN}{name} {surname}{Fore.RESET}")


class FilmWorld(Film):
    def print_param(self, films):
        for title, (name, surname) in ast.literal_eval(films).items():
            print(f"\t{Fore.RED}{translit(title, reversed=True)}{Fore.RESET} -  "
                  f"в главной роли {Fore.GREEN}{translit(name, reversed=True)} "
                  f"{translit(surname, reversed=True)}{Fore.RESET}")


if __name__ == '__main__':
    num_rus = int(input('Сколько будет русских фильмов: '))
    num_word = int(input('Сколько будет зарубежных фильмов: '))
    film = Film(num_rus)
    film_world = FilmWorld(num_word)
    film.print_param(repr(film))
    print()
    film_world.print_param(repr(film_world))


