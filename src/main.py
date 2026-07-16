from src.config import BASE_URL
from src.exporter import BookExporter
from src.parser import BookParser
from src.scraper import WebScraper
from src.utils import setup_logger

logger = setup_logger()


def run() -> None:
    """
    Execute complete scraping pipeline.
    """

    logger.info("Starting web scraping process")

    scraper = WebScraper()

    parser = BookParser()

    exporter = BookExporter()

    html = scraper.fetch_page(BASE_URL)

    books = parser.parse_books(html)

    exporter.export_json(books)

    exporter.export_csv(books)

    logger.info(
        "Process completed successfully. Books exported: %s",
        len(books),
    )


def main() -> None:
    """
    Application entry point.
    """

    try:

        run()

    except Exception:

        logger.exception("Application failed")

        raise


if __name__ == "__main__":
    main()
