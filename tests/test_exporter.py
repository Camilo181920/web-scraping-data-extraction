from src.exporter import BookExporter
from src.models import Book


def test_export_books_json(tmp_path):

    book = Book(
        title="Clean Code",
        price=35.0,
        availability=True,
        rating=5,
        product_url="catalogue/test.html",
    )

    exporter = BookExporter()

    output = exporter.export_json([book])

    assert output.exists()


def test_export_books_csv():

    book = Book(
        title="Clean Code",
        price=35.0,
        availability=True,
        rating=5,
        product_url="catalogue/test.html",
    )

    exporter = BookExporter()

    output = exporter.export_csv([book])

    assert output.exists()
