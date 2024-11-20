from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for scraping
@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']  # Get URL from the form
    try:
        # Set up Selenium WebDriver
        driver = webdriver.Chrome()  # Make sure ChromeDriver is in PATH

        # Load the Amazon product page
        driver.get(url)

        # Wait for the product title to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )

        # Get the fully-rendered HTML content
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Extract product title
        title_element = soup.find('span', id='productTitle')
        title = title_element.text.strip() if title_element else "N/A"

        # Extract price
        price_element = soup.find('span', class_='a-offscreen')
        price = price_element.text.strip() if price_element else "N/A"

        # Close the browser
        driver.quit()

        # Render the result back to the user
        return render_template('result.html', title=title, price=price)

    except Exception as e:
        return f"An error occurred: {e}"

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
