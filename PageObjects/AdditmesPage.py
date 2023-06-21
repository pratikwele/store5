import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddItems:
    home  = "/html/body/nav/div/div/ul/li[1]/a"
    phone  = "Phones"
    samsung  = "Samsung galaxy s6"
    AddTocart  = "Add to cart"
    monitor = "Monitors"
    asus = "ASUS Full HD"
    laptop = "Laptops"
    dell = "Dell i7 8gb"
    carturl = "cartur"
    rows = "/html/body/div[6]/div/div[1]/div/table/tbody/tr"
    cols =  "/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td"
    place_order = "/html/body/div[6]/div/div[2]/button"
    name =  '//*[@id="name"]'
    country = "country"
    city = "city"
    credit_card = "card"
    month = "month"
    year = "year"
    purchse = "/html/body/div[3]/div/div/div[3]/button[2]"
    your_purchase = "/html/body/div[10]/p"
    success = "/html/body/div[10]/h2"
    ok = "/html/body/div[10]/div[7]/div/button"
    place_order="/html/body/div[6]/div/div[2]/button"
    def __init__(self,driver):
        self.driver=driver


    def clickhome (self):
        return By.XPATH,self.home


    def clickphone(self):
        self.driver.find_element(By.LINK_TEXT,self.phone).click()

    def clickSamsung(self):
        self.driver.find_element(By.LINK_TEXT,self.samsung).click()

    def clickAddTocart(self):
         return  By.LINK_TEXT,self.AddTocart

    def clickmonitor(self):
        self.driver.find_element(By.LINK_TEXT, self.monitor).click()

    def clickAsus(self):
        self.driver.find_element(By.LINK_TEXT,self.asus).click()

    def clickLaptop(self):
        self.driver.find_element(By.LINK_TEXT,self.laptop).click()

    def clickDell(self):
        self.driver.find_element(By.LINK_TEXT,self.dell).click()

    def clickCarturl(self):
        self.driver.find_element(By.ID,self.carturl).click()

    def fetchRows (self):
        return len (self.driver.find_elements(By.XPATH, self.rows))
        # self.row=len (self.driver.find_elements(By.XPATH, self.rows))
        # print(self.row)
    def fetchCols (self):
        return len (self.driver.find_elements(By.XPATH, self.cols))
        # self.col=len (self.driver.find_elements(By.XPATH, self.cols))
        # print(self.col)
    def  clickPlaceOrder(self):
        self.driver.find_element(By.XPATH, self.place_order).click()

    def setName(self):
        time.sleep(4)
        # return self.driver.find_elements(By.XPATH,self.name)
        self.driver.find_elements(By.XPATH,self.name).send_keys("pratik")

    def setCountry(self):
        self.driver.find_element(By.ID,self.country).send_keys("India")

    def  setCity(self):
        self.driver.find_element(By.ID,self.city).send_keys("delhi")

    def setCreditCard(self):
        self.driver.find_element(By.ID, self.credit_card).send_keys("VISA")

    def setMonth(self):
        self.driver.find_element(By.ID, self.month).send_keys("june")

    def setYear(self):
        self.driver.find_element(By.ID, self.year).send_keys("2023")
    def clickPurchse(self):
        self.driver.find_element(By.XPATH,self.purchse).click()

    def fetchYourPurchase(self):
        self.driver.find_element(By.XPATH,self.your_purchase).get_attribute("innerHTML")

    def msgSuccess(self):
        self.driver.find_element(By.XPATH,self.success).get_attribute("innerHTML")

    def clickOk(self):
        self.driver.find_element(By.XPATH,self.ok).click()

