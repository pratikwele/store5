from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# class Base:
#
#     def explicitwait(self,locator):
#         WebDriverWait(self.driver, 20).until(
#             expected_conditions.presence_of_element_located((locator))).click() def explicitwaitAlert(self):
    #    WebDriverWait(self.driver, 20).until(expected_conditions.alert_is_present())
    #    self.driver.switch_to.alert.accept()

    # def explicitwaitSet(self,locator):
    #     WebDriverWait(self.driver, 20).until(
    #         expected_conditions.presence_of_all_elements_located((By.XPATH,locator)))