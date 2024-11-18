from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

#initial the app/webpage
app = Flask(__name__)

@app.route('/')
#Homepage, an HTML code
def home():
    return '''
        <h1>Amazon Product Scraper</h1>
        <form action="/search" method="GET">
            <label for="query">Enter Search Term:</label>
            <input type="text" id="query" name="query" required>
            <button type="submit">Search</button>
        </form>
    '''

@app.route('/search')  #route Decorator, define urls ends withh /search
def search():
    query = request.args.get('query')
    if not query:
        return "Please enter a valid search term.", 400

    # Test: Format the Amazon search URL
    url = f"https://www.amazon.ca/s?k={query}"

    # Send an HTTP request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to retrieve the page. Status Code: {response.status_code}", 500

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('div', class_='s-result-item')

    results = []  #collecting all the HTML elements we want in the result array

    #Utilizing the size of the word to determine which one is the title or price(typical in Amazon items) and only for websites like this
    for e in elements: 
        try:
            title = e.find('span', class_='a-size-medium').text.strip() 
        except AttributeError:
            title = "N/A" 

        try:
            price = e.find('span', class_='a-offscreen').text.strip()
        except AttributeError:
            price = "N/A"

        try:
            link = e.find('a', class_='a-link-normal s-no-outline')['href']
            product_link = f"https://www.amazon.ca{link}"
        except (AttributeError, TypeError):
            product_link = "N/A"

        results.append({
            "title": title,
            "price": price,
            "link": product_link
        })

    # Generate HTML for results
    result_html = '<h1>Search Results</h1><ul>'
    for r in results:
        result_html += f'''
            <li>
                <strong>Title:</strong> {r['title']}<br>
                <strong>Price:</strong> {r['price']}<br>
                <strong>Link:</strong> <a href="{r['link']}" target="_blank">View Product</a>
            </li><br>
        '''
    result_html += '</ul><a href="/">Search Again</a>'
    return result_html

if __name__ == '__main__':
    app.run(debug=True)
