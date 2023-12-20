# Automated Test Case for Snapdeal Website

## Overview
This repository contains an automated test case implemented using Selenium for the Snapdeal website. The test script automates the process of searching for a product, applying filters, adding the item to the cart, and checking for successful addition.

# Test Case Description
The test case performs the following steps:

1. Opens the Snapdeal website using Chrome browser.
2. Searches for a "bag" using the search bar.
3. Clicks on the search button to view search results.
4. Filters the search results by price range between 600 and 1000.
5. Verifies if the URL matches the expected URL after applying the filters.
6. Retrieves the price of the first item and verifies if it falls within the expected price range (500 to 1000).
7. Adds the item to the cart and checks if the item was added successfully.
8. Opens the cart and validates the item.

# Tools Used
- Selenium WebDriver: Used for browser automation.
- Python: Language used to write the automation script and test cases.
- ChromeDriver: WebDriver for Chrome browser.
- pycharm (IDE)

# Setup Instructions
To run the script locally, follow these steps:

1. Clone this repository to your local machine.
2. Install Python if not already installed.
3. Install the Selenium package using pip: `pip install selenium`.
4. Download the ChromeDriver compatible with your Chrome browser version and place it in the project directory.

# Running the Test
1. Open the terminal and navigate to the project directory.
2. Execute the command: `python test_script.py`.
3. The automated test will run, and the output will be displayed in the terminal.

# Challenges Faced
- Installation and Configuration: Setting up the Selenium WebDriver and ensuring compatibility with the Chrome browser version was a challenge.
- Dynamic Elements: Identifying and handling dynamically changing elements on the website was challenging, requiring the use of explicit waits and proper element locators.

# Future Improvements
- Enhance error handling and reporting for a more comprehensive test suite.
- Implement data-driven testing for different search queries and price ranges.
- Modularize the code for better maintainability.
# Files in Repository
- functionality.py - main file of testing(this is main file in which the testing code is written)
- testing.py - tried to use pytest (can ignore this file)
# Testing Screenshots
<img width="960" alt="test1" src="https://github.com/munagalasandeep99/testing/assets/129391713/32d69b0e-90b2-4cc7-9669-65cc899f88fe">
<img width="960" alt="test2" src="https://github.com/munagalasandeep99/testing/assets/129391713/15348fd2-1149-45fe-ac86-7453bcd02bea">
