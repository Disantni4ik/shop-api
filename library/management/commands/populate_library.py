from datetime import date
from decimal import Decimal
from django.core.management.base import BaseCommand

from library.models import Author, Book, Borrowing, Reader


class Command(BaseCommand):
    help = "Заповнює базу даних тестовими даними"

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Book.objects.all().delete()
        Borrowing.objects.all().delete()

        reader1, _ = Reader.objects.get_or_create(username="dmytro")
        reader1.set_password("12345678")
        reader1.save()

        reader2, _ = Reader.objects.get_or_create(username="olena")
        reader2.set_password("12345678")
        reader2.save()

        a1 = Author.objects.create(name="Тарас Шевченко", bio="Український поет", birth_date=date(1814, 3, 9))
        a2 = Author.objects.create(name="Іван Франко", bio="Український письменник", birth_date=date(1856, 8, 27))
        a3 = Author.objects.create(name="Леся Українка", bio="Українська поетеса", birth_date=date(1871, 2, 25))
        a4 = Author.objects.create(name="Джордж Орвелл", bio="Англійський письменник", birth_date=date(1903, 6, 25))
        a5 = Author.objects.create(name="Артур Конан Дойл", bio="Шотландський письменник", birth_date=date(1859, 5, 22))

        b1 = Book.objects.create(title="Кобзар", author=a1, description="Поезія", isbn="9780000000001",
                                 published_date=date(1840, 5, 1), pages=640, available_copies=3)
        b2 = Book.objects.create(title="Гайдамаки", author=a1, description="Поема", isbn="9780000000002",
                                 published_date=date(1841, 1, 1), pages=120, available_copies=0)

        b3 = Book.objects.create(title="Захар Беркут", author=a2, description="Повість", isbn="9780000000003",
                                 published_date=date(1883, 1, 1), pages=250, available_copies=4)
        b4 = Book.objects.create(title="Украдене щастя", author=a2, description="Драма", isbn="9780000000004",
                                 published_date=date(1893, 1, 1), pages=160, available_copies=2)

        b5 = Book.objects.create(title="Лісова пісня", author=a3, description="Драма-феєрія", isbn="9780000000005",
                                 published_date=date(1911, 1, 1), pages=180, available_copies=5)
        b6 = Book.objects.create(title="Бояриня", author=a3, description="Драматична поема", isbn="9780000000006",
                                 published_date=date(1910, 1, 1), pages=90, available_copies=0)

        b7 = Book.objects.create(title="1984", author=a4, description="Антиутопія", isbn="9780000000007",
                                 published_date=date(1949, 6, 8), pages=320, available_copies=6)
        b8 = Book.objects.create(title="Колгосп тварин", author=a4, description="Сатира", isbn="9780000000008",
                                 published_date=date(1945, 8, 17), pages=140, available_copies=1)

        b9 = Book.objects.create(title="Етюд у багряних тонах", author=a5, description="Детектив", isbn="9780000000009",
                                 published_date=date(1887, 11, 1), pages=160, available_copies=2)
        b10 = Book.objects.create(title="Собака Баскервілів", author=a5, description="Детектив", isbn="9780000000010",
                                  published_date=date(1902, 4, 1), pages=220, available_copies=3)

        Borrowing.objects.create(book=b1, reader=reader1, return_date=date(2024, 1, 20), is_returned=True)
        Borrowing.objects.create(book=b3, reader=reader1, return_date=date(2024, 2, 15), is_returned=True)
        Borrowing.objects.create(book=b5, reader=reader1, return_date=date(2024, 5, 10), is_returned=False)
        Borrowing.objects.create(book=b7, reader=reader2, return_date=date(2024, 4, 1), is_returned=False)
        Borrowing.objects.create(book=b9, reader=reader2, return_date=date(2024, 3, 20), is_returned=True)

        self.stdout.write(self.style.SUCCESS(
            f"✅ Готово! Створено: {Author.objects.count()} авторів, "
            f"{Book.objects.count()} книг, "
            f"{Borrowing.objects.count()} позик."
        ))