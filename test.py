import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна: Пустынная планета')
        collector.add_new_book('Основание: Крах Империи')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_cannot_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Солярис')
        collector.add_new_book('Солярис')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name, expected', [
        ('А' * 41, False),
        ('', False),
        ('А' * 40, True),
        ('Гиперион', True)
    ])
    def test_add_new_book_name_length(self, book_name, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Нейромант')
        collector.set_book_genre('Нейромант', 'Фантастика')
        assert collector.get_book_genre('Нейромант') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Космоопера')
        assert collector.get_book_genre('Пикник на обочине') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_books == ['Дюна']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Хроники Нарнии')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Хроники Нарнии', 'Фантастика')
        collector.set_book_genre('Дракула', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert children_books == ['Хроники Нарнии']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('451° по Фаренгейту')
        collector.add_book_in_favorites('451° по Фаренгейту')
        assert '451° по Фаренгейту' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.add_book_in_favorites('Мечтают ли андроиды об электроовцах?')
        collector.add_book_in_favorites('Мечтают ли андроиды об электроовцах?')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Война миров')
        collector.add_book_in_favorites('Война миров')
        collector.delete_book_from_favorites('Война миров')
        assert 'Война миров' not in collector.get_list_of_favorites_books()

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None