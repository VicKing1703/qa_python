from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # в коде класса нет метода books_rating, был заменён на метод get_books_genre
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 2 добавление жанра 'Ужасы' книге
    def test_set_book_genre_add_from_book_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Кристина')
        collector.set_book_genre('Кристина', 'Ужасы')
        assert collector.books_genre('Кристина') == 'Ужасы'

    # 3 показ книги по жанру 'Фантастика'
    def test_get_books_with_specific_genre_get_genre_fiction(self):
        collector = BooksCollector()
        name = 'Автостопом по галактике'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert name in collector.get_books_with_specific_genre('Фантастика')

    # 4 получение жанра по названию книги
    def test_get_book_genre_get_book_genre_detective(self):
        collector = BooksCollector()
        name = 'Дурная кровь'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # 5 получения словаря и сравнение книг из словаря
    def test_get_books_genre_comparing_books_from_the_dictionary(self):
        collector = BooksCollector()
        dict_books = {'Властелин колец': 'Фантастика', 'Кристина': ''}
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Кристина')
        assert collector.get_books_genre() == dict_books

    # 6 получаем книгу для детей с жанром 'Мультфильм'
    def test_get_books_for_children_get_one_book_for_children_with_genre_cartoons(self):
        collector = BooksCollector()
        name = 'Муми-тролли'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Мультфильмы')
        assert name in collector.get_books_for_children()

    # 7 добавление одной книги в избранное
    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        name = 'Инквизитор Эйзенхорн'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    # 8 удаление одной книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        name = 'Инквизитор Эйзенхорн'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    # 9 получить спсок из 2-х избранных книг
    def test_get_list_of_favorites_books_get_list_of_two_favorite_books(self):
        collector = BooksCollector()
        name = ['Инквизитор Эйзенхорн', 'Космические волки']
        collector.add_new_book(name[0])
        collector.add_book_in_favorites(name[0])
        collector.add_new_book(name[1])
        collector.add_book_in_favorites(name[1])
        assert len(collector.get_list_of_favorites_books()) == 2

    # 10 не добавляет книгу в кол-вом символов > 40
    def test_add_new_book_does_not_add_book_more_forty_characters(self):
        collector = BooksCollector()
        collector.add_new_book('Девушка, которая взрывала воздушные замки')  # в названии 41 символ
        assert len(collector.get_books_genre()) == 0

    # 11 не добавляется уже существующая книга
    def test_add_new_book_not_add_exist_book(self):
        collector = BooksCollector()
        collector.add_new_book('Просперо в огне')
        collector.add_new_book('Просперо в огне')
        assert len(collector.get_books_genre()) == 1
