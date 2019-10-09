from selenium import webdriver
import time
from selenium.webdriver.support.color import Color
browser = webdriver.Chrome()
browser.get("http://localhost:8081/litecard/public_html/en/")

duck=browser.find_element_by_css_selector('#box-campaigns [class = "link"]')

duck_title=duck.get_attribute("title")

price=duck.find_element_by_css_selector('#box-campaigns .price-wrapper [class = "regular-price"]')

sale_price=duck.find_element_by_css_selector('#box-campaigns .price-wrapper [class = "campaign-price"]')

price_number=price.get_attribute("textContent")

price_color=[Color.from_string(price.value_of_css_property("color")).red,
             Color.from_string(price.value_of_css_property("color")).green,
             Color.from_string(price.value_of_css_property("color")).blue]

price_stricked=price.value_of_css_property("text-decoration-line")

price_size= price.value_of_css_property("font-size")

sale_price_number = sale_price.get_attribute("textContent")

sale_price_color = [Color.from_string(sale_price.value_of_css_property("color")).red,
                         Color.from_string(sale_price.value_of_css_property("color")).green,
                         Color.from_string(sale_price.value_of_css_property("color")).blue]

sale_price_size = sale_price.value_of_css_property("font-size")

sale_price_weight = int(sale_price.value_of_css_property("font-weight"))

duck.click()
time.sleep(2)

duck_after_click =browser.find_element_by_css_selector('#box-product')

duck_title_after_click=duck_after_click.find_element_by_css_selector('.title').get_attribute("textContent")

price_after_click = duck_after_click.find_element_by_css_selector('#box-product .price-wrapper [class = "regular-price"]')

price_number_after_click =price_after_click.get_attribute("textContent")

price_color_after_click = [Color.from_string(price_after_click.value_of_css_property("color")).red,
                         Color.from_string(price_after_click.value_of_css_property("color")).green,
                         Color.from_string(price_after_click.value_of_css_property("color")).blue]

price_stricked_after_click = price_after_click.value_of_css_property("text-decoration-line")

price_size_after_click= price_after_click.value_of_css_property("font-size")

sale_price_after_click=duck_after_click.find_element_by_css_selector('#box-product .price-wrapper [class = "campaign-price"]')

sale_price_number_after_click= sale_price_after_click.get_attribute("textContent")

sale_price_color_after_click= [Color.from_string(sale_price_after_click.value_of_css_property("color")).red,
                          Color.from_string(sale_price_after_click.value_of_css_property("color")).green,
                          Color.from_string(sale_price_after_click.value_of_css_property("color")).blue]

sale_price_size_after_click = sale_price_after_click.value_of_css_property("font-size")

sale_price_weight_after_click = int(sale_price_after_click.value_of_css_property("font-weight"))

if price_stricked== "line-through":
    print("Correct.line-through")
else:
    print("Error with style")

if price_number==price_number_after_click:
    print("Correct price")
else:
    print("Error with price")

if duck_title==duck_title_after_click:
    print("Correct titles")
else:
    print("Error with titles")

if price_color_after_click[0]==price_color_after_click[1]==price_color_after_click[2]:
    print("Correct . Color of price  after click is gray")
else:
    print("Error.Color of price after click is not gray")

if price_stricked_after_click== "line-through":
    print("Correct.line-through of price  after click")
else:
    print("Error with style")

if price_color[0]==price_color[1]==price_color[2]:
    print("Correct .Color of price is gray")
else:
    print("Error.Color of price is not gray")

if sale_price_number == sale_price_number_after_click:
    print("Correct .sale price is correct")
else:
    print("Error.sale price is not correct")

if sale_price_size > price_size :
    print("Correct . Size of sale price is correct")
else:
    print("Error.Size of sale price is uncorrect" )

if sale_price_size_after_click > price_size_after_click:
    print("Correct .Size of sale price after click  is correct")
else:
    print("Error.Size of sale price  after click is uncorrect")

if sale_price_weight > 0 :
    print("Correct .Font-weight is correct  of sale price")

else:
    print("Error.Font-weight is uncorrect  of sale price ")

if sale_price_weight_after_click > 0 :
    print("Correct .Font-weight is correct  of sale price after click ")

else:
    print("Error.Font-weight is uncorrect  of sale price  after click")

if  0 in sale_price_color_after_click[1:]:
    print("Correct. Color of sale price is red")
else:
    print("Error.Color of sale price is not red")

if  0 in sale_price_color[1:]:
    print("Correct. Color of sale price is red")
else:
    print("Error.Color of sale price is not red")


browser.quit()





