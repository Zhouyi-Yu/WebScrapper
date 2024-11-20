import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.ca/s?k=iphone+14&crid=KMQVK68QEO50&sprefix=iphone+1%2Caps%2C131&ref=nb_sb_noss_2"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the result items
    elements = soup.find_all('div', class_='s-result-item')

    for e in elements:
        # Find the product title
        try:
            title = e.find('span', class_='a-size-medium')
            product_title = title.text.strip()
        except AttributeError:
            product_title = "N/A"

        # Find the product price
        try:
            price = e.find('span', class_='a-offscreen')
            product_price = price.text.strip()
        except AttributeError:
            product_price = "N/A"

        # Find the product link
        try:
            link = e.find('a', class_='a-link-normal s-no-outline')['href']
            product_link = f"https://www.amazon.ca{link}"
        except (AttributeError, TypeError):
            product_link = "N/A"

        print("Title:", product_title)
        print("Price:", product_price)
        print("Link:", product_link)
        print()

else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")
