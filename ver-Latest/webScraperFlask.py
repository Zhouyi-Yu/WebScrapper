from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']  # Get URL from the form
    try:
        # Set up Selenium WebDriver with headless mode
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)

        # Load the Amazon product page
        driver.get(url)

        # Wait for the product title to load (5 seconds max)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )

        # Extract product title
        title_element = driver.find_element(By.ID, "productTitle")
        title = title_element.text.strip()

        # Extract price
        price = "N/A"
        try:
            price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
            price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
            price = f"{price_element.text.strip()}.{price_fraction.text.strip()}"
        except:
            price = "Price not found"

        # Close the browser
        driver.quit()

        # Render the result back to the user
        return render_template('result.html', title=title, price=price)

    except Exception as e:
        return f"An error occurred: {e}"

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

