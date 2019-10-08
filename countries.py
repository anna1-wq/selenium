from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://localhost:8081/litecard/public_html/admin/?app=countries&doc=countries")
usr_name_field = browser.find_element_by_name("username")
usr_name_field.send_keys('admin')
paswd_field = browser.find_element_by_name("password")
paswd_field.send_keys('admin')
button_login = browser.find_element_by_tag_name('button')
button_login.click()
unsorted_list_countr=[]
geo_zone_list=[]
urls_list=[]
rows = browser.find_elements_by_class_name("row")
for i in rows:
    countr = i.find_element_by_css_selector('td a').get_attribute('text')
    unsorted_list_countr.append(countr)
    zones = int(i.find_element_by_css_selector('td:nth-child(6)').get_attribute('innerText'))
    geo_zone_list.append(zones)
    urls = i.find_element_by_css_selector('td a').get_attribute('href')
    urls_list.append(urls)
if sorted(unsorted_list_countr)==unsorted_list_countr:
    print("countries in order")
else:
    print("error.countries not in order")

two_lists=zip(geo_zone_list,urls_list)
two_lists=tuple(two_lists)
for zones,url in two_lists:
    if zones>0:
        browser.get(url)
        row_list=browser.find_elements_by_xpath("//*[@id='table-zones']/tbody/tr/td[3]")
        new_list=[]
        for i in row_list:
            name=i.get_attribute('innerText')
            new_list.append(name)
            new_list=list(filter(None,new_list))
        if sorted(new_list)==new_list:
            print("countries inside in order")
        else:
            print("error.countries inside  is not in order")
            break
    else:
        continue


browser.get("http://localhost:8081/litecard/public_html/admin/?app=geo_zones&doc=geo_zones")
link_list=[]
rows = browser.find_elements_by_css_selector('.row td:nth-child(3) a')
for i in rows:
    link= i.get_attribute('href')
    link_list.append(link)
for i,link in enumerate(link_list):
    browser.get(link)
    elem_counr=browser.find_elements_by_css_selector('#table-zones td:nth-of-type(3) [selected="selected"]')
    list_of_elem = []
    for i in elem_counr:
        name_elem=i.get_attribute('innerText')
        list_of_elem.append(name_elem)
    print(list_of_elem)
    if sorted(list_of_elem)==list_of_elem:
        print("correct")
    else:
        print("error")
browser.quit()




