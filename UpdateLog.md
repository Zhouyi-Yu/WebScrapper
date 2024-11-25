# Web Scraper Update Log

## 2024-Nov-18th
### Issue:
`webScraperFlask.py` Not running at all, due to unknown reasons
### Fixes: 
#### **1. Returning the right information**
- **How:** Found the correct classname of prices and titles.
- **Why:** 
  - Only the right classname can lead the user to the correct information in an HTML file


## 2024-Nov-19th
### Issue:
`webScraperFlask.py` executes longer than 16 seconds in general, often within a pop-up window, which is misleading to users.

---

## 2024-Nov-20th
### Fixes:

#### **1. Pop-up Window Fixed**
- **How:** Enabled headless mode of Selenium WebDriver.
- **Why:** 
  - Headless mode simulates a browser without a UI, reducing resource usage and speeding up execution.

#### **2. Improved Performance Time**
- **Performance Improvement:** 
  - **Before:** Average 13 seconds.
  - **After:** Average 9 seconds.

- **How:** 
  1. Removed the `BeautifulSoup` library since Selenium already handles the required DOM interactions.
  2. Enabled headless mode of Selenium WebDriver.

- **Why:** 
  - Consistent use of one library reduces complexity and may improve performance.
  - Headless mode minimizes overhead by bypassing UI rendering.


 ---
 
## 2024-Nov-21st
### Fixes:

#### **1. Improved Webpage**
- **How:** In `index.html` and `result.html`Use HTML's functionalitis such as animation, spinner, button to create a more intuitive and user-friendly web-page
- **Why:** 
  - N/A

---
## 2024-Nov-24th
### Fixes:

#### **1. Error Page Fixed**
- **How:** Added a new `error.html` file.
- **Why:** 
  - To help users understand what went wrong and provide an option to return to the home page directly, instead of leaving them uncertain about what to do when they make a mistake.

#### **2. Added a Table of Scraped Items**
- **How:** 
  - Updated `webScraperFlask.py` by adding an empty dictionary to store scraped items.
  - Modified `result.html` to include a table using an HTML table library and jQuery for simplicity.
  - Implemented `getTable()` and `updateTable()` functions in JavaScript to handle table rendering and updates dynamically.
- **Why:** 
  - Allows users to view a history of the items they have scraped and compare products easily within the table.

#### **3. Added Cheapest Price Item Display**
- **How:** 
  - Implemented a `minimum` function in `webScraperFlask.py` to find the cheapest item from the dictionary.
  - Updated `result.html` to display the cheapest item dynamically based on the current dictionary data.
- **Why:** 
  - Enables users to identify the cheapest item directly without having to manually search through the table.

