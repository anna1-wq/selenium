from selenium import webdriver
import time

def test():
    browser = webdriver.Chrome()
    browser.get("http://localhost:8081/litecard/public_html/admin/login.php")
    usr_name_field = browser.find_element_by_name("username")
    usr_name_field.send_keys('admin')
    paswd_field = browser.find_element_by_name("password")
    paswd_field.send_keys('admin')
    button_login = browser.find_element_by_tag_name('button')
    button_login.click()
    browser.get("http://localhost:8081/litecard/public_html/admin/?app=catalog&doc=catalog&category_id=1")
    browser.find_elements_by_css_selector('.row td:nth-child(3) a')[1].click()
    browser.find_elements_by_css_selector('.row td:nth-child(3) a')[2].click()
    rows = browser.find_elements_by_css_selector('.row td:nth-child(3) a')
    for i in range(len(rows)):
        browser.find_elements_by_css_selector('.row td:nth-child(3) a')[2].click()
        rows = browser.find_elements_by_css_selector('.row td:nth-child(3) a')
        rows[i].click()
        browser.back()
        logs = browser.get_log('browser')
        for log in logs:
            assert log is None