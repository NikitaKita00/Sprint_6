import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from project.pages.base_page import BasePage


class MainPageLocators:
    # Логотип Самокат - уникальный и стабильный элемент загрузки главной страницы
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    ORDER_BUTTON_1 = (
        By.XPATH,
        "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')])[1]",
    )
    ORDER_BUTTON_2 = (
        By.XPATH,
        "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')])[2]",
    )


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Открыть главную страницу")
    def open(self, url="https://qa-scooter.praktikum-services.ru/"):
        self.open_url(url)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_load(self, timeout=15):
        """Ожидание загрузки главной страницы по появлению логотипа Самоката"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.locators.LOGO_SCOOTER)
        )

    @allure.step("Нажать кнопку 'Заказать' по индексу {index}")
    def click_order_button(self, index=0):
        buttons = [self.locators.ORDER_BUTTON_1, self.locators.ORDER_BUTTON_2]
        target = buttons[index]
        element = self.find_element(target)
        self.scroll_into_view(element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)
