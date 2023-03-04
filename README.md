# SwimSync Scraper

A Python script that uses the Selenium web driver to scrape USA Swimming's individual times search tool for a swimmer's best times.

## Requirements

* Python 3.x
* Selenium for Python (`pip install selenium`)

## Installation

* To install the required packages, run the following command:

* `pip install -r requirements.txt`

* This will install all the packages listed in the requirements.txt file.

* Note: It is recommended to create a new virtual environment for this project to avoid conflicts with other packages installed on your system. You can create a new virtual environment using venv or conda.


## Usage

1. Clone the repository.
2. Install the requirements.
3. Import the `SwimCloudScraper` class.
4. Instantiate the class using the `with` statement.
5. Call the `get_swimmer_times()` method, passing in the first and last name of the swimmer as strings.
6. The method will return a dictionary containing the swimmer's best times, with event names as keys and times as values.

```python
from SwimCloudScraper import SwimCloudScraper

with SwimCloudScraper() as scraper:
    swimmer_times = scraper.get_swimmer_times("Caeleb", "Dressel")
    print(swimmer_times)
