import time



# from UTILITIES.BaseClassPage import Base
import allure
import pytest

from PageObjects.AdditmesPage import AddItems


from UTILITIES.Logger import Logging_Class

from allure_commons.types import AttachmentType
class Test_001():
    username="pratik"
    log = Logging_Class.log_genarator()
    # @pytest.mark.skip
    @allure.severity(allure.severity_level.CRITICAL)
    def test_additem(self,setup):
        self.log.info(" test_additem is started")
        self.driver=setup
        self.log.info(" Browser is opening ")
        self.driver.get("https://demoblaze.com/index.html")
        self.log.info(" Going to https://demoblaze.com/index.html url")
        self.driver.maximize_window()
        self.obj=AddItems(self.driver)
        self.driver.implicitly_wait(360)
        self.obj.clickphone()
        self.log.info(" Clicking on phone tab")
        self.obj.clickSamsung()
        self.log.info("Clicking on phone samsung ")
        self.obj.clickAddTocart()
        self.log.info("Clicking addTocart button ")
        self.obj.explicitwaitAlert()
        self.obj.clickhome()
        self.log.info("Clicking home  button ")
        self.obj.clickmonitor()
        self.log.info("Clicking on monitor ")
        self.obj.clickAsus()
        self.log.info("Clicking  on Asusu")
        self.obj.clickAddTocart()
        self.log.info("Clicking addTocart button ")
        self.obj.explicitwaitAlert()
        self.obj.clickhome()
        self.log.info("Clicking home  button ")
        self.obj.clickLaptop()
        self.log.info("Clicking  on Laptop")
        self.obj.clickDell()
        self.log.info("Clicking  on Dell")
        self.obj.clickAddTocart()
        self.log.info("Clicking addTocart button ")
        self.obj.explicitwaitAlert()
        self.obj.clickCarturl()
        self.log.info("Clicking carturl  ")
        self.obj.verify_amount()
        # time.sleep(5)
        # self.row=self.obj.fetchRows()
        # self.col=self.obj.fetchCols()

        self.obj.clickPlaceOrder()
        self.log.info("Clicking Place order button ")

        time.sleep(1)
        # self.explicitwaitSet(self.obj.setName()).send_keys("India")
        # self.driver.find_element(By.XPATH,self.obj.name).send_keys('rahul')
        self.obj.setName()
        self.log.info(" Entering name ")
        self.obj.setCountry()
        self.log.info(" Entering country")
        self.obj.setCity()
        self.log.info(" Entering city ")
        self.obj.setCreditCard()
        self.log.info(" Entering  credit card detail ")
        self.obj.setMonth()
        self.log.info(" Entering  the month ")
        self.obj.setYear()
        self.log.info(" Entering  year ")
        self.obj.clickPurchse()
        self.log.info(" Clcking on purchase button ")
        if self.obj.fetchYourPurchase()=="Thank you for your purchase!":
           self.log.info(" test_additem is passed ")
           assert True
        else :
            self.log.info(" test_additem is failed ")
            allure.attach(self.driver.get_full_page_screenshot_as_png(),name="test_additemfailed",
                          attachment_type=AttachmentType.PNG)
            assert False

        self.log.info(" test_additem is completed ")

        # self.obj.clickOk()
