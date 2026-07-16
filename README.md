# Web Scraping Data Extraction Pipeline

Professional Python web scraping automation tool designed to extract, validate, transform, and export structured data from websites.

## Overview

This project implements an automated data extraction pipeline that collects book information from a public website, processes the extracted HTML content, validates the resulting data, and exports clean datasets in JSON and CSV formats.

The solution demonstrates a maintainable approach for building scraping workflows with separation of responsibilities, automated testing, logging, and reproducible execution.

## Features

* Automated web page retrieval
* HTML parsing with BeautifulSoup
* Data validation using Pydantic models
* Structured JSON and CSV exports
* Logging system for process monitoring
* Configuration management
* Automated tests with Pytest
* Code formatting and quality checks
* Docker-ready execution

## Project Architecture

```text
web-scraping-data-extraction/

├── src/
│   ├── scraper.py       # Website data retrieval
│   ├── parser.py        # HTML parsing and transformation
│   ├── exporter.py      # JSON and CSV generation
│   ├── models.py        # Data validation models
│   ├── config.py        # Application configuration
│   ├── utils.py         # Logging utilities
│   └── main.py          # Application entry point
│
├── tests/
│   ├── test_parser.py
│   └── test_exporter.py
│
├── data/
│   └── output/          # Generated datasets
│
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── requirements.txt
```

## Technologies

* Python 3.12
* Requests
* BeautifulSoup4
* Pydantic
* Pytest
* Docker
* Black
* isort
* Flake8

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/web-scraping-data-extraction.git

cd web-scraping-data-extraction
```

Create and activate a virtual environment:

```bash
python -m venv .venv

source .venv/bin/activate
```

Install dependencies:

```bash
make install
```

## Usage

Run the scraper:

```bash
make run
```

The pipeline will:

1. Fetch the target webpage
2. Extract book information
3. Validate the data structure
4. Generate output files

Generated files:

```text
data/output/books.json
data/output/books.csv
```

## Testing

Run automated tests:

```bash
make test
```

Expected result:

```text
3 passed
```

## Code Quality

Format the project:

```bash
make format
```

Run lint checks:

```bash
make lint
```

## Example Output

Generated JSON:

```json
{
    "title": "A Light in the Attic",
    "price": 51.77,
    "availability": true,
    "rating": 3
}
```

## Purpose

This project showcases practical experience building Python automation solutions for:

* Web data extraction
* Data processing pipelines
* Dataset generation
* Automation workflows
* Structured information collection
