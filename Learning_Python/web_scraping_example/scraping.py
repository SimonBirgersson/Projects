# scraping.py
import requests
from bs4 import BeautifulSoup


#  check if site works
def check_rss(url: str):
    """
    call the Requests library and fetch our website using requests.get(...). I’m printing the status code to the terminal using r.status_code to check that the website has been successfully called.

    Additionally, I’ve wrapped this into a try: except: to catch any errors we may have later on down the road.

    Once we run the program, we’ll see a successful status code of 200. This states that we’re able to ping the site and “get” information.
    """
    try:

        # request HTML library
        r = requests.get(url)

        # if successful, http status code should be "200", 300 is redirect, 400 is error
        if r.status_code == 200:
            print(
                f"Connection established: status code is {r.status_code}\n\n", end="\r"
            )
            return True
        else:
            print(
                f"Connection unsucessful... status code is {r.status_code}\n\n",
                end="\r",
            )
            return False

    # if unsuccessful, print exception
    except Exception as exception:
        print("The scraping job failed. See exception: ")
        print(exception)


def pull_rss_xml(url: str):
    """
    Our program has returned a status code of 200, we’re all set to begin pulling XML content from the site.

    The above will assign our XML content from url to the soup variable. We’re using r.content to pass the returned XML to BeautifulSoup, which we’ll parse in the next example.

    A key thing to note is that we’re leveraging features='xml' , this would differ in other projects (i.e., if you’re scraping HTML you’ll declare it as HTML).

    Our output of the above will be a large mess of content that makes very little sense. This is to illustrate that we’re successfully pulling information from the website.
    """
    # create empty list
    try:
        # get HTML library
        r = requests.get(url)

        # parse XML data
        soup = BeautifulSoup(r.content, features="xml")

        return soup

    # if unsuccessful, print exception
    except Exception as exception:
        print("The scraping job failed. See exception: ")
        print(exception)


def save_function(
    text: str,
    path: str = "/Users/simon/Documents/Projects/Learning_Python/web_scraping_example/",
):
    """Save list as txt file"""
    # open or create txt file
    with open(
        path + "output.txt",
        "w",
        encoding="UTF-8",
    ) as f:

        f.write(text)
        f.close()


def main():
    """
    actual function, scrapes EU articles from NY times, and prints title, summary and url for each.
    """

    # NY times RSS
    PATH = "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml"

    print("Starting scraping...", end="\r")

    # check if the url connection can be established, i.e http code = 200
    if check_rss(url=PATH):
        # pull xml infor from url
        soup = pull_rss_xml(url=PATH)

        # articles are denoted as "items" in the xml for NYT
        items = soup.find_all("item")

        # fetch article, title,  description, and url.
        for item in items:
            title = item.title.text
            summary = item.description.text
            link = item.link.text

            # print each article
            print(
                f"Title: {title}\n\nSummary: {summary}\n\nLink: {link}\n\n-----------------------------\n\n"
            )


if __name__ == "__main__":
    main()
