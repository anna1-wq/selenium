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
    elems = browser.find_elements_by_id('app-')
    for i in range(len(elems)):
        elems = browser.find_elements_by_id('app-')
        elems[i].click()
        header = browser.find_element_by_tag_name('h1')
        sub_menu = browser.find_elements_by_css_selector("[id^=doc-]")
        if len(sub_menu) > 0:
            for i in range(len(sub_menu)):
                sub_menu = browser.find_elements_by_css_selector("[id^=doc-]")
                sub_menu[i].click()
                header = browser.find_element_by_tag_name('h1')



    browser.quit()
finally:
    time.sleep(3)
    browser.quit()