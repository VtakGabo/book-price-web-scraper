import pandas as pd
import matplotlib.pyplot as plt


def analyze_books():
    # load dataset created by the scraper
    data = pd.read_csv("data.csv")

    # convert price column to float for calculation
    data["price"] = data["price"].astype(float)

    print("Average price:")
    print(data["price"].mean())
    print("\nMost expensive book:")
    print(data.loc[data["price"].idxmax()])
    print("\nCheapest book:")
    print(data.loc[data["price"].idxmin()])
    print("\nAverage price by rating:")
    print(data.groupby("rating")["price"].mean())

    #number of books for each rating
    data["rating"].value_counts().plot(kind="bar")

    plt.title("Number of Books by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Count")

    plt.show()


    #distribution of book prices
    data["price"].plot(kind="hist", bins=20)

    plt.title("Price Distribution of Books")
    plt.xlabel("Price")
    plt.ylabel("Number of Books")

    plt.show()


    #average price per rating
    data.groupby("rating")["price"].mean().plot(kind="bar")
    
    plt.title("Average Book Price by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Average Price")

    plt.show()


if __name__ == "__main__":
    analyze_books()