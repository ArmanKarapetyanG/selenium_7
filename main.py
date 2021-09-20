from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\chromedriver.exe')

driver.get('https://book24.ru/')

input_field = driver.find_element_by_name("q")
input_field.send_keys("Гарри Поттер")
input_field.send_keys(Keys.ENTER)
time.sleep(20)
# 1 book #
book_xpath = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div/div[1]/article/div[2]/a')
print(book_xpath.get_attribute("title"))
# all books #

all_books = driver.find_elements_by_css_selector("article.product-card a.product-card__name.smartLink")

for i in all_books:
    print(i.get_attribute("title"))






#driver.close()