from pathlib import Path

# ==========================
# Base paths
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "output"

LOGS_DIR = BASE_DIR / "logs"

# ==========================
# Scraper configuration
# ==========================

BASE_URL = "https://books.toscrape.com/"

REQUEST_TIMEOUT = 10

# ==========================
# Output files
# ==========================

JSON_OUTPUT_FILE = OUTPUT_DIR / "books.json"

CSV_OUTPUT_FILE = OUTPUT_DIR / "books.csv"

LOG_FILE = LOGS_DIR / "app.log"
