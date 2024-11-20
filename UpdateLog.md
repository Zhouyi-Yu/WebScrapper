# Web Scraper Update Log

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
