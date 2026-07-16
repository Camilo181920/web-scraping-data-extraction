from src.parser import BookParser


def test_parse_single_page_books():

    html = """
    <html>
        <body>

            <article class="product_pod">

                <h3>
                    <a
                        href="catalogue/clean-code_1/index.html"
                        title="Clean Code"
                    >
                    Clean Code
                    </a>
                </h3>

                <p class="price_color">
                    £35.00
                </p>

                <p class="star-rating Three"></p>

                <p class="availability">
                    In stock
                </p>

            </article>

        </body>
    </html>
    """

    books = BookParser().parse_books(html)

    assert len(books) == 1

    book = books[0]

    assert book.title == "Clean Code"

    assert book.price == 35.00

    assert book.rating == 3

    assert book.availability is True

    assert book.product_url == "catalogue/clean-code_1/index.html"
