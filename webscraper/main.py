import webbrowser, sys, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By

#if len(sys.argv) > 1:
#    address = ' '.join(sys.argv[1:])
#else:
#    print("Must provide an address in arguments")
#    exit()

#webbrowser.open("https://www.google.com/maps/place/" + address) # Only works with specific addresses including the city, state, and zipcode

#res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
#play_file = open("webscraper/Romeo_and_Juliet.txt", 'wb')
#for chunk in res.iter_content(100000):
#    play_file.write(chunk)

#play_file.close()

def get_newegg_price(product_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    res = requests.get(product_url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select("html.show-tab-store.is-new body div#app div#newProductPageContent.page-content div.page-section div.page-content-inner div.row.is-product.has-side-right.has-side-items.is-new div.row-body div.product-main.has-combo.display-flex div.product-wrap div.row-side div.product-buy-box div.product-price ul.price div.price-new-action div.price-new-right div.price-current strong")
    return elems[0].text.strip() 

price = get_newegg_price("https://www.newegg.com/obsidian-black-acer-nitro-v-anv15-51-98n0/p/N82E16834360352?Item=N82E16834360352")
print("The price is: $" + price)

browser = webdriver.Firefox()
browser.get("https://newegg.com/")
#elem = browser.find_element(By.CSS_SELECTOR, ".main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(2) > a:nth-child(1)")
#elem.click()

search_elem = browser.find_element(By.CSS_SELECTOR, ".header2021-search-box > input:nth-child(1)")
search_elem.send_keys("test")