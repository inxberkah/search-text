import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Read list of URLs from file
with open('urls.txt') as f:
    urls = f.readlines()
urls = [url.strip() for url in urls]

# Text to search for
search_text = "example"

def scrape_url(url):
    # Send HTTP GET request to URL and get response
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if search text is present in the HTML content
    if soup.find(text=search_text) is not None:
        print(f"{search_text} found in {url}")
    else:
        print(f"{search_text} not found in {url}")

if __name__ == '__main__':
    # Create a ThreadPoolExecutor with 4 worker threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit scraping tasks to executor for each URL
        futures = [executor.submit(scrape_url, url) for url in urls]

        # Wait for all tasks to complete
        for future in futures:
            future.result()
