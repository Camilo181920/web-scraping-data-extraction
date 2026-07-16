import csv
import json
from pathlib import Path

from src.config import (
    CSV_OUTPUT_FILE,
    JSON_OUTPUT_FILE,
    OUTPUT_DIR,
)
from src.models import Book
from src.utils import setup_logger

logger = setup_logger()


class BookExporter:
    """
    Export books into different formats.
    """

    def __init__(self) -> None:

        OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def export_json(
        self,
        books: list[Book],
    ) -> Path:
        """
        Export books as JSON.
        """

        data = [book.model_dump() for book in books]

        with open(
            JSON_OUTPUT_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        logger.info(
            "JSON export completed: %s",
            JSON_OUTPUT_FILE,
        )

        return JSON_OUTPUT_FILE

    def export_csv(
        self,
        books: list[Book],
    ) -> Path:
        """
        Export books as CSV.
        """

        with open(
            CSV_OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "title",
                    "price",
                    "availability",
                    "rating",
                    "product_url",
                ],
            )

            writer.writeheader()

            for book in books:

                writer.writerow(book.model_dump())

        logger.info(
            "CSV export completed: %s",
            CSV_OUTPUT_FILE,
        )

        return CSV_OUTPUT_FILE
