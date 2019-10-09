from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from random import uniform

try:
    browser = webdriver.Chrome()
    browser.get("http://litecart.stqa.ru/ru/")
    a = str(uniform(1, 99))
    email = a+"blala@list.ru"
    password = "password"
    browser.find_element_by_css_selector('#box-account-login tr td a').click()
    browser.find_element_by_name('firstname').send_keys("firstname")
    browser.find_element_by_name('lastname').send_keys("lastname")
    browser.find_element_by_name('address1').send_keys("address")
    browser.find_element_by_name('postcode').send_keys("35004")
    browser.find_element_by_name('city').send_keys("city")
    Select(browser.find_element_by_name('country_code')).select_by_visible_text('United States')
    time.sleep(2)
    Select(browser.find_element_by_css_selector('#create-account > div > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')).select_by_value("AK")
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('phone').send_keys("9456783421")
    browser.find_element_by_name('newsletter').click()
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('confirmed_password').send_keys(password)
    browser.find_element_by_name('create_account').click()
    browser.find_element_by_css_selector('#box-account li:nth-child(4) a').click()
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_name("login").click()
    browser.find_element_by_css_selector('#box-account li:nth-child(4) a').click()
    browser.quit()

finally:
    time.sleep(2)
    browser.quit()