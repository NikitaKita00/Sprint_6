from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from project.locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = MainPageLocators()
        self.url = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        self.driver.get(self.url)

    def wait_for_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.MAIN_PAGE_CONTENT)
        )

    def click_header_order_button(self):
        self.driver.find_element(*self.locators.HEADER_ORDER_BUTTON).click()

    def click_footer_order_button(self):
        self.driver.find_element(*self.locators.FOOTER_ORDER_BUTTON).click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.locators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.locators.YANDEX_LOGO).click()
