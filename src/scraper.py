import requests

from src.config import REQUEST_TIMEOUT
from src.utils import setup_logger

logger = setup_logger()


class WebScraper:
    """
    HTTP client responsible for retrieving web pages.
    """

    def __init__(self) -> None:

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 " "(compatible; " "ProfessionalWebScraper/1.0)"
                )
            }
        )

    def fetch_page(
        self,
        url: str,
    ) -> str:
        """
        Download HTML content from URL.

        Args:
            url: Target page URL.

        Returns:
            HTML content.
        """

        logger.info(
            "Fetching URL: %s",
            url,
        )

        try:

            response = self.session.get(
                url,
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            logger.info("Page retrieved successfully")

            return response.text

        except requests.RequestException as exc:

            logger.exception("Failed fetching URL")

            raise exc
