import requests
from bs4 import BeautifulSoup
import csv


def scrape_books():
    books_data = []

    # loop through all pages of the website
    for page in range(1, 51):

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # find all book containers on the page
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            # book title is stored in the "title" attribute
            title = book.find("h3").find("a")["title"]
            # remove currency symbols from price
            price = book.find("p", class_="price_color").text
            price = price.replace("Â", "").replace("£", "")
            # extract rating (One, Two, Three, Four, Five)
            rating = book.find("p", class_="star-rating")["class"][1]

            books_data.append((title, price, rating))


    # save scraped data into CSV file
    with open("data.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["title", "price", "rating"])
        writer.writerows(books_data)

    print("Scraping finished. Data saved to data.csv")


if __name__ == "__main__":
    scrape_books()