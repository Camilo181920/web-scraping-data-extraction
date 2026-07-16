from bs4 import BeautifulSoup

from src.models import Book
from src.utils import setup_logger

logger = setup_logger()


class BookParser:
    """
    Parse HTML content into Book models.
    """

    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    def parse_books(
        self,
        html: str,
    ) -> list[Book]:
        """
        Extract books from HTML.
        """

        logger.info("Starting HTML parsing")

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        books = []

        articles = soup.select("article.product_pod")

        logger.info(
            "Books found: %s",
            len(articles),
        )

        for article in articles:

            try:

                book = self._parse_book(article)

                books.append(book)

            except Exception:

                logger.exception("Failed parsing book")

        logger.info(
            "Books parsed successfully: %s",
            len(books),
        )

        return books

    def _parse_book(
        self,
        article,
    ) -> Book:
        """
        Parse single book element.
        """

        title = article.h3.a["title"]

        price = self._parse_price(article)

        availability_text = article.select_one(".availability").text.strip()

        availability = "In stock" in availability_text

        rating = self._parse_rating(article)

        product_url = article.h3.a["href"]

        return Book(
            title=title,
            price=price,
            availability=availability,
            rating=rating,
            product_url=product_url,
        )

    def _parse_price(
        self,
        article,
    ) -> float:
        """
        Extract numeric price value.
        """

        price_text = article.select_one(".price_color").text

        cleaned_price = price_text.replace("£", "").replace("Â", "").strip()

        return float(cleaned_price)

    def _parse_rating(
        self,
        article,
    ) -> int:
        """
        Extract star rating.
        """

        rating_class = article.select_one("p.star-rating")["class"]

        rating_name = rating_class[1]

        return self.RATING_MAP.get(
            rating_name,
            0,
        )
