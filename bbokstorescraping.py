import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1️⃣ Set the URL
url = 'http://books.toscrape.com/catalogue/page-1.html'

# 2️⃣ Make the HTTP GET request
response = requests.get(url)
print("Status Code:", response.status_code)

# 3️⃣ Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# 4️⃣ Find all book containers
books = soup.find_all('article', class_='product_pod')
print(f"Found {len(books)} books on the page.")

# 5️⃣ Prepare an empty list for book data
data = []

# 6️⃣ Loop through each book and extract details
for book in books:
    # Title
    title = book.h3.a['title']

    # Price
    price = book.find('p', class_='price_color').text.strip()

    # Availability
    availability = book.find('p', class_='instock availability').text.strip()

    # Rating (it's in the class name like 'star-rating Three')
    rating_class = book.find('p', class_='star-rating')['class']
    # The second class is the rating value
    rating = rating_class[1]

    # Append to list
    data.append({
        'Title': title,
        'Price': price,
        'Availability': availability,
        'Rating': rating
    })

# 7️⃣ Convert to pandas DataFrame
df = pd.DataFrame(data)
print(df)

# 8️⃣ Save to CSV
df.to_csv('books_page1.csv', index=False)
print("\nCSV file 'books_page1.csv' saved successfully.")
