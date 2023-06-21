import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from UTILITIES.BaseClassPage import Base
from PageObjects.AdditmesPage import AddItems
import pytest
from UTILITIES.XLUTILS import XLUtils
import openpyxl
class Test_001(Base):
    username="pratik"
    def test_additem(self,setup):
        self.driver=setup
        self.driver.get("https://demoblaze.com/index.html")
        self.driver.maximize_window()
        self.obj=AddItems(self.driver)
        self.driver.implicitly_wait(360)
        self.obj.clickphone()
        self.obj.clickSamsung()
        self.explicitwait(self.obj.clickAddTocart())
        self.explicitwaitAlert()
        self.explicitwait(self.obj.clickhome())
        self.obj.clickmonitor()
        self.obj.clickAsus()
        self.explicitwait(self.obj.clickAddTocart())
        self.explicitwaitAlert()
        self.explicitwait(self.obj.clickhome())
        self.obj.clickLaptop()
        self.obj.clickDell()
        self.explicitwait(self.obj.clickAddTocart())
        self.explicitwaitAlert()
        self.obj.clickCarturl()
        time.sleep(5)
        self.row=self.obj.fetchRows()
        self.col=self.obj.fetchCols()
        list = []
        new_list = []
        for i in range(1,self.row + 1):
            for j in range(3, self.col):
                ele = self.driver.find_element(By.XPATH,
                    "/html/body/div[6]/div/div[1]/div/table/tbody/tr[" + str(i) + "]/td[" +
                                               str(j) + "]").get_attribute("innerHTML")
                list.append(ele)
        for value in list:
            if type(value) == str:
                new_list.append(int(value))
        temp = new_list.sort()
        print("cost price of each item =", new_list)
        print(" summed up value of all items = ", sum(new_list))
        self.explicitwait(self.obj.clickPlaceOrder())
        time.sleep(5)
        # self.explicitwaitSet(self.obj.setName()).send_keys("India")
        # self.driver.find_element(By.XPATH,self.obj.name).send_keys('rahul')
        self.obj.setName()

