# AxarAzParser

AxarAzParser is a Python web scraper designed to extract news articles from the Azerbaijani news website "Axar.az". The scraper utilizes the BeautifulSoup library for HTML parsing and Requests for making HTTP requests. The scraped data is then stored in a Pandas DataFrame and saved to a CSV file.

## Usage

1. Install the required libraries:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```

2. Import the AxarAzParser class into your script or project.

```python
from axar_az_parser import AxarAzParser
```

3. Create an instance of AxarAzParser by providing the base directory where you want to save the CSV file.

```python
base_directory = "/path/to/your/directory/"
parser = AxarAzParser(base_directory)
```

4. Run the `scrape` method to start extracting news articles from Axar.az.

```python
parser.scrape()
```

5. After scraping, use the `save_to_csv` method to save the extracted data to a CSV file.

```python
parser.save_to_csv()
```

## Class Methods

### `__init__(self, base_dir)`

- Constructor method to initialize the AxarAzParser instance.
- Parameters:
  - `base_dir`: The base directory where the CSV file will be saved.

### `get_soup(self, url) -> BeautifulSoup`

- Fetches the HTML content of a given URL and returns a BeautifulSoup object for parsing.
- Parameters:
  - `url`: The URL of the webpage to fetch.

### `get_pages(self, url, n) -> List[str]`

- Generates a list of page URLs based on the provided URL and the number of pages (n).
- Parameters:
  - `url`: The base URL.
  - `n`: The number of pages.

### `get_news_urls(self, url) -> Tuple[List[str], bool]`

- Extracts news article URLs from a given category page.
- Parameters:
  - `url`: The URL of the category page.
- Returns:
  - A tuple containing a list of news URLs and a boolean flag indicating success.

### `get_news(self, url) -> Tuple[str, str]`

- Extracts the summary and article text from a news article page.
- Parameters:
  - `url`: The URL of the news article.
- Returns:
  - A tuple containing the summary and article text.

### `scrape(self) -> None`

- Initiates the scraping process by iterating through categories, pages, and news articles.

### `save_to_csv(self) -> None`

- Converts the scraped data into a Pandas DataFrame and saves it to a CSV file in the specified base directory.

## Example

```python
from axar_az_parser import AxarAzParser

base_directory = "/path/to/your/directory/"
parser = AxarAzParser(base_directory)
parser.scrape()
parser.save_to_csv()
```

This example demonstrates how to use the AxarAzParser to scrape news articles from Axar.az and save the data to a CSV file. Adjust the `base_directory` variable to the desired location on your system.
