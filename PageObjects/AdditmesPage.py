import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import allure
class AddItems:
    home  = (By.XPATH,"/html/body/nav/div/div/ul/li[1]/a")
    phone  = "Phones"
    samsung  =( By.LINK_TEXT,"Samsung galaxy s6")
    AddTocart  = (By.LINK_TEXT,"Add to cart")
    monitor = "Monitors"
    asus = "ASUS Full HD"
    laptop = "Laptops"
    dell = "Dell i7 8gb"
    carturl = "cartur"
    rows = (By.XPATH,"/html/body/div[6]/div/div[1]/div/table/tbody/tr")
    cols =  (By.XPATH,"/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td")
    place_order = (By.XPATH,"/html/body/div[6]/div/div[2]/button")
    name =  (By.XPATH,'//*[@id="name"]')
    country = (By.ID,"country")
    city = (By.ID,"city")
    credit_card = (By.ID,"card")
    month = (By.ID,"month")
    year = (By.ID,"year")
    purchse = (By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]")
    your_purchase = (By.XPATH,"/html/body/div[10]/p")
    success = (By.XPATH,"/html/body/div[10]/h2")
    ok = (By.XPATH,"/html/body/div[10]/div[7]/div/button")
    # place_order="/html/body/div[6]/div/div[2]/button"
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 20)

    def clickhome (self):
        self.wait.until(expected_conditions.presence_of_element_located(self.home))
        self.driver.find_element(*AddItems.home).click()

    def explicitwaitAlert(self):
        self.wait.until(expected_conditions.alert_is_present())
        self.driver.switch_to.alert.accept()

    def clickphone(self):
        self.driver.find_element(By.LINK_TEXT,self.phone).click()

    def clickSamsung(self):
       try:
        # self.wait.until(expected_conditions.presence_of_element_located(self.samsung))
         self.driver.find_element(*AddItems.samsung).click()
       except:
          self.driver.find_element(*AddItems.samsung).click()
    def clickAddTocart(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.AddTocart))
        self.driver.find_element(*AddItems.AddTocart).click()


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

    def verify_amount(self):
        time.sleep(5)
        self.row = len(self.driver.find_elements(*AddItems.rows))
        self.col = len(self.driver.find_elements(*AddItems.cols))
        print(self.row)
        print(self.col)
        list = []
        new_list = []
        for i in range(1, self.row + 1):
            for j in range(3, self.col):
                ele = self.driver.find_element(By.XPATH,
                                               "/html/body/div[6]/div/div[1]/div/table/tbody/tr[" + str(i) + "]/td[" +
                                               str(j) + "]").get_attribute("innerHTML")
                list.append(ele)
        for value in list:
            if type(value) == str:
                new_list.append(int(value))
        temp = new_list.sort()
        print(temp)
        print("cost price of each item =", new_list)
        print(" summed up value of all items = ", sum(new_list))
    '''def fetchRows (self):
        return len (self.driver.find_elements(By.XPATH, self.rows))
        # self.row=len (self.driver.find_elements(By.XPATH, self.rows))
        # print(self.row)
    def fetchCols (self):
        return len (self.driver.find_elements(By.XPATH, self.cols))
        # self.col=len (self.driver.find_elements(By.XPATH, self.cols))
        # print(self.col)'''
    def  clickPlaceOrder(self):

        self.wait.until(expected_conditions.presence_of_element_located(self.place_order))
        self.driver.find_element(*AddItems.place_order).click()

    def setName(self):
        time.sleep(4)
        # return self.driver.find_element(By.XPATH,self.name)
        self.driver.find_element(*AddItems.name).send_keys("pratik")

    def setCountry(self):
        # self.driver.find_element(By.ID,self.country).send_keys("India")
        self.driver.find_element(*AddItems.country).send_keys("india")
    def  setCity(self):
        # self.driver.find_element(By.ID,self.city).send_keys("delhi")
        self.driver.find_element(*AddItems.city).send_keys("nagpur")
    def setCreditCard(self):
        # self.driver.find_element(By.ID, self.credit_card).send_keys("VISA")

       self.driver.find_element(*AddItems.credit_card).send_keys("visa")
    def setMonth(self):
        # self.driver.find_element(By.ID, self.month).send_keys("june")

       self.driver.find_element(*AddItems.month).send_keys("june")
    def setYear(self):
        # self.driver.find_element(By.ID, self.year).send_keys("2023")

        self.driver.find_element(*AddItems.year).send_keys("2023")
    def clickPurchse(self):
        # self.driver.find_element(By.XPATH,self.purchse).click()

        self.driver.find_element(*AddItems.purchse).click()
    def fetchYourPurchase(self):
       # print( self.driver.find_element(*AddItems.your_purchase).get_attribute("innerHTML"))
        # self.purchess=self.driver.find_element(*AddItems.your_purchase).get_attribute("innerHTML")
        # print(self.purchess)
        return self.driver.find_element(*AddItems.your_purchase).get_attribute("innerHTML")
    def msgSuccess(self):
        # print(self.driver.find_element(*AddItems.success).get_attribute("innerHTML"))
        # self.mgsuccs=self.driver.find_element(*AddItems.success).get_attribute("innerHTML")
        # print(self.mgsuccs)
        return self.driver.find_element(*AddItems.success).get_attribute("innerHTML")
    def clickOk(self):
        # self.driver.find_element(By.XPATH,self.ok).click()

        self.driver.find_element(*AddItems.ok).click()
