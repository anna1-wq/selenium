from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://localhost:8081/litecard/public_html/admin/login.php")
usr_name_field = browser.find_element_by_name("username")
usr_name_field.send_keys('admin')
paswd_field = browser.find_element_by_name("password")
paswd_field.send_keys('admin')
button_login = browser.find_element_by_tag_name('button')
button_login.click()

active_window = browser.current_window_handle
browser.find_elements_by_css_selector('#app-')[2].click()
country_list = browser.find_elements_by_css_selector('tbody tr td:nth-child(5) a')
country_list[0].click()
links = browser.find_elements_by_css_selector('#content tbody tr td a i ')
list=[]
for i, links in enumerate(links):
    links = browser.find_elements_by_css_selector('#content tbody tr td a i ')
    links[i].click()
    list =browser.window_handles
    last_el =len(list)-1
    new_window_id= list[last_el]
    browser.switch_to.window(new_window_id)
    if browser.current_window_handle ==new_window_id:
        print("Correct.Old window switched to new Window")
        print(browser.current_window_handle)
        browser.switch_to.window(active_window)
    else:
        print("Error")
browser.quit()
    


