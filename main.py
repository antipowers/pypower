from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from paths import *

"""
Example usage:

with SwimCloudScraper() as scraper:
    swimmer_times = scraper.get_swimmer_times("Caeleb", "Dressel")
    print(swimmer_times)
"""

class SwimCloudScraper:
    def __init__(self):
        # Create the webdriver and navigate to the website
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.usaswimming.org/times/individual-times-search')

        # Click the consent button to accept cookies, data storage, etc
        self.driver.find_element(By.XPATH, consent_button).click()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Quit the webdriver when exiting the 'with' block
        self.driver.quit()

    # Returns a dictionary of a swimmer's best times in the 'event': 'time' format
    def get_swimmer_times(self, first_name, last_name):
        times = {}

        # Enter the swimmer's name and prepare for search
        self.driver.find_element(By.XPATH, first_name_input).send_keys(first_name)
        self.driver.find_element(By.XPATH, last_name_input).send_keys(last_name)

        # Make it only show fastest times and search by event
        self.driver.find_element(By.XPATH, show_all_times_arrow).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fastest_by_event_button).click()

        # Search for the swimmer's times
        self.driver.find_element(By.XPATH, search_button).click()
        time.sleep(1)

        # Parse the swimmer's times from the table
        rows = self.driver.find_elements(By.XPATH, times_table + '/tr')
        for row in rows:
            try:
                text = row.text
                event = text.split(' ')[0] + ' ' + text.split(' ')[1] + ' ' + text.split(' ')[2]
                swim_time = text.split(' ')[3]
                times[event] = swim_time
            except:
                # Break out of the loop if there are no more rows to parse
                break

        return times