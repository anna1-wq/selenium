from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://localhost:8081/litecard/public_html/en/")
try:
    products = browser.find_elements_by_css_selector('[class^=product]')
    for i in products:
        sticker= i.find_elements_by_css_selector('[class^=sticker]')
        if len(sticker)==1:
            continue
        else:
            print("Couldnt find sticker")
            break
    browser.quit()
finally:
    time.sleep(2)
    browser.quit()






