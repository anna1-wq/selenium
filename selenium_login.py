from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://localhost:8081/litecard/public_html/admin/login.php")
try:
    usr_name_field = browser.find_element_by_name("username")
    usr_name_field.send_keys('admin')
    paswd_field = browser.find_element_by_name("password")
    paswd_field.send_keys('admin')
    button_login = browser.find_element_by_tag_name('button')
    button_login.click()
    time.sleep(3)
    browser.quit()
finally:
    time.sleep(3)
    browser.quit()