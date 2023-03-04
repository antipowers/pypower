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

## License
Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

This is a human-readable summary of (and not a substitute for) the license. 

You are free to:

Share — copy and redistribute the material in any medium or format 
The licensor cannot revoke these freedoms as long as you follow the license terms. 

Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use. 

NonCommercial — You may not use the material for commercial purposes. 

NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified material. 

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits. 

Notices:

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation. 

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.
