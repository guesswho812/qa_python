import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Основание')
        assert len(collector.books_genre) == 2

    def test_add_new_book_cannot_add_duplicate(self, collector):
        collector.add_new_book('Солярис')
        collector.add_new_book('Солярис')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name, expected', [
        ('А' * 41, False),
        ('', False),
        ('А' * 40, True),
        ('Гиперион', True)
    ])
    def test_add_new_book_name_length(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.books_genre) == expected

    def test_set_book_genre_valid(self, collector):
        collector.books_genre = {'Нейромант': ''}
        collector.set_book_genre('Нейромант', 'Фантастика')
        assert collector.books_genre['Нейромант'] == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.books_genre = {'Пикник на обочине': ''}
        collector.set_book_genre('Пикник на обочине', 'Космоопера')
        assert collector.books_genre['Пикник на обочине'] == ''

    def test_set_book_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_specific_genre(self, collector):
        collector.books_genre = {'Дюна': 'Фантастика', 'Оно': 'Ужасы'}
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_books == ['Дюна']

    def test_get_books_genre_returns_correct_dict(self, collector):
        collector.books_genre = {'Дюна': 'Фантастика'}
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        collector.books_genre = {'Хроники Нарнии': 'Фантастика', 'Дракула': 'Ужасы'}
        children_books = collector.get_books_for_children()
        assert children_books == ['Хроники Нарнии']

    def test_add_book_in_favorites(self, collector):
        collector.books_genre = {'451° по Фаренгейту': 'Фантастика'}
        collector.add_book_in_favorites('451° по Фаренгейту')
        assert '451° по Фаренгейту' in collector.favorites

    def test_add_book_in_favorites_duplicate(self, collector):
        collector.books_genre = {'Мечтают ли андроиды об электроовцах?': 'Фантастика'}
        collector.favorites = ['Мечтают ли андроиды об электроовцах?']
        collector.add_book_in_favorites('Мечтают ли андроиды об электроовцах?')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.favorites = ['Война миров']
        collector.delete_book_from_favorites('Война миров')
        assert 'Война миров' not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ['Дюна', 'Основание']
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Основание']

    def test_get_book_genre_nonexistent(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None