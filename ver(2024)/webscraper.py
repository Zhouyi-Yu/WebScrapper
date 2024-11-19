from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver (Ensure you have ChromeDriver installed)
driver = webdriver.Chrome()  # Use the Chrome as the Web-Driver

url = "https://www.amazon.ca/Sony-WH-1000XM4-Canceling-Headphones-WH1000XM4/dp/B0863TXGM3" #Test with this url for the stablized analysis

# Load the URL in the browser
driver.get(url)

# Get the fully-rendered HTML
html = driver.page_source

# Close the browser after use it
driver.quit()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract and display relevant information
try:
    # Extract title
    title_element = soup.find('span', id='productTitle')
    title = title_element.text.strip() if title_element else "N/A"

    # Extract price
    price_element = soup.find('span', class_='a-offscreen')
    price = price_element.text.strip() if price_element else "N/A"

    # Extract product description (optional)
    description_element = soup.find('div', id='productDescription')
    description = description_element.text.strip() if description_element else "N/A"

    # Print details to the terminal
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Description: {description}")

except Exception as e:
    print(f"An error occurred: {e}") #The older version is failed due to the request module, reason unknown.
