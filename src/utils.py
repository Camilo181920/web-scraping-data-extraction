import logging

from src.config import LOG_FILE, LOGS_DIR


def setup_logger() -> logging.Logger:
    """
    Configure application logger.
    """

    LOGS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger("web_scraper")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
