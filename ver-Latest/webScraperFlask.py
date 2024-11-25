from flask import Flask, request, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
itemsCollection = {
    # title: [price, url]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    url = request.form['url']  # Get URL from the form
    try:
        # Headless mode
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)

        # Load the Product page(url)
        driver.get(url)

        # Wait (1 seconds max)
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )

        # Extract title
        title_element = driver.find_element(By.ID, "productTitle")
        title = title_element.text.strip()

        # Extract price
        price = "N/A" #initialize the price
        try:
            price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
            price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
            price = f"{price_element.text.strip()}.{price_fraction.text.strip()}"
            
            #append into the itemCollection
            itemsCollection[title] = [float(price), url]
            
            #find the lowest price and the url for the user
            if itemsCollection:
                lowest_title, lowest_item = min(itemsCollection.items(), key = lambda x: x[1][0])
                lowest_price = lowest_item[0]
                lowest_url = lowest_item[1] 
                
            else:
                lowest_title,lowest_item,lowest_price = None, None, None
          
            #go to the result page, pass all the data to it
            return render_template(
                'result.html', 
                title=title,
                price=price,
                lowest_title = lowest_title,
                lowest_price = lowest_price,
                lowest_url = lowest_url
                )
        
        except:
            price = "Price not found"

        # Close the browser(while scrapping the url, not our html)
        driver.quit()

    except Exception as e:
        return render_template('error.html') #Error page for a more intuitive instruction

#going to the table 
@app.route("/get_table", methods=["GET"])
def go_to_data():
    global itemsCollection
    
    #return the updated dictionary
    return jsonify(itemsCollection)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
    
#Optimize the error exception page, i.e. tell the user what to do, or go back to the index.html --> FIXED!
#Create a hashmap, after scrape one, can have button option to "KEEP SCRAPE", if(more than 2 products), find the best deal(scrape the numbe of items), or lowest price
#Use Dictionary instead of hashmap, as we suppose the user are going to ONLY use this function when they need to find the best deal for the same item
#Need Scrape() have a return value, s.t. 
