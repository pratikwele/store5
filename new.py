import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://seleniumbase.io/demo_page")
print(driver.get_window_size())
driver.set_window_size(500,300)
# elehover = driver.find_element(By.ID,"myDropdown")
# elelink3 = driver.find_element(By.ID,"dropOption3")
# action = ActionChains(driver)
#action.move_to_element(elehover).move_to_element(elelink3).click().perform()
# mouse double click
#eledbl = driver.find_element(By.ID,'myButton')
#action.double_click(eledbl).perform()
#single click
#action.click(eledbl).perform()
# right click
# link2 = driver.find_element(By.ID,"myLink2")
# action.context_click(link2).perform()


#driver.close()