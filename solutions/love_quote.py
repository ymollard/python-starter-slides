from bs4 import BeautifulSoup
from time import sleep
import requests

quote_str, author = "", ""
found_love_quote = False
analysed_quotes = 0

while not found_love_quote:
    get = requests.get("http://www.quotationspage.com/random.php")

    if not get.ok:
        print("Sorry, something went wrong while trying to retrieve the quotation web page :(")
    else:
        page = get.content
        soup = BeautifulSoup(get.content, "html.parser")
        quotes = soup.find_all("dt", class_="quote")
        authors = soup.find_all("dd", class_="author")

        assert len(quotes) == len(authors)

        for i, quote in enumerate(quotes):
            analysed_quotes += 1
            quote_str = list(quote.children)[0].string
            b_tag_author = list(authors[i].children)[1]
            author = list(b_tag_author.children)[0].string

            if "love" in quote_str.lower():
                found_love_quote = True
                break
    print("No LOVE quote found, trying a new page...")
    sleep(1)

if found_love_quote:
    print("After {} quote analyses, I found a LOVE quote. {} someday said:".format(analysed_quotes, author))
    print("\"{}\"".format(quote_str))

