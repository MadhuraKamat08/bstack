from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def initialize_client():
    driver = webdriver.Chrome()

    return driver
  
  
def element_finder(driver, xpath, wait_time = 10):
    waiter = WebDriverWait(driver, wait_time)
    element = waiter.until(EC.element_to_be_clickable((By.XPATH,xpath)))
    return element
  
  
def search_flipkart(driver,product_name):
  driver.get('https://www.flipkart.com/')
  search_box = element_finder(driver,'//input[@name="q"]')
  search_box.send_keys(product_name + Keys.ENTER)

  click_brand = element_finder(driver,'//div[text()="SAMSUNG"]')
  click_brand.click()
  time.sleep(2)

  assured= element_finder(driver,'//label[@class="_2iDkf8 shbqsL"]')
  assured.click()

  sort = element_finder(driver,'//div[text()="Price -- High to Low"]')
  sort.click()
  time.sleep(5)


  product_data= []

  product_card= driver.find_elements(By.XPATH,'//div[@class="_13oc-S"]')
  total_products = len(product_card)

  total_names = driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
  total_links = driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
  total_prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
  # logging.warning(total_products)

  for i in range(total_products):
      name_element = total_names[i]
      price_element = total_prices[i]
      link = total_links[i]
      href_link=link.get_attribute('href')
      name = name_element.text
      price = price_element.text
      product_data.append({"Name": name, "Price": price, "Link": href_link})

  print(product_data)

if __name__ == "__main__":
  driver = initialize_client()
  search_flipkart(driver,"Samsung Galaxy S10")
  driver.quit()
